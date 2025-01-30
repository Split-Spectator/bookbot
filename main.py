def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    lowercase_text = make_lower_case(text)
    result = counter(lowercase_text)

    print("--- Begin report of books/frankenstein.txt ---")
    word_count = len(text.split())
    print(f"{word_count} words found in the document\n")
    convert(result)
    print("--- End report ---")
    
def make_lower_case(text):
    return text.lower() 
   
def counter(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
            


def sort_on(filtered_list):
    return filtered_list["num"]

def convert(counts):
    filtered_list = []
    for char, num in counts.items():
        if char.isalpha():
           filtered_list.append({"char": char, "num": num})
    
    filtered_list.sort(reverse=True, key=sort_on)
    for item in filtered_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    return filtered_list

def get_text(path):
    with open(path) as f:
        return f.read()


main()
