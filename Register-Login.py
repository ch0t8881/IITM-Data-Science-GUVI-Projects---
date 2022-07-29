def registration(username=None,password=None,password1=None):
    username = input("Create Username       : ")
    password = input("Create Password       : ")
    password1 = input("Re_enter Your Password: ")
    db=open("database.txt","r")
    v = []
    for x in db:
        a,b= x.split(",")
        b=b.strip()
        c=a,b
        #v.append()
    if password1!=password:
        print("Password Not Match")
        registration()
    elif len(password) < 5:
        print("password too short")
    elif len(password) > 16:
        print("pass too long")

    else:
        valid = 0
        user = []
        if username[0].isalpha():
            if "@." not in username:
                if "@" in username:
                    if "." in username:
                        user.append(username)
                else:
                    pass
            else:
                print("invalid")
        else:
            print("invalid")

        if len(user) > 0:
            if username not in v:
                valid = valid + 1
                pass
            else:
                print("username already exist")
                registration()

        u, l, d, s = 0, 0, 0, 0
        for x in password:
            if x.isdecimal():
                d = 1
            if x.upper() in password:
                u = 1

            if x.lower() in password:
                l = 1

            if x == "@" or x == "$" or x == "_":
                s = 1
        if u == 1 and l == 1 and d == 1 and s == 1:

            valid = valid + 1
        else:
            print("invalid password")

        if valid == 2:

            with open("database.txt", "a") as db:
                db.write(username + ", " + password1 + "\n")
                print("***** REGISTER SUCCESSFUL *****")
            Home_page()
        else:
            print("please try again")
            registration()

            
def welcome():
    print("Welcome to your dashboard")

def Forget_password(username=None):
    Username = str(input("Enter your username:"))

    if not len(Username ) < 1:

        # noinspection PyUnreachableCode
        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
                f.append(b)
            data = dict(zip(d, f))

            if Username in d:

                print("your password is: ",f[d.index(Username)])
            else:
                print("Username does not exist please register")
                registration()


        else:
            pass

def login(username=None,password=None):
    Username = input("Enter your username:")
    Password = input("Enter your Password:")

    if not len(Username or Password) < 1:

        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
                f.append(b)
            data = dict(zip(d, f))
            try:
                if data[Username]:
                    try:
                        if Password == data[Username]:
                            print("Login success!")
                            print("Hello!", Username)
                            welcome()
                        else:
                            print("Incorrect password or username")
                            print("Please register")
                            print("      or")
                            print("Please select forget password")

                            Home_page()
                    except:
                        print("Incorrect password or username")
                        print("Please register")
                        print("      or")
                        print("Please select forget password")
                        Home_page()


                else:
                    print("Password or username doesn't exist")
                    print("Please register")
                    print("      or")
                    print("Please select forget password")
                    Home_page()
            except:
                print("Password or username doesn't exist")
                Home_page()



    else:
        print("Please attempt login again")
        login()

    pass

def Home_page(option=None):
    print("please select the option")
    option=input(" 1.Login: \n 2.Register: \n 3.Forget_password: \n 4.Exit \n")
    if option == "1":
        login()
    elif option == "2":
        registration()
    elif option == "3":
        Forget_password()
    elif option == "4":
        print("Thank You so much...")
        exit()
    else:
        print("invalid option")
        Home_page()
Home_page()
