import hashlib
from itertools import chain, product
import time

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

str1 = "".join([chr(x) for x in range(ord('a'), ord('z') + 1)])
str2 = str1.upper()
str3 = "".join([chr(x) for x in range(ord('1'), ord('9') + 1)])
charset = str2 + str1 + str3
max_length = 4
print("Charset is\t: ", charset)
print("Max length is\t: ", max_length)

start = time.time()
word_list = list(bruteforce(charset, max_length))
end = time.time() - start
print("Time taken to create word list (approx)\t\t:", round(end,2), " sec")

def create_dict(filename, wordlist):
  rb = {}
  for each in wordlist:
    str2hash = each
    result = hashlib.md5(str2hash.encode()) 
    rb[result.hexdigest()] = str2hash
  return rb

start = time.time()
rainbow = create_dict("my_dict.txt", word_list)
end = time.time() - start
print("Time taken to create hash dictionary(approx)\t:", round(end,2), " sec")
info = {}
file = open("passwd.txt", "r")
for each in file:
  line_words = each.split(':')
  info[line_words[0]] = line_words[1]

print('-'*30)
start = time.time()
for username, password in info.items():
  if password in rainbow.keys():
    print("Username\t:", username)
    print("Password\t:", rainbow[password])
    print('-'*30)
end = time.time() - start
print("Time taken to crack password\t:", end, " sec")
