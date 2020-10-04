#import numpy as np
import hashlib
import time

# handling word list
def store_wordlist(file):
    _dictionary = {}
    f = open(file, "r")
    contents = f.readlines()
    for x in contents:
        #print(x)
        _word = x.rstrip("\n")
        _dictionary[hashlib.md5(_word.encode()).hexdigest()] = _word
    
    return _dictionary

wordlist = store_wordlist("wordlist.txt")
#print(wordlist)

start = time.time()
# display rainbow table
for key, value in wordlist.items():
    print(key, '->', value)
end = time.time() - start
print("Time taken to generate rainbow table: ", end)

columns = ['username', 'password', 'user id', 'group id', 'user id info', 'home directory', 'command/shell']

# handling accounts
def process_data(file):
    _dictionary = {}
    f = open(file, "r")
    contents = f.readlines()
    for x in contents:
        count = 0
        account = {}
        record = x.split(':')
        for item in record:
            account[columns[count]] = item
            count += 1
        _dictionary[account['password']] = account

    return _dictionary

accounts = process_data("passwd.txt")

#compre accounts with known passwords
start = time.time()
for key, value in accounts.items():
    try:
        print(value['username'], ",", wordlist[value['password']])
    except:
        continue
end = time.time() - start
print("Time taken: ", end)