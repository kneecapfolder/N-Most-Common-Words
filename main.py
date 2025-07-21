# https://www.youtube.com/watch?v=ZQ9JO0e9468

import sys

def main(path):

    n = 0
    txt = ""
    words_count = {}

    # get n if file was ran correctly
    try:
        n = int(sys.argv[1])
    except:
        print("Please run 'main.py' through a terminal in this format: 'python main.py {n}' (n = an integer)")
        return
    
    # open read file if 'path' leads to a file
    try:
        with open(path, "r") as file:
            txt = file.read()
    except:
        print(f"A file named '{path}' could not be found in this directory")

    # delete all instances of [\n], [.] and [,] and create a set from all the words (no duplicates)
    words = set(txt.translate(str.maketrans({ '\n': '', '.': '', ',': '' })).split(' '))

    # count each word in the sentence
    for word in words:
        words_count[word] = txt.count(word)

    # turn the dictionary in to a list of the tuples (word, num of appearances) sorted by how common they are
    common_words = sorted(words_count.items(), key=lambda item: item[1], reverse=True)

    # print the n most common words according to the given format
    for i in range(min(n, len(common_words))):
        print(f"{i + 1} - \"{common_words[i][0]}\" {common_words[i][1]} times")



if __name__ == "__main__":
    main("./file.txt")