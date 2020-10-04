import hashlib

info = {}
file = open("shadow.txt", "r")
for each in file:
  line_words = each.split(':')
  line_words[1] = line_words[1].split("$")[1:]
  info[line_words[0]] = line_words[1]

def login(username, password):
  salt, pwd_hash = info[username]
  str2hash = password + salt
  result = hashlib.md5(str2hash.encode()) 
  if(result.hexdigest() == pwd_hash):
    print("Login Succeeded")
  else:
    print("Login Failed")

username = input("Login name: ")
password = input("Password: ")
login(username, password)