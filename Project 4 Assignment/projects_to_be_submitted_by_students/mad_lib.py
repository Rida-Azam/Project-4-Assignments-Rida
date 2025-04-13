# Mad libs Python Project

# Collect user inputs

name = input("Enter your name : ")
programming_language=input("Enter a programming language : (e.g:python,next js, typrescript, java, html) : ")
mentor=input("Enter mentor name : ")




# Create the story
story = f"""
Once upon a time, there was a curious learner named {name}.
{name} decided to master {programming_language}, a language that many said was both powerful and fun.
With guidance from a brilliant mentor named {mentor}, {name} tackled every bug and challenge with determination.
Day by day, {name} grew more confident, eventually building amazing projects and inspiring others to code too.
All thanks to the incredible journey with {programming_language} and the support of {mentor}!
"""

print("\nHere's your personalized Mad Libs story:")
print(story)