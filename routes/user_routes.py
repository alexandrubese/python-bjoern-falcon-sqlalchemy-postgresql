from resources import user


def set_user_routes(api):
    user_resource = user.User()

    api.add_route('/mock_user', user_resource, suffix='mock_user')
    api.add_route('/users/{id}', user_resource, suffix='item')
    api.add_route('/users', user_resource, suffix='collection')
