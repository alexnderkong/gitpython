import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  0   |
      |
      |
     ===''', '''
  +---+
  0   |
  |   |
      |
     ===''', '''
  +---+
  0   |
 /|   |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
 /    |
     ===''', '''
  +---+
  0   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [0   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [0]   |
 /|\  |
 / \  |
     ===''']

words = {'Colours': 'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron \
pentagon hexagon septagon octagon'.split(),
         'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana \
cantaloupe mango strawberry tomato'.split(),
         'Animals': 'ant badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog \
donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose \
mouse mule newt otter owl panda parrot pigeon python rabbit ram rat rhino salmon seal \
shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel \
whale wolf wombat zebra'.split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0,len(wordDict[wordKey])-1)
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed letters:", end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        guess = str(input("Guess a letter: "))
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter!")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a LETTER!")
        else:
            return guess

def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

print("H A N G M A N")

difficulty = ' '
while difficulty not in 'EMH':
    difficulty = str(input("Enter difficulty: E - Easy, M - Medium, H - Hard: "))
    difficulty = difficulty.upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

    
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print ('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes! The secret word is '" + secretWord + "'! You have won!")
            gameIsDone = True
    else:
        missedLetters += guess

        if len(missedLetters) == len(HANGMAN_PICS)-1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print("You have run out of guesses!\nAfter " + str(len(missedLetters)) + \
                  " missed guesses and " + str(len(correctLetters)) + " correct guesses, " \
                  + "the word was '" + secretWord + "'")
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break