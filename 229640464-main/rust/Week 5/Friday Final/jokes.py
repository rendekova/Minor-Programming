import pyjokes
import sys

LANGUAGES = ["cs", "de", "en", "es", "eu", "fr", "gl", "hu", "it", "lt", "pl", "ru", "sv"]
def read_arg():

    # Default language called default_language
    default_language = "en"

    # Check of the extra argument
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if len(arg) == 3 and arg.startswith("-"):
            s = arg[1:]
            if s in LANGUAGES:
                default_language = s


    # If more arguments are entered, they must be ignnored.
    return default_language


def get_single_joke(lang):

    try:
        joke = pyjokes.get_joke(language=lang)
        return joke

    # If any error occurs it returns the string "Bad joke".
    except Exception:
        return "Bad joke"



def main():
    lang = read_arg()
    joke = get_single_joke(lang)
    print(joke)

if __name__ == "__main__":
	main()
