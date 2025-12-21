def get_secret_number():
    """Get a secret number from user input."""
    while True:
        try:
            secret_number = int(input("Enter a secret number: "))
            return secret_number
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    secret = get_secret_number()
    print(f"Your secret number is: {secret}")