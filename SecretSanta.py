# Iterate over every participant in the list,
# Assign every participant someone else in the list to be the person they give the gift two
# Each person has to give one gift to one person
import random


def SecretSanta(participants: list, guaranteedpairs=False):
    secretsantalist = {}
    if guaranteedpairs:
        # If there is a guaranteed pair, add those to the list first
        secretsantalist.update(guaranteedpairs)
    if len(participants) % 2 != 0:
        return "Uneven amount of participants."
        # Not built for odd amount of participants right now
    # Initialize the gifter, giftee dictionary
    needsgift = participants[:]
    # slice of participants to not iterate over a list you're modifying
    for person in participants:
        needsgiftminusperson = [x for x in needsgift if x != person]
        # list of participants - person, select giftee from this list
        if not needsgiftminusperson:
            # If the only person left in the list is that person, list will be 0 when that person is removed
            return SecretSanta(participants)
            # probably inefficient but whatever
        randomperson = random.choice(needsgiftminusperson)
        # select from participants that aren't the person or aren't already selected
        secretsantalist[person] = randomperson
        # adds it into the dictionary as gifter, giftee pair
        needsgift.remove(randomperson)
        # removes giftee from the list of people without gifts
    if len(set(secretsantalist.values())) != len(list(secretsantalist.values())) \
            or len(set(secretsantalist.keys())) != len(list(secretsantalist.keys())):
        print("Sorry, I messed something up in here. There are duplicates")
        for key in secretsantalist:
            print(key, secretsantalist[key])
        return ""
        # Compares len of set and list. If there are any duplicates then len of set will be different and
        # the error code will run
    for person in secretsantalist:
        print(f"{person:10}==>{'':5}{secretsantalist[person]}")
        # Prints the pairings in a nicer way
    return secretsantalist


def collectinput():
    # Collects the inputs to run the Secret Santa function with
    print("\nSecret Santa\n")
    guaranteedpairs = False
    guaranteedpair = input("Is there a guaranteed pair?\n(E.g. You want to force Payton to gift John in the Secret Santa List) Y/N: ")
    if guaranteedpair[0] == "Y" or guaranteedpair[0] == 'y':
        # Creates the optional parameter of guaranteedpairs for SecretSanta()
        amountofguaranteedpairs = int(input("How many guaranteed pairs? "))
        guaranteedpairs = {}
        for name in range(amountofguaranteedpairs):
            gifter = input(f"Gifter {name+1}: ")
            giftee = input(f"Giftee {name+1}: ")
            guaranteedpairs[gifter] = giftee
    amountofnames = int(input("Amount of People in this Secret Santa (excluding guaranteed pairs): "))
    if amountofnames % 2 != 0:
        print("Buddy boy, I don't know how to code something for an odd amount of people, please try again.\n\n")
        return collectinput()
    participantlist = []
    for name in range(amountofnames):
        participant = input(f"Name {name+1}: ")
        participantlist.append(participant)
    if guaranteedpairs:
        return SecretSanta(participantlist, guaranteedpairs)
    else:
        return SecretSanta(participantlist)
collectinput()
