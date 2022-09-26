def emoji_converter(message):
    words_in_message = message.split(" ")
    emoji = {
        ":)": "😀",
        ":(": "😩"
    }
    output = ""
    for word in words_in_message:
        output += emoji.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))
