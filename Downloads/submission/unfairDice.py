"""
##########################################################################
    Name: Avs Revanth
    Student_id: 1684293
    CMPUT 274 Fall 2020
    Weekly Exercise = 2
    Exercise: Unfair Dice and Histogram
##########################################################################
"""
# Random module to generate number from [0,1) and seed module
import random

# Auguments probablity list, seed value, and number of rolls and return rolls
def biased_rolls(prob_list, s, n):
    # Initize all local variables for this function
    rolls = []
    outer_i = 0
    random_num = 0
    # Initize seed value
    random.seed(s)
    prob_sum = 0
    number_list = []
    prob_total = []
    # To make a list of numbers and to order the given probablity
    for i in range(len(prob_list)):
        prob_sum += prob_list[i]
        number_list.append(i+1)
        prob_total.append(prob_sum)
    # loop ends after n rolls 
    while (outer_i < n):
        # Call to random fuction
        random_num = random.random()
        inner_i = 0
        # To generate number in given probability
        while (inner_i < len(prob_list)):
            # To check for first number
            if inner_i == 0:
                if 0 <= random_num and prob_total[inner_i] > random_num:
                    rolls.append(number_list[inner_i])
                    break
            elif prob_total[inner_i - 1] <= random_num and prob_total[inner_i] > random_num:
                rolls.append(number_list[inner_i])
                break
            inner_i += 1
        outer_i += 1
    # return the resulting rolls
    return rolls
# Auguments m(sides of dices), rolls(Total rolls generated) and width of histogram  No return value
def draw_histogram(m, rolls, width):
   # Initize all local variables for this function
    count = []
    outer_j = 0
    outer_k = 0
    inner_k = 0
    # To count the Frequency of the number
    while (outer_j < m):
        count_value = 0
        for i in range(len(rolls)):
            if rolls[i] == (outer_j+1):
                count_value += 1
        count.append(count_value)
        outer_j += 1

    # Block-1 :- if number of rolls are greater than width 
    condition = True
    if len(rolls) > width:
        while condition:
            boo = True
            # To check if any number is greater than width
            for i in count:
                if i > width:
                    boo = False
            if boo == False:
                # To fit the given width
                for i in range(len(count)):
                    count[i] /= 2
            if boo == True:
                condition = False
    if condition == False:
        for i in range(len(count)):
            count[i] = round(count[i])

    # Block-2 :- if number of rolls are less than width
    condition = True
    if len(rolls) < width:
        while condition:
            boo = True
            # To check if any number is less than width
            if max(count) < width:
                boo = False
            if boo == False:
                # To fit the given width
                for i in range(len(count)):
                    count[i] = count[i] * 2
            # If number corss the limit
            if max(count) > width:
                for i in range(len(count)):
                    count[i] = (count[i]) / 2
                boo = True
            if boo == True:
                condition = False
    if condition == False:
        for i in range(len(count)):
            count[i] = round(count[i])  
    # Printing the histogram     
    print(f"Frequency Histogram: {m}-sided Die")
    while (outer_k < m):
        inner_k = 0
        print(f"{outer_k+1}.", end="")
        while (inner_k < width):
            if count[outer_k] > inner_k:
                print("#", end="")
            else:
                print("-",end="")
            inner_k += 1
        print()
        outer_k += 1
    pass

    # There is no return value for this function


if __name__ == "__main__":
    prob_list = list(map(float, input("Enter: ").split()))
    seed_value = int(input("Enter the seed value: "))
    n = int(input("Enter no.of rolls: "))
    rolls = biased_rolls(prob_list, seed_value, n)

    m = len(prob_list)
    width = int(input("Enter the width: "))
    draw_histogram(m, rolls, width)

    pass
