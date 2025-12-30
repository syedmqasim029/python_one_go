# # class Student:
# #     def __init__(this,name,marks): # this is the reference variablle pointing to the current obj
# #         # but generally we use self but we can write any valid name here
# #         this.name = name 
# #         this.marks = marks

# # qasim = Student("Qasim",93)
# # print(qasim) # Reference variable to the obj
# # print(qasim.name,qasim.marks) # Attributes



# # class Student:
# #     name = "Qasim" # Attributes
# #     def __init__(self,name,rollNo):
# #         self.name = name
# #         self.rollNo = rollNo
# #     def setNameMarks(self,rollNo,name):
# #         self.name = name
# #         self.rollNo = rollNo
# #     # def getRollNo(self):
# #     #     return self.rollNo
# #     # def getName(self):
# #     #     return self.name
# # a = Student("Abdullah",29)
# # #print(a.name," ",Student.name) # obj precedence > class precedence
# # a.setNameMarks(name="Ali",rollNo=55)
# # print(a.name,a.rollNo)
        

# class Student:
#     name = "Anonymous"
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def avgCalculate(self):
#         return sum(self.marks)/len(self.marks)
#     @staticmethod              # decurator
#     def welcome():
#         print(f"Hello Students!")
# q  = Student("Qasim",[99,100,98])
# print(f"Your average marks are : {q.avgCalculate()}")
# Student.welcome()
# q.welcome()


# class Restaurant:
#     def __init__(self,restaurantName,cuisineType):
#         self.restaurantName = restaurantName
#         self.cuisineType = cuisineType
#     def describeRestaurant(self):
#         print(self.restaurantName," ",self.cuisineType)
#     def openRestaurant(self):
#         print(f"{self.restaurantName} is now open!")   

# restaurant = Restaurant("Royal","ABC")
# restaurant.describeRestaurant()
# restaurant.openRestaurant() 
# a = Restaurant("A","A")
# b = Restaurant("B","B")
# c = Restaurant("C","C")
# a.describeRestaurant()
# b.describeRestaurant()
# c.describeRestaurant()

