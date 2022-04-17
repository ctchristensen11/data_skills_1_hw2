# PPHA 30535
# Spring 2022
# Homework 2

# CTCHRISTENSEN
# CTCHRISTENSEN11

# Due date: Sunday April 17th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]

def func_e(num1, num2):
    value = (num1 + num2)
    if value > 10:
        return 'big'
    elif value == 10:
        return 'just right'
    elif value < 10:
        return 'small'
    else:
        result = value


size_matters = [func_e(i[1], i[0]) for i in start_list]


print(size_matters)


# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

def my_func(a=10):
    b = 30
    return a + b


x = my_func()

print(x)

# Global are accessible throughout entire program. Local are accessible only
# within the function. Editing global will change func result. inconsistency=bad

# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.
#import random
#from numpy import random
  
import random
import string


def get_random_password(length, special_chars=True ):
    if length < 8 or length > 16:
        return "Not a good length"
    else:
        if special_chars == True:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
        else:
            characters = string.ascii_letters + string.digits
            password = ''.join(random.choice(characters) for i in range(length))
    return password
 
get_random_password()   



# https://www.geeksforgeeks.org/ython-select-random-value-from-a-list/
#https://pynative.com/python-generate-random-string/
  
# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 1, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes any number of these instances and 
# returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])

class COVIDData():
    def __get_record__():
        pass
    def 

class HouseValues():
    def __init__(self, num_bedrooms, num_baths, sqft):
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths
        self.sqft = sqft
    
    def pick_a_neighborhood(self):
        value = random.normal(1, 0.1)
        if value > 1.2:
            print('Whoa, you got an expensive neighborhood!')
        elif value > 1:
            print('Fairly pricy neighborhood.')
        elif value < 1:
            print('Maybe not the nicest neighborhood.')
        return value
        
    def estimate_value(self):
        #add 10% per num of bedrooms over 1
        bedroom_mod = ((self.num_bedrooms - 1) * 0.1) + 1
        
        #add 5% per num of baths over 1
        bath_mod = ((self.num_baths - 1) * 0.05) + 1
        
        n_mod = self.pick_a_neighborhood()
        
        self.value = (self.sqft * 400) * bedroom_mod * bath_mod * n_mod
        print(f'I estimate this house will be worth ${round(self.value, 2)}')
        
house1 = HouseValues(2, 2, 950)
house2 = HouseValues(1, 1, 700)
house1.estimate_value()
house2.estimate_value()