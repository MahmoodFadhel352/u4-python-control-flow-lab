# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()
#Exercise 1
def check_letter():
    # user input
    letter = input("Enter a single letter (a-z or A-Z): ")

    # Validate input
    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter exactly one alphabetical character.")
        return

    # Define vowels
    vowels = "aeiouAEIOU"

    # Check if the letter is a vowel or consonant
    if letter in vowels:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")


# Call the function
check_letter()
#Exercise 2
def check_voting_eligibility():
        # Prompt user for input
        age = int(input("Please enter your age: "))

        # Validate input
        if age < 0:
            print("Invalid age. Age cannot be negative.")
            return

        # Define voting age
        voting_age = 18

        # Check eligibility
        if age >= voting_age:
            print(f"You are {age} years old and eligible to vote.")
        else:
            print(f"You are {age} years old and not eligible to vote yet.")

# Call the function
check_voting_eligibility()
#Exercise 3
def calculate_dog_years():
        # Prompt user for input
        age = int(input("Input a dog's age: "))

        # Validate input
        if age < 0:
            print("Invalid age. Age cannot be negative.")
            return

        # Calculate dog years
        if age <= 2:
            dog_years = age * 10
        else:
            dog_years = (2 * 10) + ((age - 2) * 7)

        # Print result
        print(f"The dog's age in dog years is {dog_years}.")
# Call the function
calculate_dog_years()
#Exercise 4
def weather_advice():
    # Ask user about weather
    cold = input("Is it cold? (yes/no): ").lower()
    raining = input("Is it raining? (yes/no): ").lower()
    # Decision logic
    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")
# Call the function
weather_advice()
#Exercise 5
def determine_season():
    # Map months to numeric values for easier comparisons
    months = {
        "Jan": 1, "Feb": 2, "Mar": 3,
        "Apr": 4, "May": 5, "Jun": 6,
        "Jul": 7, "Aug": 8, "Sep": 9,
        "Oct": 10, "Nov": 11, "Dec": 12
    }

    # Prompt for month
    month_str = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()

    if month_str not in months:
        print("Invalid month. Please enter a valid three-letter abbreviation (e.g., Jan, Feb, Mar).")
        return

    # Prompt for day
    day = int(input("Enter the day of the month: ").strip())
    

    month = months[month_str]

    # Basic validation
    if day < 1 or day > 31:
        print("Invalid day. Please enter a value between 1 and 31.")
        return

    # Determine season
    if (month == 12 and day >= 21) or (month in [1, 2]) or (month == 3 and day <= 19):
        season = "Winter"
    elif (month == 3 and day >= 20) or (month in [4, 5]) or (month == 6 and day <= 20):
        season = "Spring"
    elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day <= 21):
        season = "Summer"
    elif (month == 9 and day >= 22) or (month in [10, 11]) or (month == 12 and day <= 20):
        season = "Fall"
    else:
        season = "Unknown"  # Fallback

    # Print result
    print(f"{month_str} {day} is in {season}.")


# Call the function
determine_season()
#Exercise 6
def guess_number():
    target = 42  # fixed number to guess
    attempts = 5  # max attempts
    low, high = 1, 100  # guessing range

    print(f"Guess the number between {low} and {high}. You have {attempts} attempts!")

    for i in range(1, attempts + 1):
        guess = int(input(f"Attempt {i}: Enter your guess: "))

        # Check correct guess
        if guess == target:
            print("Congratulations, you guessed correctly!")
            return

        # Give hints
        if guess < target and guess >= low:
            print("Your guess is too low.")
        elif guess > target and guess <= high:
            print("Your guess is too high.")
        else:
            print(f"Your guess is not in the valid range ({low}-{high}).")

        # Last chance warning
        if i == attempts - 1:
            print("Last chance!")

    # If loop completes without correct guess
    print("Sorry, you failed to guess the number in five attempts.")


# Call the function
guess_number()
