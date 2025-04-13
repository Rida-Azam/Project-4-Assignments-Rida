# Write a program which prompts the user for an adjective, then a noun, then a verb,
#  and then prints a fun sentence with those words!

SENTENCE_START: str = "Learning Python is exciting. I explored coding and built my "

def main():
    adjective:str=input("Please Enter a Adjective : ")
    noun:str=input("Please Enter a Noun : ")
    verb:str=input("Please Enter a Verb : ")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

main()    
# output
# Learning Python is exciting. I explored coding and built my Creative  Website Designed!