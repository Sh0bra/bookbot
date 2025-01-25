def main():
    path_to_file = "books/frankenstein.txt"
    try:
        with open(path_to_file) as f:
            file_contents = f.read()
            word_count = get_words_count(file_contents)
            char_count = get_chars_count(file_contents)
            
            # printing file contents and word count
            print(f'--- Begin report of {path_to_file} ---')
            print(f'{word_count} words found in the document')
            print()
            for c in char_count:
                # if c == "\n":
                    # print(f'The \\n character was found {char_count[c]} times')  
                    # continue  
                print(f'The \'{c}\' character was found {char_count[c]} times')
            print('--- End report ---')
    except Exception as e:
        print(e)

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