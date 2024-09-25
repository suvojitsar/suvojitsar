import string

def remove_punctuation(input_string):
    # Create a translation table for removing punctuation
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

if __name__ == "__main__":
    # Example usage
    text = input("Enter a string: ")
    clean_text = remove_punctuation(text)
    print("String without punctuation:", clean_text)
