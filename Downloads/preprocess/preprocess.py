#--------------------------------------------
#   Name: Atmakuri Venkata Sai Revanth
#   ID: 1684293
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise #4: Text Preprocessor
#--------------------------------------------
# sys module to take commandline arguments
import sys


def read_cline(kdigit=True, kstops=True, ksymbols=True):
    """
    Reads commandline arguments and check for errors and mode. Exits
    the program if given mode is different or if more arguemnts.

    Arguments (bools): Optional arguments kdigit, kstops, ksymbols default
                       set to True

    Returns (bools): states of kdigit, kstops, ksymbols
    """
    command_line = []
    for i in sys.argv:
        command_line.append(i)
    # To check for given mode
    if len(command_line) == 2:
        if command_line[1] == "keep-digits":
            kdigit = False
        elif command_line[1] == "keep-stops":
            kstops = False
        elif command_line[1] == "keep-symbols":
            ksymbols = False
        # Exits the program since the given mode is not correct
        else:
            print("Wrong mode of input!\nPlease make sure to enter " +
            "one of the below mode\n'keep-digits': will not"
            + " remove numbers from words\n'keep-stops': will" +
            " not remove stopwords\n'keep-symbols': will not" +
             "remove punctuation or symbols")
            exit()
    # Exits the program since there are more command line arguments given
    elif len(command_line) > 2:
        print("Too many command_line values\nplease make sure to " +
        "enter only one of the below mode\n'keep-digits': will not" +
        " remove numbers from words\n'keep-stops': will" +
        " not remove stopwords\n'keep-symbols': will not"
        " remove punctuation or symbols")
        exit()
    return(kdigit, kstops, ksymbols)


def wordslist():
    """
    Reads the input line and add the given words to a list

    Arguments : No arguemnts required

    Returns (List) : Address of the word list created
    """
    word_list = []
    try:
        userinput = list(input().split())
        return (userinput)
    except EOFError:
        return (userinput)


def lowercasewords(word_list):
    """
    Converts all Uppercase letters in the given list of words into Lowercase

    Arguments (List): Address of list of words to process

    Returns (List): Address of new list created
    """
    word_list1 = []
    for i in range(len(word_list)):
        string = ""
        for j in range(len(word_list[i])):
            asci = ord(word_list[i][j])
            if asci >= 65 and asci <= 90:
                # Converts to lower case since ascii value of letter is
                # between 65 to 90 are Upper case letters
                string += chr(asci + 32)
            else:
                string += word_list[i][j]
        word_list1.append(string)
    return (word_list1)


def R_symbols(word_list):
    """
    Removes all punctuation and symbols in the given list of words

    Arguments (List): Address of list of words to process

    Returns (List): Address of new list created after removing symbols
    """
    word_list2 = []
    for i in range(len(word_list)):
        string = ""
        for j in range(len(word_list[i])):
            asci = ord(word_list[i][j])
            # Adding only letter which are letters or digits and other
            # Character will not be added since they are consider symbols
            if asci >= 97 and asci <= 122:
                string += word_list[i][j]
            elif asci >= 48 and asci <= 57:
                string += word_list[i][j]
        word_list2.append(string)
    return (word_list2)


def R_digits(word_list):
    """
    Removes digits if they are part of word and keep digits if word consists
    only number

    Arguments (List): Address of list of words to process

    Returns (List): Address of new list created
    """
    word_list3 = []
    for i in range(len(word_list)):
        string1 = ""
        string2 = ""
        for j in range(len(word_list[i])):
            asci = ord(word_list[i][j])
            if asci >= 48 and asci <= 57:
                string1 += word_list[i][j]
            else:
                string2 += word_list[i][j]
        # If the given word contain only digits
        if len(string1) == len(word_list[i]):
            word_list3.append(string1)
        else:
            # If the given word contains both digits and letters
            word_list3.append(string2)
    return (word_list3)


def R_stops(word_list):
    """
    Removes stopwords if they are in the given list and add new words to a new
    list

    Arguments (List): Address of list of words to process

    Returns (List): Address of new list of words after removing stopwords
    """

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves",
    "you", "your", "yours", "yourself", "yourselves", "he", "him", "his",
    "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they",
    "them", "their", "theirs", "themselves", "what", "which", "who", "whom",
    "this", "that", "these", "those", "am", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "having", "do", "does", "did",
    "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
    "until", "while", "of", "at", "by", "for", "with", "about", "against",
    "between", "into", "through", "during", "before", "after", "above",
    "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then", "once", "here", "there", "when",
    "where", "why", "how", "all", "any", "both", "each", "few", "more",
    "most", "other", "some", "such", "no", "nor", "not", "only", "own",
    "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
    "don", "should", "now"]
    word_list4 = []
    for i in word_list:
        if i in stop_words:
            pass
        else:
            word_list4.append(i)
    return (word_list4)


def main():
    """
    The complete process of code is excited from this main() function
    No Arguemnts and No returns values
    The final processed words will be printed from this function
    """
    kdigit, kstops, ksymbols = read_cline()
    word_list = wordslist()
    word_list = lowercasewords(word_list)
    # if the given mode is to keep-digits
    if kdigit is False:
        word_list = R_symbols(word_list)
        word_list = R_stops(word_list)
    # if the given mode is to keep-stops
    elif kstops is False:
        word_list = R_symbols(word_list)
        word_list = R_digits(word_list)
    # if the given mode is to keep-symbols
    elif ksymbols is False:
        word_list = R_digits(word_list)
        word_list = R_stops(word_list)
    # if no mode is present
    else:
        word_list = R_symbols(word_list)
        word_list = R_digits(word_list)
        word_list = R_stops(word_list)
    processed_words = word_list[:]
    # Final list of processed words
    print(*processed_words)


if __name__ == "__main__":
    main()
