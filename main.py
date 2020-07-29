import json
import time
import sys

def main():
    login_or_register = input("Do you have an account? y/n: ")

    try:

        with open('users.json') as f:
            jsonObject = json.load(f)
    except json.decoder.JSONDecodeError:
        print("json decoder error")

    def verifyLogin(_username, _password):
        try:

            for cred in jsonObject["users"]:
                if cred['username'] == _username and cred['password'] == _password:
                    print("you are now logged in")
                    sys.exit()
            else:
                print("incorrect username/password")
                login()
        except KeyError:
            print("Username/pass does not exist")
            login()

    def AddUser(_username, _password) -> None: 
        newl = {'username': _username,'password': _password}
        jsonObject['users'].append(newl)
        outstring = json.dumps(jsonObject)
        with open("users.json", "w") as json_file:
            json_file.write(outstring)
        login()
    def login() -> None:
        username_input = input("username: ")
        pass_input = input("password: ")
        verifyLogin(username_input, pass_input)
    def register() -> None:
        new_user = input("please enter a username: ")
        new_pass = input("please enter a password: ")
        confirm_pass = input("please confirm your password: ")

        if new_pass != confirm_pass:
            print("your passwords did not match")
            register()
        else:
            AddUser(new_user, new_pass)
    
    if login_or_register == "y":
        print('login')
        login()
    elif login_or_register == "n":
        print('register')
        register()

if __name__ == "__main__":
    main()

