# Password Cracking

**File formats**

The files `shadow.txt` and `passwd.txt` have formats similar to the Unix files (with a bit of simplification). The different fields of a user record are separated by “:”. The following explains the format of each record in these files. Some of these fields can be empty (“::” indicates an empty field)

*Record format of file passwd.txt:*
```
login_name:password_hash:user_number:user_group_number:comment:home_director:command_shell
```

The flowing is a record example
```
jsmith:x:1001:1000:Joe Smith,Room 1007,Phone(234)555-0044:/home/jsmith:/bin/sh
```

**x** in the password_hash field indicates that the password hash is stored separately in a shadow file.

*Record format of file shadow.txt:*
```
login_name:$salt$password_hash:other_colon_separated_fields
```

The following is a record example
```
jsmith:$AQKDPc5E$SWlkjRWexrXYgc98F.:17555:3:30:5:30:17889:
```
___

## Cracked passwords

|**User name**|**password**|
|---------|:-------:|
|aisha	|Qm7B|
|aiman	|september|
|myousef|	12345678|
|asmaa	|banana|
|mike	|abc123|
|daniel	|password123|

## Time analysis

**Machine**:

MacBook Pro (16-inch, 2019)
Processor 2.3 GHz 8-Core Intel Core i9
Memory 16 GB 2667 MHz DDR4

|**Attack**|**Time it took**|
|-------|:----------:|
|Brute force (step 1)|	2.8848648071289062 * 10^-5  sec|
|Generating the rainbow table| 	0.00045680999755859375 sec|
|Cracking the passwords in /etc/passwd|	2.6941299438476562 * 10^-5 sec|
---
## Running and testing the code
The code is in python.
1.	main1.py
2.	main2.py
3.	main3.py

To run 1st program (Brute force attack)
```
python main1.py
```

To run 2nd program (Dictionary attack)
```
python main2.py
```

To run 3rd program (Authenticating)
```
python main3.py
```