
class Users:
    def __init__(self, login, password, access_rights):
        self.login = login
        self.password = password
        self.access_rights = None

    def check_password (login, password):

        if login not in users:
            print("Такого пользователя не существует!")

        add_hash = login[users]
        hash_password = hashlib.sha256(password.encode()).hexdigest()

        if hash_password == add_hash:
            return True
        else:
            return False

        if check_password == True:
            print("Вход выполнен успешно!")
        else:
            print("Неверный логин или пароль")


us_er = Users
users = {"user6":"123456789", "user7":"pass12345"}
login = input("Введите имя пользователя")
password = input("Введите пароль")
