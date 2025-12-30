'''The following exercises are a bit more complex than those in Chapter 2, but
they give you an opportunity to use lists in all of the ways described.
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still
in your list.
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list.
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
•	 Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
•	 Print a message to each of the two people still on your list, letting them
know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
'''







GuestList = []

GuestList.append("Abdullah")
GuestList.append("Rehman")
GuestList.append("Shahji")

print("Initial Invitations:")
print(f"{GuestList[0]}, you are invited to dinner.")
print(f"{GuestList[1]}, you are invited to dinner.")
print(f"{GuestList[2]}, you are invited to dinner.")

print("\nUnfortunately Shahji can't make it to the dinner.\n")

GuestList[2] = "Ahmed"

print("Updated Invitations:")
print(f"{GuestList[0]}, you are invited to dinner.")
print(f"{GuestList[1]}, you are invited to dinner.")
print(f"{GuestList[2]}, you are invited to dinner.")


print("\nGood news! I found a bigger dinner table.\n")

GuestList.insert(0, "Ali")                      
GuestList.insert(len(GuestList)//2, "Umer")     
GuestList.append("Hamza")                       

print("New Invitations:")
for guest in GuestList:
    print(f"{guest}, you are invited to dinner.")

print("\nSorry, I can invite only two people for dinner.\n")

while len(GuestList) > 2:
    removed_guest = GuestList.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print("\nStill Invited Guests:")
for guest in GuestList:
    print(f"{guest}, you are still invited to dinner.")


del GuestList[0]
del GuestList[0]

print("\nFinal Guest List:", GuestList)
