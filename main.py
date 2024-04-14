import sys
import os


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <book_path>")
        sys.exit(1)

    book_path = sys.argv[1]

    if not os.path.exists(book_path):
        print(f"Error: File '{book_path}' not found.")
        sys.exit(13)

    try:
        text = get_book_text(book_path)
        word_count = get_word_count(text)
        character_count = get_character_counts(text)
        char_list = char_dict_to_sorted_list(character_count)

        print_report(book_path, word_count, char_list)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(69)


def get_book_text(book_file_path):
    with open(book_file_path) as file:
        return file.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_counts(text):
    char_counts = {}

    lower_case_text = text.lower()

    for char in lower_case_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def char_dict_to_sorted_list(dict):
    char_list = []
    for char in dict:
        char_list.append({"char": char, "count": dict[char]})

    char_list.sort(reverse=True, key=sort_on_count)
    return char_list


def sort_on_count(dict):
    return dict["count"]


def print_report(document, word_count, char_list):
    print(f"\n--- Begin report of {document} ---")
    print(f"{word_count} words found in document\n")
    for char in char_list:
        if char["char"].isalpha():
            print(
                f"The '{char["char"]}' character was found {
                    char["count"]} times"
            )
    print("--- End report ---")


main()
