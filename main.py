import operator


def main():

    path_to_book = "books/frankenstein.txt"

    with open(path_to_book) as f:
        file_centents = f.read()

        #print(num_words_in_string(file_centents))

        #print(num_of_letters(file_centents))

        generate_report(num_of_letters(file_centents), num_words_in_string(file_centents), path_to_book)

    return 0

def num_words_in_string(book_text):
    words = book_text.split()

    num_words = len(words)

    return num_words


def num_of_letters(book_text):
    words = book_text.split()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", 
                "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter_numbers_dict = {}
    
    for alpha in alphabet:
        count = 0
        for word in words:
            letters = [*word]
            for letter in letters:
                low_letter = letter.lower()
                if low_letter == alpha:
                    count += 1
        letter_numbers_dict[alpha] = count

    return letter_numbers_dict

def generate_report(number_letters_dict, num_words, book_path):

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    number_letters_list = []


    for key in number_letters_dict:
        number_letters_list.append({"letter":key, "number":number_letters_dict[key]})

    number_letters_list.sort(reverse=True, key=operator.itemgetter('number'))

    for dict in number_letters_list:
        print(f"The '{dict['letter']}' character was found {dict['number']} times")

    
    print("--- End Report ---")

    return 0
    





main()




