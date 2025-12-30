# import this
# import qasim

'''Just Recalling list'''
cars = ["Mehran","Bugati","lamborgini","Civic"]
print(f"Expensive cars are {cars[1]} and {cars[2]} ")
print(f"Pakistani cars are {cars[0]} and {cars[-1]} ")

# it changes 'Mehran' to 'Yamaha'
cars[0] = "Yamaha"
print(cars)

# if.we want to add string in the list so we use 'append' function
cars.append('Mehran')
print(cars)
# append method append value at the las tof the list 

# if we want to add a string to a particular position we use insert method
'''Insert'''
cars.insert(0,'Mehran')
print(cars)
# Now our list contanis same as we wanted 
# But now we have mehran two times in the list we dont wanted the last one 
'''Del'''
# TO delete that we use 'del' but 'del' keyword don't return our deleted value
del cars[-1]
print(cars)
# TO return the deleted item you must use pop method
print(cars.pop())
print(cars)

# Remove item using giving value
cars.remove("Bugati")
print(cars)

