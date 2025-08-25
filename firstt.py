# Create a list of your 5 favourite fruits and print it.Print the first and last elements of the list.Change the second item in the list to "Mango".Insert: Add "Watermelon" at index 2.Check existence: Write a program that asks the user for a fruit name and checks if it’s in the list.Sort the list alphabetically.
list = ["appel","manga","banana","orange","freez"]
print(list)
print(list[0])
print(list[4])
list[1] = "mango"
print(list)
list.insert(2,"watremellon")
print(list)
frute = input("enter your frute name :\n")
if frute in list:
    print(f" {frute:} exist")
else:
    print(f"{frute} not exist")
list.sort()
print(list)

