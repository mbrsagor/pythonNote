import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account.
cred = credentials.Certificate("pythonfirestore.json")

app = firebase_admin.initialize_app(cred)
db = firestore.client()


def get_users():
    # list of users
    my_users = []
    users = db.collection('users')
    for user in users.stream():
        my_users.append(user.to_dict())
    resp = {
        'status': True,
        'message': 'Successfully data returned',
        'data': my_users
    }
    return resp


def create_user(first, last, born):
    # Create new user
    users_ref = db.collection("users")
    print("Create Successfully.")
    return users_ref.add({"first": first, "last": last, "born": born})


def update_user(first, last, born, user_id):
    """
    User update function
    params: user_id: user id
    """
    users_ref = db.collection("users").document(user_id)
    return users_ref.update({"first": first, "last": last, "born": born})
