# Paste your code into this box
def main():
    correct = False
    low, high = 0, 100
    validRep = {"h", "l", "c"}
    print("Please think of a number between 0 and 100!")
    while not correct:
        guess = (low + high) // 2
        print(f"Is your secret number {guess}?")
        inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if inp not in validRep:
            print("Sorry, I did not understand your input.")
        elif inp == "c":
            correct = True
            print(f"Game over. Your secret number was: {guess}")
        elif inp == "h":
            high = guess
        else:
            low = guess + 1        
    return
if __name__ == "__main__":
    main()