import argparse
import string
import secrets


def generate_random_string(length):
    output = ''
    choice = string.digits + string.ascii_letters + string.punctuation
    choice = choice.replace("'", "")
    choice = choice.replace('"', '')
    for i in range(length):
        output += secrets.choice(choice)

    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Generate a secret key/password.  The string will include digits, letters, "
                                     "and punctuation, and has a default length of 50.")
    parser.add_argument("-l", "--length", help="Specify secret length", type=int, default=50)

    args = parser.parse_args()
    print(generate_random_string(args.length))
