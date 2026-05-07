# name = "suleman ahmed"
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
#     # sys.exit() >> it will complete stop the file
    
# print("hello world")

totalStudent = 75
attendance=[
    {
        "Date":"20260421",
        "present":48
    },
       {
        "Date":"20260422",
        "present":50
    }
]

for atd in attendance:
    percentage = (atd["present"] / totalStudent) * 100
    # print("percentage of students present on", atd["Date"], "is", percentage, "%")
    print(f"percentage of students present on {atd['Date']} is {percentage}%")