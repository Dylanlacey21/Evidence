import mdvl

key = "11035489762"

def loggedin():
  print("You Are Now Logged In")

def login1():
  def banner():
    MyFile = open("Welcome.txt","r")
    print("""
Don't Type Upper-Case""")
    banner = MyFile.read()
    mdvl.main(banner)

  def Help():
    MyFile = open("Help.txt","r")
    help_ = MyFile.read()
    mdvl.main(help_)
    login1()

  def login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")  
    for line in open("accountfile.txt","r").readlines():
        login_info = line.split()
        print(login_info)
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            loggedin()
            return True
    print("Incorrect credentials.")
    login1()
    return False

  def register():
    username = input("Type Your Email: ")
    password1 = input("Please input your desired password: ")
    password2 = input("Type your desired password again: ")
    if password1 == password2:
      file = open("accountfile.txt","a")
      file.write("\n")
      file.write(username)
      file.write(" ")
      file.write(password1)
      file.close()
      print("You're Account Is Now Created!")
      login1()
    else:
      print("Your Password is not the same")
  
  
  banner()
  x = input("Home.Term:\> ")
  
  if x == "help":
    Help()

  elif x == "login":
    login()

  elif x == "register":
    register()
  
  else:
    print("Not Found")
login1()