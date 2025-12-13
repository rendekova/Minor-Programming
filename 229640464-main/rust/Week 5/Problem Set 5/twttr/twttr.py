import twttr


def main():
    # Ask for an input in shorten version.
    s = input("Input: ")
    print(shorten(s))




def shorten(word):

    # Wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, ...
    if not isinstance(word, str):
        raise TypeError("shorten expects a str")

    vowels = set("aeiouAEIOU")
    return "".join(ch for ch in word if ch not in vowels)




if __name__ == "__main__":
     main()
