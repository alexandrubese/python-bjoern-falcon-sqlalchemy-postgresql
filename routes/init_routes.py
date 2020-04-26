from routes import user_routes


def init_app_routes(api, conn):
    user_routes.set_user_routes(api, conn)
