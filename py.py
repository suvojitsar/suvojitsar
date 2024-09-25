import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

text = "suvojit@sarkar : section-H : bwu/bta/22/472 : BRAINWARE@UNIVERSITY"

clean_text = remove_punctuation(text)

print("String without punctuation:", clean_text)
