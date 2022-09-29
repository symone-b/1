from random import sample, shuffle

digits = 3
guesses = 10

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
    Pico       One digit is correct but in the wrong position.
    Fermi      One digit is correct and in the right position.
    Bagels     No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.''')        

# Create a random number.

letters = sample('0123456789', digits)

if letters[0] == '0':
    letters.reverse()

number = ''.join(letters)

print('I have thought up a number.')
print('You have', guesses, 'guesses to get it.')

counter = 1

while True:
    print('Guess #', counter)
    guess = input()

    if len(guess) != digits:
        print('Wrong number of digits. Try again!')
        continue

    # Create the clues.

    clues = []

    for index in range(digits):
        if guess[index] == number[index]:
            clues.append('Fermi')
        elif guess[index] in number:
            clues.append('Pico')

    shuffle(clues)

    if len(clues) == 0:
        print('Bagels')
    else:
        print(' '.join(clues))

    counter += 1

    if guess == number:
        print('You got it!')
        break

    if counter > guesses:
        print('You ran out of guesses. The answer was', number)
        break
