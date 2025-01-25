import string

def main():
    path_to_file = "books/frankenstein.txt"
    try:
        with open(path_to_file) as f:
            file_contents = f.read()
            word_count = get_words_count(file_contents)
            char_count = get_chars_count(file_contents)
            char_count.sort(reverse=True, key=sort_on)
            #printing file contents and word count
            print(f'--- Begin report of {path_to_file} ---')
            print(f'{word_count} words found in the document')
            print()
            for c in char_count:
                print(f'The \'{c["char"]}\' character was found {c["count"]} times')
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
    alpha = list(string.ascii_lowercase)
    alpha_count = {}
    lower_file = file.lower()
    for char in lower_file:
        if char in alpha:
            if char in alpha_count:
                alpha_count[char] += 1
            else:
                alpha_count[char] = 1

    alpha_list = []
    for item in alpha_count.items():
        tmp = {}
        tmp["char"] = item[0]
        tmp["count"] = item[1] 
        alpha_list.append(tmp)
    return alpha_list

def sort_on(dict):
    return dict["count"]

main()