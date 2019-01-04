def iterate_keys(length_in_bytes, remove_null_bytes = False):
    for key in range(0, 0x100 ** length_in_bytes):
        bytes = key.to_bytes(length_in_bytes, byteorder='little')
        if (remove_null_bytes):
            yield [byte for byte in bytes if byte != '\x00']
        else:
            yield [byte for byte in bytes]

def do_xor(msg, key):
    result = []
    key_ptr = 0
    key_len = len(key)
    for byte in msg:
        xored_byte = key[key_ptr] ^ ord(byte)
        key_ptr += 1
        if key_ptr >= key_len:
            key_ptr = 0
        result.append(xored_byte)
    return bytes_to_string(result)

def bytes_to_string(byte_list):
    return "".join(chr(byte) for byte in byte_list)


if __name__ == "__main__":
    import argparse
    import re

    parser = argparse.ArgumentParser(description="Symetric key encryption \'cracking\' algorithm with generated keys")
    parser.add_argument('--f', help="file name of the input text file.")
    parser.add_argument('--r', help="regular expression pattern for output matching.")
    parser.add_argument('--l', help="max key lenght to look for.", type=int)
    args = parser.parse_args()

    try:
        with open(args.f, "r") as file_handle:
            cypher_text = file_handle.read()
        cypher_text = "hello world!"
        gen = iterate_keys(args.l, True)
        for key in gen:
            decyphered = do_xor(cypher_text, key)
            match = re.match(args.r, decyphered)
            if match:
                print("Found key: {}".format(str(key)))
                break
        else:
            print("Didn't find anything that matches the pattern: {}".format(args.r))
    except e:
        print(e)