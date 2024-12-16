from os import write

from cryptography.fernet import Fernet

#this is a module which help you encrypt a text .
#take a string of text & using a key , turn it into completely random string of text
#that you cannot turn back to the original text without the key


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key



master_pwd = input("what is the master password?")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split(" | ")
            print("User : ",user,"|","Password:",fer.decrypt(passw.encode()).decode() )


def add():
    name = input("account number: ")
    pwd = input("Password: ")

    with open('passwords.txt','a') as f:
        f.write(name + ' | '+ fer.encrypt(pwd.encode()).decode()+"\n" ) # we set name of the file as f so we use f here.


    #The purpose of with is to automatically close the file when you are done with it
    #cuz usually we do is file = open('passwords.txt','a') , but then in this case
    #we also need to manually close the file by file.close()
    # w mode is to write , create a new file or override the already existing file , which
    # override the contents of the while and remove the existing content.
    #r is simply read mode
    #a append mode , will let you add content to end of the file ,
    #it'll also create a new file if doesn't already exist

    pass

while True:
    mode = input("would you like to add a new pwd or view the existing one (view/add)?, press 'q' to quit.").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
        #here note we could have just written the coondition and whatever we wanna
        # do when we put view and add within the if but to make the code cleaner
        #we choose to write it in a func

    elif mode == 'add':
        add()

    else:
        print("Invalid mode")
        continue