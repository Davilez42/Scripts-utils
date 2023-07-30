from random import randint
from string import ascii_lowercase
"""
* Password Generator Script
*
* 
* Commands
* -l : generate a password between 16 and 8 characters
* -s : contains symbols
* -m : contains mayus
* -n : contains numbers

* Examples 
* generate-password -l -s 
* generate-password -l 
* generate-password -l -s -m 
* generate-password -s -m 

"""


def init():
    input_ = str(input('!->'))
    params = input_.split()
    if params[0] == "generate-password":
        print(generatePassword(params[1::]))
    else:
        raise Exception('Params incorrects')


def generatePassword(configs: list):
    LETTERS = list(ascii_lowercase)
    SYMBOLS = list(map(chr, range(33, 47)))
    NUMBERS = [x for x in range(11)]
    MAYUS = False
    
    config_loaded = [LETTERS]
    long = int(randint(5, 11))
    
    # load configs add
    if configs.count('-n') != 0:
        config_loaded.append(NUMBERS)

    if configs.count('-s') != 0:
        config_loaded.append(SYMBOLS)

    if configs.count('-l') != 0:
        long = int(randint(8, 17))

    if configs.count('-m') != 0:
        MAYUS = True

    passwod = ""
    for i in range(0, long):
        r = randint(0, len(config_loaded)-1)
        n = randint(0, len(config_loaded[r])-1)
        character_generated = str(config_loaded[r][n])
        if MAYUS and r == 0:
            if (randint(0, 1)):
                character_generated = character_generated.upper()
        passwod += character_generated

    return passwod


if __name__ == '__main__':
    try:
        init()
    except Exception as e:
        print(e)
