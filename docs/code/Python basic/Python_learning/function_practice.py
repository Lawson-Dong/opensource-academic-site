# function_practice




#input the data of the function
username = input(f"Please enter your name: ")


#define a function
def greet_user(username):
    """show a simple greeting"""
    print(f"Hello, {username.title()}!")


greet_user(username)  #call a function
