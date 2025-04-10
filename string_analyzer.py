from string_package import *
from string_package import *

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    reversed_text = reverse_string(sentence)
    capitalized_text = capitalize_words(sentence)
    cleaned_text = remove_punctuation(sentence)

    print("\nReverse:", reversed_text)
    print("High case:", capitalized_text)
    print("Remove punctuation:", cleaned_text)
    print("Character count:", count_characters(cleaned_text))
    print("Word count:", count_words(cleaned_text))
    print("Average word length:", average_word_length(cleaned_text))
