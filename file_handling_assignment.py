# file_handling_assignment.py

# Task 1: File Creation
try:
    # Open a new text file in write mode
    with open("Week_5_assignment/my_file.txt", 'w') as file:
        # Write at least three lines of text to the file
        file.write("Hello, this is line 1.\n")
        file.write("This is line 2 with a number: 42\n")
        file.write("And here is line 3 with a mix of text and numbers: 12345\n")
    print("File created and written successfully.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# Task 2: File Reading and Display
try:
    # Open the file in read mode and display its contents
    with open("Week_5_assignment/my_file.txt", 'r') as file:
        content = file.read()
        print("\nReading the file content:")
        print(content)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Task 3: File Appending
try:
    # Open the file in append mode
    with open("Week_5_assignment/my_file.txt", 'a') as file:
        # Append three additional lines of text to the existing content
        file.write("This is an appended line 4.\n")
        file.write("Appending line 5 with another number: 6789\n")
        file.write("Finally, appended line 6 with mixed content: Hello123\n")
    print("File appended successfully.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Task 4: Error Handling
try:
    # Attempt to open a file that does not exist to demonstrate error handling
    with open("non_existent_file.txt", 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file 'non_existent_file.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
