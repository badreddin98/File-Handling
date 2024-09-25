import os

def list_directory_contents(path):
    try:
        # List all files and subdirectories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user for the directory path
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)
