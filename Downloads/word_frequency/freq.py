# --------------------------------------------
#   Name: Atmakuri Venkata Sai Revanth
#   ID: 1684293
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise 3: Word Frequency
# --------------------------------------------

# To access command line arguments
import sys


def command_line():
    # Adding command line arguments to a list and checking for errors
    # Return value:- address of list created
    fnames = []
    for i in sys.argv:
        fnames.append(i)

    # To check if the user inputed only inputfile or other arguments
    if len(fnames) != 2:
        # Error message since the user much include inputfilename
        if len(fnames) < 2:
            print("Too few command-line arguments")
            print("Please make sure to include name of inputfile")
            # Exit from the program
            exit()
        # Error message since there are more commandline arguments
        else:
            print("Too many command-line arguments")
            print("Please make sure to include only name of inputfile")
            # Exit from the program
            exit()
    return(fnames)


def open_file(filename):
    # To check if the inputfile is in same directory and open the file
    # Arguments : name of file and Return opened file
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        print("File Not Found")
        print("Make sure the inputfile is in same directory")
        # Since the file not found Exit from program
        exit()


def word_list(filename=None):
    # To create list of words in inputfile & sort them
    # Arguments : name of file
    # Return :- address of sorted word list
    filecontent = []
    cflag = True
    while cflag:
        line = filename.readline()
        if line == "":
            cflag = False
            break
        else:
            line.strip()
        for i in line.split():
            filecontent.append(i)
    # sort the word list by using sort method
    filecontent.sort()
    return(filecontent)


def words_freq(fcontent1):
    # To find the word count, frequncy and relative frequency
    # Arguments : List of sorted words in inputfile
    # Return : lists of ordered words, word count and word frequency
    i = 0
    words = []
    word_count = []
    word_freq = []
    # If there is only one element in the input file
    if len(fcontent1) == 1:
        words.append(fcontent1[i])
        word_count.append(1)
        f = round(1, 3)
        word_freq.append(f)
    # To count the frequency of word and it's relative frequency
    while (i < len(fcontent1)-1):
        count = 0
        # Since words were sorted in order as sequence
        if fcontent1[i] == fcontent1[i+1]:
            count += 1
            k = i+1
            # Since the sequence of word started count ends when sequence ends
            while (len(fcontent1)-1 != k):
                if fcontent1[k] == fcontent1[k+1]:
                    count += 1
                else:
                    # Since the sequence ends break from inner loop
                    # outer loop start from the next index the sequence ends
                    i = k
                    break
                k += 1
                # If sequence continues till the end of list
                if len(fcontent1)-1 == k:
                    i = k
                    break
        # Adding word, count and freqency to differents lists at same index
        words.append(fcontent1[i])
        word_count.append(count+1)
        f = round((count+1)/len(fcontent1), 3)
        word_freq.append(f)
        i += 1
        # If list comes to an end break from outer while loop
        if len(fcontent1)-1 == i:
            # if list contains only two different words
            if fcontent1[i-1] != fcontent1[i]:
                count = 0
                words.append(fcontent1[i])
                word_count.append(count+1)
                f = round((count+1)/len(fcontent1), 3)
                word_freq.append(f)
            break
    return(words, word_count, word_freq)


def data_output(words, word_count, word_freq, name):
    # To output the data to a output file
    # Arguments : address of words, words_count,word_freq and name of file
    # No return value
    outputf = name+".out"
    foutput = open(outputf, 'w')
    # Since the words, word_count and word_freq are added at same index
    for i in range(len(words)):
        foutput.write(words[i])
        foutput.write(" ")
        count = str(word_count[i])
        foutput.write(count)
        foutput.write(" ")
        freq = str(word_freq[i])
        foutput.write(freq)
        if i < len(words)-1:
            foutput.write("\n")
    # Closeing the output file
    foutput.close()


def main():
    user_input = command_line()
    finput = open_file(user_input[1])
    fcontent = word_list(finput)
    words, word_count, word_freq = words_freq(fcontent)
    data_output(words, word_count, word_freq, user_input[1])
    finput.close()


if __name__ == "__main__":
    main()
