from routes import user_routes


def init_app_routes(api, db_connection):
    user_routes.set_user_routes(api, db_connection)
