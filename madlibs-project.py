words = {}

def store_input ():
    words ["noun1"] = input("Enter noun: ")
    words ["adjective1"] = input("Enter adjective: ")
    words ["adverb1"] = input("Enter adverb: ")
    words ["verb1"] = input("Enter verb: ")
    words ["noun2"] = input("Enter noun: ")
    words ["noun3"] = input("Enter noun: ")
    words ["adverb2"] = input("Enter adverb: ")
    words ["pronoun1"] = input("Enter pronoun: ")
    words ["adjective2"] = input("Enter adjective: ")
store_input()


def print_Madlib():
    print (words["noun1"] + ", the man that first set foot on the moon was very " + words["adjective1"] + " despite popular belief. ")
    print (words["adverb1"] + " often he was seen sweeping dirt paths or mopping ponds. ")
    print ("why? " + "He " + words["verb1"] + " everyday after class and once before bedtime. ")
    print ("Oh, but " + words["noun2"] + " is the crazy one")
    print ("They run all day with " + words["noun3"] + " ,I'll never understand. ")
    print ("But they always arrive " + words["adverb2"])
    print ("Why " + words["pronoun1"] + " does this, I might now understand.")
    print ("All I know is this madlibs is a " + words["adjective2"] + " mess. ")
print_Madlib()