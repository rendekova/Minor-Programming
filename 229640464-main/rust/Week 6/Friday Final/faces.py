def convert(emoji):
  # Replace emoticons to emojis
  emoji = emoji.replace(":)", "🙂")
  emoji = emoji.replace(":(", "🙁")
  emoji = emoji.replace(";)", "😉")
  emoji = emoji.replace(":frog:", "🐸")
  return emoji

def main():
    x = input (" Answer: ")
    result = convert(x)
    print(result)

if __name__ == "__main__":
  main()
