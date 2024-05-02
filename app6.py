def imoji_converter(message):
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
    return output


message = input("> ")

print(imoji_converter(message))