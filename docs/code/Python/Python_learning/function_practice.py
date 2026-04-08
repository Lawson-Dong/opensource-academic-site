# function_practice




#8.1 Define a function
#username = input(f"Please enter your name: ") #input data 

#def greet_user(username):
#    """show a simple greeting"""
#    print(f"Hello, {username.title()}!")

#greet_user(username)  #call a function


#8.2 Actual parameter and formal parameter
#animal_type = input(f"Please enter the type of animal: ")
#pet_name = input(f"Please enter the name of the pet: ")

#def describe_pet(animal_type, pet_name):
#    """display information about a pet"""
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet(animal_type, pet_name)

#animal_type and pet_name are formal parameters, which are the variables that receive the values when the function is called.
#the values you input are actual parameters, which are the values that you pass to a function when you call it.

##8.2.1 Positional arguments 

#def describe_pet(animal_type, pet_name):
#    """showcase the information of the pet"""
#    print("\nI have a " + animal_type + "'s name is " + pet_name.title() + ".")
    
#describe_pet("hamster", "harry")

#hamster and harry are positional arguments
#The order of the positional arguments have to match the order of formal parameter
""" actual parameter 
├── positional argument 
└── keyword argument """

##8.2.2 Keyword arguments

#def describe_pet(animal_type, pet_name):
#    """showcase the information of the pet"""
#    print("\nI have a " + animal_type + "'s name is " + pet_name.title() + ".")
    
#describe_pet(animal_type = "hamster" , pet_name = "harry")

#The datatype of the keyword argument is key-value pair
#e.g. animal_type = "hamster", this is a key-value pair

##8.2.3 default value

#def describe_pet(pet_name = 'harry', animal_type):
#    """showcase the information of the pet"""
#    print("\nI have a " + animal_type + "'s name is " + pet_name.title() + ".")
#def describe_pet(animal_type, pet_name = 'harry'):
#    """showcase the information of the pet"""
#    print("\nI have a " + animal_type + "'s name is " + pet_name.title() + ".")
    
#describe_pet(animal_type = "hamster")
#describe_pet("hamster")

#So if we don't use keyword argument, python will automatically sense the actual argument as position argument 
#Believe it or not, you can check it using the two functions upwards
#The order of keyword argument doesn't affect the output, but the order of the position argument can affect the output

##8.2.4 common error
#def describe_pet(animal_type, pet_name):
    #"""showcase the information of the pet"""
    #print("\nI have a " + animal_type + "'s name is " + pet_name.title() + ".")
    
#describe_pet()
#describe_pet(animal_type = "dog")
#describe_pet("Bobby","dog")

#We are not going to pass any information to the formal argument
#There is an error

#8.3 return
# y = f(x), the effect of "return" is to return the outcome of execution back to the function itself

##8.3.1 return simple value

#first_name = input(f"please input your first name: ")
#last_name = input(f"please input your last name: ")

#first_name, last_name = input(f"please input your first name: "), input(f"please input your last name: ")

#def get_formatted_name(first_name, last_name):
#    """return name"""
#    return print(f'My name is {first_name.title()} {last_name.title()}')

#get_formatted_name("Lawson", "Dong")
#get_formatted_name(first_name, last_name)

##8.3.2 let actual argument become optional
#first_name, middle_name, last_name = input(f"please input your first name: "), input(f"please input your middle name: "), input(f"please input your last name: ")

#def get_formatted_name(first_name, middle_name, last_name):
#    """return name with optional middle name"""
#    if middle_name:
#        full_name =  f'My name is {first_name.title()} {middle_name.title()} {last_name.title()}'
#    else:
#        full_name = f'My name is {first_name.title()} {last_name.title()}'
#    return print(full_name.title())
       
#get_formatted_name(first_name, middle_name, last_name)

##8.3.3 return dictionary
#first_name, last_name = input(f"please input your first name: "), input(f"please input your last name: ")

#def get_formatted_name(first_name, last_name):
#    """return a dictionary which containing the information of one's name"""
#    person_name = {"first": first_name.title(), "last": last_name.title()}
#    return person_name 

#personal_information = get_formatted_name(first_name, last_name)

#print(personal_information)
#print(type(personal_information))

#Using properties of the dictionary

#first_name, last_name, age = input(f"please input your first name: "), input(f"please input your last name: "), input(f"please input your age: ")
#def get_formatted_name(first_name, last_name, age = ""):
#    """return a dictionary with the age information of a person"""
#    person = {"first" : first_name, "last" : last_name}
#    if age:
#        person['age'] = age
#    return person

#personal_information = get_formatted_name(first_name, last_name, age)
#print(personal_information)

##8.3.4 combining function and while loop



#def get_formatted_name(first_name, last_name):
#    """return a full name, neatly formatted"""
#    full_name = f"{first_name} {last_name}"
#    return print(full_name.title())

#while True:
#    print("\nPlease tell me your name: ")
#    print("Enter 'q' at any time to quit.")
    
#    f_name = input("First name: ")
#    if f_name == 'q':
#        print("You quit to input your name.")
#        break
#    l_name = input("Last name: ")
#    if l_name == 'q':
#        print("You quit to input your name.")
#        break
        
    
#    get_formatted_name(f_name, l_name)
    
    
   
#8.4 pass the list to a function


usernames = [input(f"Please enter the name of user {i+1}: ") for i in range(3)]

def greet_users(names):
    """greet each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

greet_users(usernames)


