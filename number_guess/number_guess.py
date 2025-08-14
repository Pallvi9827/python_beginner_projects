import random        # we need to pick a random number

# Step 1: show a welcome messgae
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 100.")

# Step 2: generate a random number
secret_number = random.randint(1, 100)
# Step 3: initialize the number of attempts
attempts = 0 
# Step 4: start the guessing loop
while True:
    # Step 5: get user input
    guess = int(input("Please enter your guess: "))
    attempts += 1  # increment the number of attempts

    # Step 6: check if the guess is correct
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
        break  # exit the loop if the guess is correct