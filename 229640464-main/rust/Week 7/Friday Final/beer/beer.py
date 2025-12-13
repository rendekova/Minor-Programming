import re
def read_quotes(beerpath):
    # beerpath contains the path to the file beer.txt
    # read the contents of the file beerpath
    # filter out empty lines
    # Do not remove the "quotation marks"
    # put the lines in a list
    # return the list with all the quotes
    quotes = []
    with open(beerpath, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                quotes.append(line)
    return quotes

def change_beer_into_wine(single_quote):
    # in comes a single quote as string
    # change beer into wine and Beer into Wine, see assignment
    single_quote = re.sub(r'\bbeer\b', 'wine', single_quote)
    single_quote = re.sub(r'\bBeer\b', 'Wine', single_quote)

    # return the quote as string
    return single_quote

def write_quotes(winepath, winequotes):
    # winepath is the path to the file with wine quotes that has to be written
    # winequotes is the list with quotes
    with open(winepath, "w") as file:
        for quote in winequotes:
            file.write(quote + "\n")

# --------- do not change below lines ---------
def change_quotes(beerquotes):
    # do not change below code
    winequotes = list()
    for b in beerquotes:
        w = change_beer_into_wine(b)
        winequotes.append(w)
    return winequotes

def main():
    # do not change below code
    beerpath = "beer.txt"
    winepath = "wine.txt"
    # reads the file with quotes into the beerquotes list
    beerquotes = read_quotes(beerpath)
    # changes each quote from beer to wine
    winequotes = change_quotes(beerquotes)
    # write the list with winequotes to output
    write_quotes(winepath, winequotes)

if __name__ == "__main__":
    # do not change below code
    main()
