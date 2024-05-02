message = input("> ")
words = message.split(" ")
imoji = {
    ":)": "😊",
    ":(": "😔"
}
output = ""
for word in words:
    if word in imoji:
        output += imoji[word]
    else:
        output += word + " "
print(output)
