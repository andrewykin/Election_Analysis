# print("Hello World")

#3.2.8 Decision Statements
counties = ["Arapahoe","Denver","Jefferson"]

if counties[3] != 'Jefferson':
    print(counties[2])

if counties[1] == 'Denver':

   print(counties[1])



 #if-else
temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#3.2.9
#Membership Operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


#Logical Operators
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


#Logical Operators "or"
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


#Practice
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")


#3.2.10
#Iterate through Lists & Tuples
counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)

counties = ["Arapahoe","Denver","Jefferson"]
for i in range(len(counties)):
    print(counties[i])


numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

#PRACTICE
counties_tuples = ["Arapahoe","Denver","Jefferson"]
for i in range(len(counties_tuples)):
    print(counties_tuples[i])
#correct output

counties_tuples = ["Arapahoe","Denver","Jefferson"]
for i in len(counties_tuples):
    print(counties_tuples[i])
#for i in len(counties_tuples): --> TypeError: 'int' object is not iterable

counties_tuples = ["Arapahoe","Denver","Jefferson"]
for county in counties_tuples:
    print(county)
#correct output

counties_tuples = ["Arapahoe","Denver","Jefferson"]
for county in counties_tuples:
    print(counties)
#print(counties) --> NameError: name 'counties' is not defined

#ITERATE THROUGH A DICTIONARY
#Get the Keys of a Dictionary - using a for loop
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
#Keys method to get Keys
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)

#Get the Values of a Dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for voters in counties_dict.values():
    print(voters)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict[county])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict.get(county))

#Get the Key-Value Pairs of a Dictionary
#items method in for loop
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county, voters)

#Skill Drill
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#Get each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#PRACTICE - How would you use the range() function to iterate over the list of dictionaries & print the counties in voting_data?
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(counties_dict)):
    print(counties_dict[i])
#NameError: name 'counties_dict' is not defined

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in len(voting_data):
    print(voting_data[i])
#TypeError: 'int' object is not iterable

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    print(voting_data[i]['county'])
#CORRECT OUTPUT

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county in range(len(voting_data)):
    print(county)
#Prints 0, 1, 2

#Get the Values from a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#PRACTICE - How would you retrieve the number of registered voters from each dictionary?
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict.values())
#almost right OUTPUT --> dict_values(['Arapahoe', 422829])... prints every value from dictionary as a list, 
#need to add print(county_dict[registered_voters']) as the statement under the for loop

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict:
        print(value)
#INCORRECT OUTPUT --> county registered_voters

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict['registered_voters'])
#CORRECT OUTPUT

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for key, value in county_dict.items():
        print(value)
#not quite --> prints each county & registered voter #

#If we only want to print the county name from each dictionary, we can use county_dict['county'] in the print statement for the for loop.
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict['county'])

#Repetition Statements
#While Loop
x = 0
while x <= 5:
    print(x)
    x = x + 1


#While Loop Practice 
count = 7

while count < 1:

    print("Hello World")
#nothing printed b/c condition is false on the first test

#Nested If Else Practice
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')




# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')



#3.4.1 Dependencies - datetime
#get today's date
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

#updated code for today's date 
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# 3.4.3
#Direct Load CSV
# Assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)


#Indirect Load CSV
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)




