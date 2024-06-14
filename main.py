def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_count = get_book_char(text)
    print(f"{char_count} in book")
    sorted = sorting(char_count)
    for sort in sorted:
        if sort["char"].isalpha():
            print(f"The '{sort["char"]}' charactger was found {sort["num"]} times")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def get_book_char(text):
    lowered_text = text.lower()
    char_count = {}
    for cha in lowered_text:
        if cha in char_count:
            char_count[cha] += 1
        else:
            char_count[cha] = 1
    return char_count
            
def sort_on(dict):
     return dict["num"]
         
def sorting(dict):
    finished_sort = []
    for letter in dict:
        finished_sort.append({"char": letter,"num": dict[letter]})
    finished_sort.sort(reverse=True,key=sort_on)
    return finished_sort    


main()