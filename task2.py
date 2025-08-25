
name =input("enter username: ") 
password =input ("enter pass: ") # Ask the user to enter a username and a password.
print(name.lower()) 
name = "_".join(name.split())
print(name)
password=len(password)


is_password_long = len(password) >= 8
is_name_admin = name == "admin"
is_password_default = password == "1234"
is_default_account = is_name_admin and is_password_default


print("Password length >= 8:", is_password_long)
print("Username is 'admin':", is_name_admin)
print("Password is '1234':", is_password_default)
print("Default account:", is_default_account)

print(f"Welcome, {name}! Your password length is {len(password)}.")
