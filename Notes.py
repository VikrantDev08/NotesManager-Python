#Notes-Python
#login() - for user to login , checks username and password in userdata file
#signup() - for first time user , asks them to enter unique username that doesnot
#already exist, if it exist it tells the user to enter an new username , also takes
#email and password , save this data in a csv file(userdata) in a list[username,email,password]
#createnew file() - executed when user wants to create a new file (takes file name as input)
#accessoldfile(filename) - allows user to choose to raed contents of the file, add furthur
#contents  or erase previous contents and add new once

import csv

def login():
    username = input("Enter User Name: ")
    password = input("Enter Password: ")
    
    # Use 'r' for reading, and a 'with' block to automatically close the file
    with open("userdata.csv", mode='r', newline='') as f:
        ro = csv.reader(f)
        for i in ro:
            # Check if row has at least 3 columns to prevent IndexError
            if len(i) > 2 and username == i[0] and password == i[2]:
                print("Login successful!")
                return username
                
    print("Username not found or incorrect password")
    return None

def signup():
    f=open("userdata.csv",'a+',newline='\n')
    ro=csv.reader(f)
    L=[]
    for i in ro:
        L+=i[0]
    a=b=1
    while a==1:
        username = input("Enter you username:")
        if username in L:
            print("This Username is already Taken")
            a=1
        else:
            while b==1:
                email = input("Enter Your Email ID:")
                password = input("Enter your password:")
                confirmpassword = input("Enter password entered above to confirm it:")
                if password==confirmpassword:
                    print("-----ID created successfully-----")
                    print("Username:",username)
                    print("email:",email)
                    print("Password:",password)
                    print("Remember the above credential for future login")
                    b=0
                    a=0
                else:
                    print("Different password Entered !! Enter the same password in both to confirm it")
                    b=1
    f.close()
    f=open("userdata.csv",'a',newline='\r\n')
    wo=csv.writer(f)
    L1=[username,email,password]
    wo.writerow(L1)
    f.close()
    return username
    

def createnewfile(username):
    name=input("Enter the name of the file:")
    f=open("{}.txt".format(name),'w')
    content=input("Enter Contents of the file:\n")
    f.write(content)
    f.close()
    f=open("Contents.csv",'a',newline='\r\n')
    wo=csv.writer(f)
    wo.writerow([username,name])
    f.close()

    
def accessoldfile(username):
    a=1
    while a==1:
        print("--------Possible Actions---------")
        print("1.Access list of all existing files for this username\n2. Open an old File and add to its existing contents\n3. Erase old contents of existing file and Rewrite\n4. Read File \n5. Back To main Menu ")
        act=int(input("Enter Your action(1,2,3,4 or 5):"))
        if act == 1:
            f=open("userdata.csv",'a',newline='\n')
            ro=csv.reader(f)
            print("--------Your Files are as follows---------")
            for i in ro:
                if i[0]==username:
                    print(i[1])
            f.close()
            
        elif act==2:
            name=input("Enter name of the file:")
            f=open("{}.txt".format(name),'a')
            data=input("Enter Data you want add in File:\n")
            data+="\n"
            f.write(data2)   
            f.close()

        elif act==3:
            name=input("Enter name of the file:")
            f=open("{}.txt".format(name),'w')
            data=input("Enter Data you want add in File:\n")
            f.write(data)
            f.close()

        elif act==4:
            name=input("Enter name of the file:")
            f=open("{}.txt".format(name),'r')
            data=f.read()
            print(data)
            f.close()

        elif act==5:
            break

        else:
            print("Enter a Valid Action")

def main(username):
    m=1
    while m==1:
        print("-------Available action-------")
        print("1. Create a new file\n 2. Work on old files\n3. Exit")
        act=int(input("Choose your action(1,2 or 3):"))
        if act==1:
            createnewfile(username)
            m=1
        if act==2:
            accessoldfile(username)
            m=1
        if act==3:
            print("Exiting the program")
            break


#main body of the program

print("==========WELCOME TO NOTES===========")
k=1
while k==1:
    print("***Press 1 to login\n***Press 2 to signin(if you are using for the first time")
    act=int(input("Enter 1,2 or 3 to exit:"))
    if act == 1:
        username=login()
        k=3
    if act== 2 :
        username=signup()
        k=2
    if act == 3:
        print("Exiting")
        k=0
        break
    else:
        print("Enter a Valid Action")


if k==0:
    print(":)bye")
else:
    main(username)
    
            
            
            
            
                
            
        










