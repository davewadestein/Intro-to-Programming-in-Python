# above we have written Python to generate the 4-digit code
# let's try putting the code we wrote into a function...

import random # to generate the secret code
import sys # to allow us to call exit()

def user_digits():
    digits = input('How many digits do you want to play with (4)? ')
    if not digits: # container is empty
        digits = 4
    else:
        digits = int(digits)
        
    return digits
    
    
def generate_code(num_digits):
    code = []
    
    # generate the code
    digits = list(range(10)) # 0..9

    #. do this once for each digit 
    #.       randomenerate a digit
    #.       add it to our code
    #.       remove it from the digits we can choose from
    for times in range(num_digits):
        digit = random.choice(digits)
        digits.remove(digit)
        code.append(str(digit))
        
    return code


def get_valid_user_guess(num_digits):
    # get a guess from user
    # ensure
    # 1. length of guess is correct
    # 2. guess is all digits
    # 3. no duplicate digits
    #
    # let them type 'quit' to stop
    
    # until the user has guessed a valid guess or said 'quit':
    #.   keep asking for a guess
    # (while ...)
    
    # validating the guess
    # 1. if length of guess is not num_digits, then BAD
    # 2. if any element of the string is not a digit, then BAD
    # 3. if any digit appears more than once, then BAD
    
    while True: # "placeholder" infinite loop
        guess = input('Enter your guess: ')
        if guess == 'quit':
            sys.exit(0) # leave the program immediately
            
        # validation step 1
        if len(guess) != num_digits:
            print('Your guess should be', num_digits, 'digits long!')
            continue
            
        # validation step 2
        if not guess.isdigit():
            print('Your guess should be ONLY digits!')
            continue
            
        # validation step 3
        # for each digit in the guess
        #.  if the number of times that digit appears in guess is > 1, then BAD        
        for digit in guess:
            if guess.count(digit) > 1:
                break
        else: # we did not break, i.e., we finished the loop normally
            # no repeating numbers
            return guess
        
        print('Your guess has more than one', digit)
        
num_digits = user_digits() # ask the user how many digits to play with?
secret_code = generate_code(num_digits) # generate the secret code
print('secret code is', secret_code)
guess = get_valid_user_guess(num_digits)
# if we're here, we have a valid guess
#print(number_of_bulls(), 'bulls')
#print(number_of_cows(), 'cows')
