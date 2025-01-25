def main():
    path_to_file = "books/frankenstein.txt"
        
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = get_words_count(file_contents)
        char_count = get_chars_count(file_contents)
        # printing file contents and word count
        print(file_contents)
        print(word_count)
        print(char_count)
    
def get_words_count(file):
    words = file.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def get_chars_count(file):
    alpha_count = {}
    lower_file = file.lower()
    for char in lower_file:
        if char in alpha_count:
            alpha_count[char] += 1
        else:
            alpha_count[char] = 1
    return alpha_count

main()