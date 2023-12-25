import random
import string


def generate_incredibly_complex_password(length):
    # Define character sets for an incredibly complex password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = '!@#$%^&*()_-+=[]{}|;:,.<>?/~`'
    more_special_characters = r'"\'\\'
    punctuation_characters = string.punctuation

    # Combine all character sets to form an incredibly complex password pool
    all_characters = (
        uppercase_letters + lowercase_letters +
        digits + special_characters +
        more_special_characters + punctuation_characters
    )

    # Ensure that the password has at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters),
        random.choice(more_special_characters),
        random.choice(punctuation_characters),
    ]

    # Fill the rest of the password with random characters
    remaining_length = length - len(password)

    # Introduce additional complexity with more diverse character choices
    password.extend([
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters),
        random.choice(more_special_characters),
        random.choice(punctuation_characters),
        random.choice(all_characters)
    ] * (remaining_length // 7))

    # Shuffle the password to make the order random
    random.shuffle(password)

    return ''.join(password)


def export_to_txt(password, filename):
    # Export the password to a text file
    with open(filename, 'w') as file:
        file.write(password)
    print(f"Password has been saved to {filename}")


def generate_and_display_options(length):
    # Generate 5 password options
    options = [generate_incredibly_complex_password(length) for _ in range(5)]

    # Display the generated password options
    print("Generated Password Options:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    # Ask the user if they want to generate again
    retry = input("Do you want to generate again? (y/n): ").lower()
    if retry == "y":
        # If yes, generate new options
        return generate_and_display_options(length)
    elif retry == "n":
        # If no, ask the user to choose a password
        choice = int(
            input("Choose the password by entering its number (1-5): "))
        if 1 <= choice <= 5:
            return options[choice - 1]
        else:
            raise ValueError(
                "Invalid choice. Please enter a number between 1 and 5.")
    else:
        raise ValueError("Invalid input. Please enter 'y' or 'n'.")


def main():
    try:
        # Get the desired length for the password
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")

        # Generate and display password options
        # Allow the user to choose or retry the generation process
        password = generate_and_display_options(length)

        # Get the filename to save the chosen password
        filename = input(
            "Enter the filename to save the password (including .txt extension): ")

        # Save the chosen password to a text file
        export_to_txt(password, filename)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
