def main():
    path_to_file = "books/frankenstein.txt"
        
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        # printing file contents and word count
        print(file_contents)
        print(word_count)
    
def get_word_count(file):
    words = file.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

main()