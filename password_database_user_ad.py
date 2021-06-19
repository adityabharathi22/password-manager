import mysql.connector as mc
import random


def appends(table):
    mycon = mc.connect(host="localhost", user="aditya", passwd="adu5146", database="password_manager")

    mycursor = mycon.cursor()

    service = input("Enter Service name: ")
    pa_con = input("Would you like me to suggest a password or you have a password ([y]/[n])?")
    if pa_con == "y":

        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
        pass_length = 8
        final_password = "".join(random.sample(s, pass_length))
        print("Your new password is ", final_password)
        #print(type(final_password))

        sq_l = "INSERT INTO " + table + " (Service ,Password) VALUES (%s, %s)"
        cmnd = (service, final_password)
        mycursor.execute(sq_l, cmnd)

        mycon.commit()

    else:
        paswd = input("Enter your password: ")

        sq_l = "INSERT INTO " + table + "(Service ,Password) VALUES (%s, %s)"
        cmnd = (service, paswd)
        mycursor.execute(sq_l, cmnd)

        mycon.commit()
    return

def access(table):
    mycon = mc.connect(host="localhost", user="aditya", passwd="adu5146", database="password_manager")

    mycursor = mycon.cursor()
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
    #print(music)

    for index, tuple in enumerate(music):
        print("Service: ", tuple[0])
        print("Password: ", tuple[1])

    return

def main_runner():
    bose = False
    while not bose:
        print("[(enter [a] for adding data),(enter [s] for accessing data)]")
        friday = input("Enter what would you like to do:")
        if friday == "a":
            nacl = False
            while not nacl:
                ask = input("Do you want to add data? ([y]/n)?")
                if ask == "y":
                    ask = input("Enter name of your table: ")
                    appends(ask)
                else:
                    nacl = True
        elif friday == "s":
            ask = input("Enter name of your table: ")

            access(ask)
        else:
            bose = True
    return

# --------------------------------------------------------------------------------------------------------
def secure_pass():
    mycon = mc.connect(host="localhost", user="aditya", passwd="adu5146", database="password_manager")

    mycursor = mycon.cursor()

    note = False
    while not note:
        print("--------------------------------------------------------------------------")
        print("Enter ac to access to existing data and alter data in your personal table")
        print("Enter cr to create a new account")
        print("--------------------------------------------------------------------------")

        guide = input("Enter What would you like to do: ")
        if guide == "ac":
            usr = input("Enter user name: ")

            usr_check = "select paswd from users where Name like '%" + usr + "%' "

            mycursor.execute(usr_check)

            my_data = mycursor.fetchall()
            #print(my_data)
            #print(type(my_data))

            manipulate = []

            for fin_passwd in my_data:
                manipulate.append(fin_passwd)

            # using list comprehension
            #print("Mani: ",manipulate)
            out = [item for t in manipulate for item in t]

            splt = ""
            for ma in out:
                splt = splt + ma

            #splt is the password
            #print(splt)
            # printing output
            #print("Existing password: ",splt)
            #print("Existing password type: ",type(splt))

            paswd = input("Enter your password: ")
            #print("entered password: ",paswd)
            #print("entered password type: ",type(paswd))


            if paswd == splt:
                print("Welcome ",usr)
                main_runner()

            else:
                print("Invalid credentials")
                note = True

        elif guide == "cr":

            new_usr = input("Enter new user name: ")
            new_paswd = input("Enter user new password: ")
            new_paswd_chech = input("Confirm your password: ")

            if new_paswd == new_paswd_chech:

                #Creating a new table
                create__ = input("Enter the name of your table: ")
                sql1 = "CREATE TABLE "
                sql2 = "(Service CHAR(20), Password varchar(20))"

                final = sql1 + create__ + sql2
                #print(final)

                mycursor.execute(final)
                print("New Account Created...")

                #Updating user credentials to users table
                #Use insert into command

                user_update = "INSERT INTO users (Name,paswd,table_name) VALUES (%s, %s, %s)"

                comnd = (new_usr, new_paswd_chech , create__)
                mycursor.execute(user_update, comnd)

                mycon.commit()
                #print("Successfully added user to user table")

                #---------------------------------------------------------
            else:
                print("Passwords are not matching")
        else:
            note = True

secure_pass()
