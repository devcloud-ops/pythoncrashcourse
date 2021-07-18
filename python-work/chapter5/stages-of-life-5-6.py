# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
# i) If the person is less than 2 years old, print a message that the person is
# a baby.
# ii) If the person is at least 2 years old but less than 4, print a message 
# that the person is a toddler.
# iii) If the person is at least 4 years old but less than 13, print a message 
# that the person is a kid.
# iv) If the person is at least 13 years old but less than 20, print a message 
# that the person is a teenager.
# v) If the person is at least 20 years old but less than 65, print a message 
# that the person is an adult.
# vi) If the person is age 65 or older, print a message that the person is an
# elder.

# version i - baby
# age = 1

# version ii - toddler
# age = 3

# version iii - kid
# age = 10

# version iv - teenager
# age = 15

# version v - adult
# age = 40

# version vi - elder
age = 67

if (age < 2):
    human_classification = 'baby'
elif (age >= 2 and age < 4):
    human_classification = 'toddler'
elif (age >= 4 and age < 13):
    human_classification = 'kid'
elif (age >= 13 and age < 20):
    human_classification = 'teenager'
elif (age >= 20 and age < 65):
    human_classification = 'adult'
elif (age >= 65):
    human_classification = 'elder'

if (human_classification == 'baby' or human_classification == 'toddler' or
    human_classification == 'kid' or human_classification == 'teenager'):
    print(f'\nThis person is a {human_classification.capitalize()}!')
elif (human_classification == 'adult' or human_classification == 'elder'):
    print(f'\nThis person is an {human_classification.capitalize()}!')
