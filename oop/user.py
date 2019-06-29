class User(object):

    def __init__(self, id, name, username):
        self.id = id
        self.name = name
        self.username = username
        self.client = self.Client()

    def fetch_user(self):
        print(f"Id: {self.id}\nName: {self.name}\nUsername: {self.username}")
        self.client.fetch_client()

    class Client(object):
        def __init__(self):
            self.domain = "http://mbrsagorbd.wordpress.com"
            self.email = "brshagor.cse@gmail.com"

        def fetch_client(self):
            print(f"Domain Name: {self.domain}\nEmail: {self.email}\n")


user1 = User(1, "Md.Bozlur Rosid Sagor", "mbr-sagor")
user1.fetch_user()
