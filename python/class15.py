import re
age = [25, 30, 28, 40, 45]

# print(max(age))
# print(min(age))
# print(sum(age))

# print(sorted(age))
# print(list(reversed(age)))
# print(list(reversed(sorted(age))))

# print(len("hello"))
# print(len(age))

# password="devopsoss"
# # print(len(password))

# if len(password) > 8:
#     print("Password accepted")
# elif len(password) == 8:
#     print("Password ok")    
# else:    
#     print("minimum password length should be 8 characters")
    
    
# for s in range(7):
#     print(s)   

# for i, ages in enumerate(age):
#     if ages < 18:
#         print("Student at #", i+1, "with age:", ages, "is minor")

# for i in range(len(age)):
#     print(age[i])
    
    
count = 0

# while count <= 5:
#     print(count)
#     count += 1

# status=200

# match status:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not found")
#     case _:
#         print("Unknown")


# students= "Hello DevOps"
# string="Hello world, I am learning DevOps.For automations,DevOps is BEST"
# print(re.match(r"DevOps", students)) //
# print(re.findall(r"DevOps", string))

# some = "Error: 404"

# print(re.sub(r"404", "Not Found", some))

# other = "apple,banana,orange,grape"
# print(re.split(r"[; ,]", other))

# hobbies="Coding Study Automation Gym Exercise"
# print(re.split(r"[; ,]", hobbies   ))

# print("hello\nworld")
# print("hello\devops")

# email="mail.sulemanahmed009@gmail.com"
# emailpattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
# print(re.match(emailpattern, email))

# ipAddress = "192.168.18.10"
# ipPattern = r"\d+\.\d+\.\d+\.\d+"
# print(re.match(ipPattern, ipAddress))

# \d = digit (0-9)
# \D = Non-Digit 
# \w = Word character 
# \W = Non-Word 
# \s = whitespace
# \S = Non-Whitespace
# ^ to start string 
# $ to end string