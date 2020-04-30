from sqlalchemy import inspect


class Serializer(object):
    def __init__(self):
        pass

    @staticmethod
    def parse_dict(obj, with_relationships=True):
        d = {}
        for column in obj.__table__.columns:
            if with_relationships and len(column.foreign_keys) > 0:
                # Skip foreign keys
                continue
            d[column.name] = getattr(obj, column.name)

        if with_relationships:
            for relationship in inspect(type(obj)).relationships:
                val = getattr(obj, relationship.key)
                d[relationship.key] = Serializer.parse_dict(val) if val else None
        return d

    @staticmethod
    def parse_list(items):
        return [Serializer.parse_dict(item) for item in items]
