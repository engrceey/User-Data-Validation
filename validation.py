# User Data Validation Program
import string
import random

# Container for storing User Details
users = {}

# Main Program: Using a while loop to keep adding users till stopped

while True:
    # Getting user details
    firstName = str(input("Please Enter First name: "))
    lastName = str(input("Please Enter Last name: "))
    email = str(input("Please Enter Email: "))

    # A function to generate Random String of length 5
    def randomLetter(length = 5):
        letters = string.ascii_lowercase
        randomString = "".join(random.choice(letters) for i in range(length))
        return randomString

    # A Function to create the System Password
    def sysPassword():
        password = firstName[0:2] + randomLetter() + lastName[-2:]
        return password

    # Asking user for preferred password
    preference = input("Do you prefer this password: '{}' : Yes/No? ".format(sysPassword()))

    # A function to determine User Password Preference
    def passwordPreference():
        if preference.lower() == "yes":
            return  sysPassword()
        elif preference.lower() == "no":
            while True:
                userPassword = input("Enter preferred Password minimum 7 characters : ")
                if len(userPassword) >= 7:
                    return userPassword
                    break

    # An Array for gathering individual details
    userArray = [firstName,lastName,email,passwordPreference()]

    # Adding Users Array to the User Dictionary using firsname as key
    users[userArray[0]] = userArray

    # An if statement to add a New User or Break and print Users
    addAnotherUser = str(input("Would you like to add another user, Yes/No? : "))
    if addAnotherUser.lower() == "yes":
        continue
    elif addAnotherUser.lower() == "no":
        break

for key, value in users.items():
    print("First Name: %s, Last Name: %s, Email: %s, Password: %s" % (value[0],value[1],value[2],value[3]))


