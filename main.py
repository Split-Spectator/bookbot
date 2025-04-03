from stats import counter
import sys  

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        book_path = sys.argv[1]
        text = get_text(book_path)
        lowercase_text = make_lower_case(text)
        result = counter(lowercase_text)

    print("--- Begin report of   ---")
    word_count = len(text.split())
    print(f"{word_count} words found in the document\n")
    convert(result)
    print("--- End report ---")
    
def make_lower_case(text):
    return text.lower() 

def sort_on(filtered_list):
    return filtered_list["num"]

def convert(counts):
    filtered_list = []
    for char, num in counts.items():
        if char.isalpha():
           filtered_list.append({"char": char, "num": num})
    
    filtered_list.sort(reverse=True, key=sort_on)
    for item in filtered_list:
        print(f"{item['char']}: {item['num']}")
    
    return filtered_list

def get_text(path):
    with open(path) as f:
        return f.read()


main()
