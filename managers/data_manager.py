class DataManager(object):
    def __init__(self, conn):
        self.conn = conn

    @staticmethod
    def set_columns(data, cursor):
        items = []
        for x in data:
            item = {}
            c = 0
            for col in cursor.description:
                item.update({col[0]: x[c]})
                c = c + 1
            items.append(item)
        return items

    def get_data(self, query):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()

            return {"status": True, 'data': self.set_columns(records, cursor)}
        except Exception as error:
            cursor.execute('ROLLBACK')
            self.conn.commit()
            return {"status": False, "message": str(error), "data": None}
