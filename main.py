def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = count_words(text)
    character_dict = count_characters(text)
    character_list = [{"char": char, "count": count} for char, count in character_dict.items()]


    character_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{total_words} words found in the document")

    for item in character_list:
        print(f"The '{item["char"]}' character was found {item["count"]} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    # Define empty dictionary
    char_dict = {}

    # Convert text to lowercase
    lower_text = text.lower()

    # Loop over the text
    for char in lower_text:
        # Check if character is not a-z
        if not char.isalpha():
            continue

        # If the character already exists in dictionary
        if char in char_dict:
            # For each character increase the count by 1
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(dict):
    return dict["count"]
main()


