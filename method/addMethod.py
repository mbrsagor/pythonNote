def add_user(user, user_list=[]):
    user_list.append(user)
    return user_list

users = ['sagor', 'ohi']

print(add_user('ohi', users))
