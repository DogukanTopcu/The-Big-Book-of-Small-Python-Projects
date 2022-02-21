"""
The Birthday Paradox, also called the 
Birthday Problem, is the surprisingly high 
probability that two people will have the 
same birthday even in a small group of people. 
In a group of 70 people, there’s a 99.9 percent chance 
of two people having a matching birthday. But even 
in a group as small as 23 people, there’s a 50 percent 
chance of a matching birthday. This program performs several probability 
experiments to determine the percentages for groups of different sizes. 
We call these types of experiments, in which we conduct multiple random 
trials to understand the likely outcomes, Monte Carlo experiments.

You can find out more about the Birthday Paradox at 
https://en.wikipedia.org/wiki/Birthday_problem.

"""

from dataclasses import dataclass
import datetime, random
import re

from urllib3 import Retry

def getBirthday(numberOfBirthdays):
    # Returns a list of a number randım date objects for birthdays.
    birthdays = []

    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumbersOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumbersOfDays
        birthdays.append(birthday)
    
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None 
        # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA
                # Return the matching birthday.


# Display the intro
print("""
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
""")


# Set up a tuple of month names in order:
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

while True:
    print("How many birthday shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()


# Generate and display the birthdays:
print("Here are", numBDays, "birthdays:")
birthdays = getBirthday(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(", ", end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = "{} {}".format(monthName, birthday.day)
        print(dateText, end='')
print()
print()


# Determine if there are two birthdays that match.
match = getMatch(birthdays)


# Display the result:
print("In this simulation, ", end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = "{} {}".format(monthName, match.day)
    print("Multiple people have a birthday on", dateText)
else:
    print("there are no matching birthdays.")
print()






# Run through 100,000 simulations:

print("Generating", numBDays, "random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let's run another 100,000 simulations")

simMatch = 0 # How many simulations had matching birthdays in them.

for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthday(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
    
print("100,000 simulations run.")



# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print("Out of 100,000 simulations of", numBDays, "people, there was a")
print("matching birthday in that group", simMatch, "times. This means")
print("that", numBDays, "people have a", probability, "% chance of")
print("having a match birthday in their group.")
print("That's probably more than would think!")




"""
IMPORTANT FUNCTIONS ON THIS SESSION:

enumerate()
"""


"""
NOTES:

100_000 = 100000
    These are same
"""