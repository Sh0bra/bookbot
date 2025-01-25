def main():
    path_to_file = "books/frankenstein.txt"

    word_count = 0
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)
        words = file_contents.split()
        for word in words:
            word_count += 1
        
    print(word_count)
    

main()