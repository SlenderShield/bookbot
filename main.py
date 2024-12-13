def on_sort(dicti):
    return dicti["count"]

def sorted_chars(char_set):
    result_list = []
    for key in char_set.keys():
        dicti = dict()
        dicti["char"] = key
        dicti["count"] = char_set.get(key)
        result_list.append(dicti)
    result_list.sort(reverse=True,key=on_sort)
    return result_list

def character_count(string):
    char_count = dict()
    for char in string.lower():
        if not char.isalpha():
            continue
        if char_count.get(char) != None:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def word_count(string):
    return len(string.split())

def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} words found in the document")
    values = sorted_chars(character_count(file_contents))
    for value in values:
        print(f"The '{value.get('char')}' character was found {value.get('count')} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()
