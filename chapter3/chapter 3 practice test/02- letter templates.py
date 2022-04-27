letter = '''</NAME/>,
greeting from abc coding house.i am happy to tell you about your selection
you are selected!
have a great day ahead!
thanks and regards
billy
YOU ARE SELECTED
</DATE/>'''

name = input("enter your name\n")
date = input("enter date\n")
letter = letter.replace("</NAME/>",name)
letter = letter.replace("</DATE/>",date)
print(letter)
