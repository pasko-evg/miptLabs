dictionary = {}

start_words = ["Hello",
               "Welcome back",
               "Good afternoon",
               "Nice to meet you",
               "Excuse me",
               "Good evening",
               "I have to apologize",
               "Not quite"]

def fill_dict(encode_str: str, decode_str: str):
    for i in range(len(encode_str)):
        encode_char = encode_str[i]
        decode_char = decode_str[i]
        dictionary[encode_char.lower()] = decode_char.lower()
        dictionary[encode_char.upper()] = decode_char.upper()


def check_string(line: str):
    mod_line = line.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    line_words = mod_line.split()
    # print(line_words)
    # hello
    if len(line_words[0]) == 5:
        # print("1")
        fill_dict(line_words[0], "Hello")

    # Welcome back
    if len(line_words[0]) == 7 and len(line_words[1]) == 4:
        # print("2")
        fill_dict(line_words[0] + " " + line_words[1], "Welcome back")

    # Good afternoon
    if len(line_words[0]) == 4 and len(line_words[1]) == 9:
        # print("3")
        fill_dict(line_words[0] + " " + line_words[1], "Good afternoon")

    # Nice to meet you
    if len(line_words[0]) == 4 and len(line_words[1]) == 2 and len(line_words[2]) == 4 and len(line_words[3]) == 3:
        # print("4")
        fill_dict(line_words[0] + " " + line_words[1] +
                  " " + line_words[2] + " " + line_words[3], "Nice to meet you")

    # Excuse me
    if len(line_words[0]) == 6 and len(line_words[1]) == 2:
        # print("5")
        fill_dict(line_words[0] + " " + line_words[1], "Excuse me")

    # Good evening
    if len(line_words[0]) == 4 and len(line_words[1]) == 7:
        # print("6")
        fill_dict(line_words[0] + " " + line_words[1], "Good evening")

    # I have to apologize
    if len(line_words[0]) == 1 and len(line_words[1]) == 4 and len(line_words[2]) == 2 and len(line_words[3]) == 9:
        # print("7")
        fill_dict(line_words[0] + " " + line_words[1] +
                  " " + line_words[2] + " " + line_words[3], "I have to apologize")

    # Not quite
    if len(line_words[0]) == 3 and len(line_words[1]) == 5:
        # print("8")
        fill_dict(line_words[0] + " " + line_words[1], "Not quite")


if __name__ == "__main__":
    encode_text = []
    for i in range(int(input())):
        encode_text.append(input())
    # print(encode_text)

    # Fill dictionary
    for line in encode_text:
        check_string(line)

    # char = list(dictionary.keys())
    # char.sort()
    # for c in char:
    #     print("{} = {}".format(c, dictionary[c]))

    decode_text = []
    for encode_line in encode_text:
        decode_line = []
        for encode_char in encode_line:
            if encode_char in list(dictionary.keys()):
                decode_line.append(dictionary[encode_char])
            else:
                decode_line.append(encode_char)
                # print("azaza:", encode_char)
        decode_text.append("".join(decode_line))

    for i in decode_text:
        print(i)