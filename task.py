# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Main program
def main():
    # Get the user's name and favorite numbers
    name = input("Enter your name: ")
    num1 = int(input("Enter your first favorite number: "))
    num2 = int(input("Enter your second favorite number: "))
    num3 = int(input("Enter your third favorite number: "))

    # Store the numbers in a list
    numbers = [num1, num2, num3]

    # Greet the user
    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    # Check if the numbers are even or odd
    for num in numbers:
        if num % 2 == 0:
            print(f"The number {num} is even.")
        else:
            print(f"The number {num} is odd.")

    # Print the number and its square
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num ** 2})")

    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    # Check if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number.")

# Run the main program
if __name__ == "__main__":
    main()
