def count_words(filename):
    """
    * Brief: Count the number of words in a book.
    * Param: filename  The file address of a .txt book.
    * Return: void
    """
    try:
        with open(filename, encoding="UTF-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print("File is not found.")
    else:
        words = contents.split()
        num_words = len(words)
        print("{} has {} words.".format(filename, num_words))

count_words("054_Frankenstein.txt")