def is_upper(c):
    if (c >= ord('A')) & (c <= ord('Z')):
        return True
    return False
    
def is_lower(c):
    if (c >= ord('a')) & (c <= ord('z')):
        return True
    return False

def shift(text, step):
    output = ""
    for letter in text:
        char = ord(letter)
        if is_lower(char):
            char = ord(letter)+step
            while (char > ord("z")):
                char-=26
        if is_upper(char):
            char = ord(letter)+step
            while (char > ord("Z")):
                char-=26
        output+=chr(char)
    return output


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Outputs all the shifts of the english alphabet, case INsensitive.")
    parser.add_argument('--f', help="file name of the encrypted text file.")
    args = parser.parse_args()

    try:
        with open(args.f, "r") as file_handle:
            cypher_text = file_handle.read()
            for step in range (1, 27):
                print("step = {}".format(step))
                print(shift(cypher_text, step))
                print("====================")
    except:
        print("Failed to open the file: " + args.f)
        exit(-1)