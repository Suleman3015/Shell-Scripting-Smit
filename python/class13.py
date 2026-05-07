from datetime import date, datetime
import math 


courseName = "DevOpsTTS2123"
classDuration = 120
classLength = 0.75
classActive = True


classStart = datetime(2026, 3, 24)
today = datetime.today()
# .strftime("%d-%m-%y")

diff = today - classStart
daysCompleted = diff.days
# weeksCompleted = daysCompleted // 7 # // 
weeksCompleted = round(daysCompleted / 7)
# print("classStart:", classStart)
# print("today:", today)
# print("diff:", diff.days)
# print("daysCompleted:", daysCompleted)
# print("weeksCompleted:", weeksCompleted)

# print(type(courseName))
# print(type(classDuration))
# print(type(classLength))
# print(type(classActive))


# print(date.today())


topics = ["OS", "OS", "Linux", "Linux", "Monitoring"]
# for index,topic in enumerate(topics):
#     print("Week",index+1,":",topic)
    
for index in topics:
    # print("Week",topics.index(index)+1,":",index)
    print(index)