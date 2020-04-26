from resources import user


def set_user_routes(api, conn):
    user_resource = user.User(conn)

    api.add_route('/users/{id}', user_resource, suffix='item')
    api.add_route('/users', user_resource, suffix='collection')
