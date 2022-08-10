class Auth(object):
    """
    This script (`Auth.py` file) using simple users login authentication
    """
    is_login = False

    def profile(self):
        """
        :return: When user login success then return `profile` otherwise return invalid user message
        """
        if not self.is_login:
            return "\nyou are not register user"
        else:
            return "==========================\nWelcome to our website!!\nYou are register user.\n=========================="

    def login(self, username, password):
        """
        :param username:
        :param password:
        :return: password not match message
        """
        if username == 'admin' and password == 'a12345':
            if self.is_login:
                return f"{username} already login"
            else:
                self.is_login = True
                return self.profile()
        else:
            return "\nSorry!! username and password doesn't match."

    def status(self):
        """
        Here check user status like, login user=active user
        :return: otherwise none
        """
        if self.is_login:
            print("user activate")
        elif not self.is_login:
            self.is_login = False


if __name__ == '__main__':
    """
    Here instantiating `Auth` class
    """
    auth = Auth()
    print(auth.login(
        input("Enter username:"),
        input("Enter password:")
    ))
    auth.status()
