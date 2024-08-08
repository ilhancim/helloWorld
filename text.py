import time
text = input("Enter your text: ")

newText= ""
for letter in text:
    if letter >= "A" and letter <= "Z":
        for x in range(ord("A"),ord(letter)+1):
            newText += chr(x)
            print(newText)
            time.sleep(0.1)
            if chr(x) != letter:
                newText=newText[:-1]

    elif letter >= "a" and letter <= "z":
        for x in range(ord("a"),ord(letter)+1):
            newText += chr(x)
            print(newText)
            time.sleep(0.1)
            if chr(x) != letter:
                newText=newText[:-1]

    if letter >= " " and letter <= "!":
        for x in range(ord(" "),ord(letter)+1):
            newText += chr(x)
            print(newText)
            time.sleep(0.1)
            if chr(x) != letter:
                newText=newText[:-1]