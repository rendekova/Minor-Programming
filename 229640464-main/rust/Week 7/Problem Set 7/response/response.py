from validator_collection import validators


def main():
    email = input("What's your email address?").strip()
    # Outputs Valid or Invalid if the input is a syntatically valid email address
    try:
        validators.email(email)
        print("Valid")
    except ValueError:
        print("Invalid")



if __name__ == "__main__":
    main()

