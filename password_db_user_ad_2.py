import mysql.connector as mc
import random

mycon = mc.connect(host="localhost", user="root", passwd="Adu@5146", database="password_manager")
mycursor = mycon.cursor()


def configuration():
    cmnd = "create table users(Name char(20),paswd varchar(10),table_name char(30))"
    mycursor.execute(cmnd)

    print("Database successfully established")


def encrypt(arg):
    new = arg.split()
    l = []
    for i in range(len(new)):
        for j in new[i]:
            l.append(j)
    convert = []
    for m in l:
        convert.append(ord(m))
    # print(convert)
    convert_2 = []
    for mm in convert:
        convert_2.append(hex(mm))

    # print(convert_2)
    str__ = " "
    for ad in convert_2:
        str__ = str__ + ad

    return str__


def decrypt(arg):
    sp = arg.strip()
    n = 4
    output = [(sp[i:i + n]) for i in range(0, len(sp), n)]

    door = []
    for j in output:
        hex_string = j[2:]
        bytes_object = bytes.fromhex(hex_string)

        ascii_string = bytes_object.decode("ASCII")

        door.append(ascii_string)
    str1 = ""
    for new in door:
        str1 = str1 + new
    return str1


# print(decrypt(" 0x550x570x260x3f0x4f0x430x250x4b"))

def appends(table):
    service = input("Enter Service name: ")
    pa_con = input("Would you like me to suggest a password or you have a password (y/n)?")
    if pa_con == "y":

        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
        pass_length = 8
        final_password = "".join(random.sample(s, pass_length))
        print("Your new password is ", final_password)
        # print(type(final_password))

        sq_l = "INSERT INTO " + table + " (Service ,Password) VALUES (%s, %s)"
        cmnd = (service, encrypt(final_password))
        mycursor.execute(sq_l, cmnd)

        mycon.commit()
        print("data successfully added")

    else:
        paswd = input("Enter your password: ")

        sq_l = "INSERT INTO " + table + "(Service ,Password) VALUES (%s, %s)"
        cmnd = (service, encrypt(paswd))
        mycursor.execute(sq_l, cmnd)

        mycon.commit()
        print("data successfully added")

    return


def access(table):
    inp = input("Enter the name of the service you would like to access: ")
    cmmd = "select * from " + " " + table
    cmmd__ = inp
    mycursor.execute(cmmd)

    my_data = mycursor.fetchall()
    neo = []

    for cap in my_data:
        neo.append(cap)
    # print(neo)

    music = []
    for i in range(len(neo)):
        for j in neo[i]:
            if j == cmmd__:
                music.append(neo[i])
    # print(music)

    for index, tuple in enumerate(music):
        print("Service: ", tuple[0])
        print("Password: ", decrypt(tuple[1]))

    return


def main_runner(user_name):
    bose = False
    while not bose:
        print("[(enter [a] for adding data),(enter [s] for accessing data)]")
        friday = input("Enter what would you like to do:")
        if friday == "a":
            nacl = False
            while not nacl:
                ask = input("Do you want to add data? (y/n)?")

                if ask == "y":
                    appends(table_extraction(user_name))
                else:
                    nacl = True
        elif friday == "s":
            # ask = input("Enter name of your table: ")

            access(table_extraction(user_name))
        else:
            bose = True
    return


def lst_to_string(lst):
    dummy = ""
    for i in lst:
        dummy = dummy + i + " "
    return dummy


# ---------------------------------------------------------------------------------------------------------
def rem_usr(name, table):
    confirm = input("Are you sure you want to delete your account (y/n)?")
    if confirm == "y":

        pswd = str(input("Enter your account password: "))

        # You have to first remove the user from the users table
        # Then you have to drop the table
        nm = name
        pswd_check = "select paswd from users where name=(%s)"
        pswd_tup = (nm,)
        mycursor.execute(pswd_check, pswd_tup)

        lst = []
        for i in mycursor:
            lst.append(i)
        fin_lst = []
        for index, tup in enumerate(lst):
            fin_lst.append(tup[0])
        check_authenticity = lst_to_string(fin_lst)


        if check_authenticity.strip() == pswd:

            cmd_usr = "DELETE FROM USERS WHERE NAME LIKE (%s)"
            cmd_tup = (nm,)
            mycursor.execute(cmd_usr, cmd_tup)
            mycon.commit()

            cmd_tab = "DROP TABLE " + table
            mycursor.execute(cmd_tab)
            print("User account deleted")
        else:
            print("Your password for your account is incorrect")
            print("Your account cannot be deleted without correct password")


    else:
        print("Okay, account is not removed")

# --------------------------------------------------------------------------------------------------------
def table_extraction(name):
    ext_cmd = "SELECT table_name from users where name like(%s)"
    d_tup = (name,)
    mycursor.execute(ext_cmd, d_tup)

    tables = mycursor.fetchall()
    l = []
    for (table_name,) in tables:
        l.append(table_name)
    str_1 = ""
    for i in l:
        str_1 = str_1 + i
    if len(l) != 0:
        return str_1
    # here str_1 is the user's table
    else:
        return "No such user"


# --------------------------------------------------------------------------------------------------------
def paswd_strength(password):
    # Min length of the password must be 5
    # special characters
    sp_chr = ["!", "@", "#", "$", "%", "&"]
    # Upper case and lower case
    # numbers
    check_lst = list(password)
    check_count = 0
    # print(check_lst)

    if len(check_lst) >= 8:
        check_count = check_count + 1

    for j in check_lst:
        for m in sp_chr:
            if j == m:
                check_count = check_count + 1
        if j.isupper():
            check_count = check_count + 1
        elif type(check_lst) == int:
            check_count = check_count + 1

    # print(check_count)

    if check_count >= 4:
        return "Password is safe"
    else:
        return "Password is not safe"


# --------------------------------------------------------------------------------------------------------

def secure_pass():
    note = False
    while not note:
        print("--------------------------------------------------------------------------")
        print("Enter ac to access to existing data and alter data in your personal table")
        print("Enter cr to create a new account")
        print("Enter del to delete a account")
        print("Enter e to exit prompt")
        print("--------------------------------------------------------------------------")

        guide = input("Enter What would you like to do: ")
        if guide == "ac":
            usr = input("Enter user name: ")

            usr_check = "select paswd from users where Name like '%" + usr + "%' "

            mycursor.execute(usr_check)

            my_data = mycursor.fetchall()
            # print(my_data)
            # print(type(my_data))

            manipulate = []

            for fin_passwd in my_data:
                manipulate.append(fin_passwd)

            # using list comprehension
            # print("Manipulate: ",manipulate)
            out = [item for t in manipulate for item in t]

            splt = ""
            for ma in out:
                splt = splt + ma

            paswd = input("Enter your password: ")

            if paswd == splt:
                print("Welcome ", usr)
                main_runner(usr)

            else:
                print("Invalid credentials")
                note = True

        elif guide == "cr":

            new_usr = input("Enter new user name: ")
            new_paswd = input("Enter user new password: ")
            new_paswd_chech = input("Confirm your password: ")

            ck = paswd_strength(new_paswd_chech)
            if ck == "Password is safe":

                if new_paswd == new_paswd_chech:

                    # Creating a new table
                    create__ = new_usr + "_pswd"  # input("Enter the name of your table: ")
                    sql1 = "CREATE TABLE "
                    sql2 = "(Service CHAR(20), Password MEDIUMTEXT)"

                    final = sql1 + create__ + sql2
                    # print(final)

                    mycursor.execute(final)
                    print("New Account Created...")

                    # Updating user credentials to users table
                    # Use insert into command

                    user_update = "INSERT INTO users (Name,paswd,table_name) VALUES (%s, %s, %s)"

                    comnd = (new_usr, new_paswd_chech, create__)
                    mycursor.execute(user_update, comnd)

                    mycon.commit()
                    # print("Successfully added user to user table")

                # ---------------------------------------------------------
                else:
                    print("Passwords are not matching")
            else:
                weak = input("Your password is not strong do you wish to continue [(y)/n]?")
                if weak == "y":
                    # Creating a new table
                    create__ = new_usr + "_pswd"  # input("Enter the name of your table: ")
                    sql1 = "CREATE TABLE "
                    sql2 = "(Service CHAR(20), Password MEDIUMTEXT)"

                    final = sql1 + create__ + sql2
                    # print(final)

                    mycursor.execute(final)
                    print("New Account Created...")

                    # Updating user credentials to users table
                    # Use insert into command

                    user_update = "INSERT INTO users (Name,paswd,table_name) VALUES (%s, %s, %s)"

                    comnd = (new_usr, new_paswd_chech, create__)
                    mycursor.execute(user_update, comnd)

                    mycon.commit()
                else:
                    note = True

        elif guide == "del":
            n = input("Enter user name: ")

            rem_usr(n, table_extraction(n))

        elif guide == "e":
            note = True
        else:
            print("Wrong input...")


secure_pass()
