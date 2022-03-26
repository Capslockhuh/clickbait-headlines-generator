# clickbait_headline_generator.py - generates random clickbait headlines

import random

# Data
objectPronouns = ['Her', 'Him', 'Them']
possesivePronouns = ['Her', 'His', 'Their']
personalPronouns = ['She', 'He', 'They']
states = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
nouns = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent', 'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado', 'Plastic Straw','Serial Killer', 'Telephone Psychic']
places = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement', 'Workplace', 'Donut Shop', 'Apocalypse Bunker']
when =  ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

# Headlines
def isGenZKillingHeadline():
    noun = random.choice(nouns)
    return 'Is gen Z killing the {} industry?'.format(noun)

def whatYouDontKnowHeadline():
    noun = random.choice(nouns)
    plurarNoun = random.choice(nouns)
    time = random.choice(when)
    return 'Without this {}, {} could kill you {}'.format(noun, plurarNoun, time)

def bigCompaniesHateHeadline():
    pronoun = random.choice(objectPronouns)
    state = random.choice(states)
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    return 'Big companies hate {}! See how this {} {} invented a cheaper {}'.format(pronoun, state, noun1, noun2)

def youWontBelieveWhatWasFound():
    state = random.choice(states)
    noun = random.choice(nouns)
    pronoun = random.choice(possesivePronouns)
    place = random.choice(places)
    return 'You won\'t believe what this {} {} found in {} {}'.format(state, noun, pronoun, place)

def dontWontYouToKnow():
    pluralNoun1 = random.choice(nouns) + 's'
    pluralNoun2 = random.choice(nouns) + 's'
    return 'What {} don\'t want you to know about {}'.format(pluralNoun1, pluralNoun2)

def giftHeadline():
    number = random.randint(7, 15)
    noun = random.choice(nouns)
    state = random.choice(states)
    return '{} gift ideas to give your {} from {}'.format(number, noun, state)

def reasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(nouns) + 's'
    number2 = random.randint(1, number1)
    return '{} Reasons why {} are more interesting than you think (number {} will suprise you!)'.format(number1, pluralNoun, number2)

def jobAutomatedHeadline():
    state = random.choice(states)
    noun = random.choice(nouns)
    i = random.randint(0, 2)
    pronoun1 = possesivePronouns[i]
    pronoun2 = personalPronouns[i]
    if pronoun1 == 'Their':
        return 'This {} {} didn\'t think robots would take {} job. {} were wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} didn\'t think robots would take {} job. {} was wrong.'.format(state, noun, pronoun1, pronoun2)


# Main
print('Clickbait headline generator')
while True:
    print('Enter the number of clickbait headlines to generate:')
    response = input()
    if not response.isdecimal():
        print('Please enter a number.')
    else:
        numberOfHeadlines = int(response)
        break

# Select the headline
for i in range(numberOfHeadlines):
    clickbaitType = random.randint(1, 8)

    if clickbaitType == 1:
        headline = isGenZKillingHeadline()
    elif clickbaitType == 2:
        headline = whatYouDontKnowHeadline()
    elif clickbaitType == 3:
        headline = bigCompaniesHateHeadline()
    elif clickbaitType == 4:
        headline = youWontBelieveWhatWasFound()
    elif clickbaitType == 5:
        headline = dontWontYouToKnow()
    elif clickbaitType == 6:
        headline = giftHeadline()
    elif clickbaitType == 7:
        headline = reasonsWhyHeadline()
    elif clickbaitType == 8:
        headline = jobAutomatedHeadline()
    print(headline)