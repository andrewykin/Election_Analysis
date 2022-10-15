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

