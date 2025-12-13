import emoji

def main():


    s = input("Input: ")


    # Function to outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
    n = emoji.emojize(s, language="alias")

    print(f"Output: {n}")



if __name__ == "__main__":
    main()


