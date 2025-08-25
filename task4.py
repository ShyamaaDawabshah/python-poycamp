#  Create a program that stores fruit prices in a dictionary and lets the user enter a fruit name. 
# 2. If the fruit exists in the dictionary, print its price. 
# 3. If the fruit doesn’t exist, print "Sorry, this fruit is
# not availab
dic ={
"bannana" : 30,
"mango" : 40,
"appel":90
}
x = dic["mango"]
print(x)
fruit_name=input("enter the fruit name: ")
if fruit_name in dic :
    price = dic[fruit_name.lower()]
    print (f"{fruit_name} price = {price}")
else :
    print(f"{fruit_name} not avilbel")    
