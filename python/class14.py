# Complex
# x = 1 + 2j
# print(x)
# print(type(x))

# classTopics=[
#     "Operating System",
#     "Operating System",
#     "Operating System",
#     ]

# classTuple=(
#     "Operating System",
#     "Operating System",
#     "Operating System",
#     )

# list = []
# tuple = ()

# print(type(classTopics))
# print(type(classTuple))
# print(list)
# print(tuple)

# list.append("Hello")
# print(list)
# tuple.append("Hello")
# print(tuple)


# class1 = ["Operating System", "Data Structure", "Python"]

# classex = ["260324", "21;00-23;00", "70", "Lab"]

# date:
# Time
# Date
# Presents
# Labs

# class1 = {
#     "date": "260324",
#     "time": "21;00-23;00",
#     "presents": 70,
#     "labs": "Lab1"
# }


# print(class1["date"])
# print(class1.get("date"))



# classDict = [
#     {
#         "Name": "Operating System",
#         "Topics": ["Process Management", "Memory Management", "File System"],
#         "Status": True
#     },
#     {
#         "Name": "Data Structure",
#         "Topics": ["Arrays", "Linked Lists", "Trees"],
#         "Status": True
#     },
#     {
#         "Name": "Python",
#         "Topics": ["Syntax", "Data Types", "Functions"],
#         "Status": True
#     },
#     {
#         "Name": "Database",
#         "Topics": ["SQL", "NoSQL", "Database Design"],
#         "Status": False
#     },
#     {
#         "Name": "Computer Networks",
#         "Topics": ["TCP/IP", "HTTP", "Network Security"],
#         "Status": False
#     }
# ]


accessLevel = {"Admin", "Trainer", "Student", "Student"}
print(type(accessLevel))
# print(accessLevel)

# frozenAccessLevel = frozenset({"Admin", "Trainer", "Student", "Student"})
# print(type(frozenAccessLevel))
# print(frozenAccessLevel)

# data= b"Hello"
# data= bytearray(b"Hello")

# print(type(data))
# print(data[0])

# data = b"Hello World"
# print(type(data))
# print(data)


# mv = memoryview(b'DevOps')

# print(type(mv))
# print(mv[0])


marks = [10,20,30,40,50,5]

# lastmark = marks[0]

# for mark in marks:
#     if mark <= lastmark:
#         lastmark = mark

def mini(list):
    minimum = list[0]
    
    for number in list:
           if number <= minimum:
            minimum = number
    return minimum

# print("Lowest mark is:", mini(marks))

print(mini(marks))