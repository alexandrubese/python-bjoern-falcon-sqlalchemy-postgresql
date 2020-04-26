from routes import user_routes


def init_app_routes(api):
    user_routes.set_user_routes(api)
