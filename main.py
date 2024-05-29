def main():

    with open("books/frankenstein.txt") as f:
        file_centents = f.read()
        print(file_centents)

        print(num_words_in_string(file_centents))

        print(num_of_letters(file_centents))

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





main()




