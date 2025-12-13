def ask() -> str:
    # TODO: ask for a text to change into title and return as string
    text = input("Make a title from... : ")
    return text

def titlize(s: str) -> str:
	# TODO change s into title form and return as string
	return s.title()




def main():
	# do not change code below
	s = ask()
	s = titlize(s)
	print(f"The title is: {s}")

if __name__ == "__main__":
	# do not change code below
	main()

# run test with:
# python test_one.py 
# pytest test_strings.py
