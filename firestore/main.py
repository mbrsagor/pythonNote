import requests
import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account.
cred = credentials.Certificate("pythonfirestore.json")

app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection("users").document("alovelace")
doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

users_ref = db.collection("users")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")


def send_message(first, last, born):
    pass
