from collections import OrderedDict
def print_distinct_words_and_number_of_occurance(ordered_dictionary):
    #Prints the number of occurances of each distinct word
    print("{}".format(len(ordered_dictionary)))
    #Iterates through the dictionary and prints the values
    for value in ordered_dictionary.values():
        #end='' takes space to print it at the end of each value
        print("{}".format(value),end=' ')

if __name__ == "__main__":
    ordered_dictionary = OrderedDict()

    for _ in range(int(input())):
        #To get the number of words
        item = input()
        #Filling up the dictionary with the words and their occurances
        #get() method takes two parameters. The first one is the key and the second one           (optional) is the value that will be returned if the key is not found. The               default value is None.
        ordered_dictionary[item] = ordered_dictionary.get(item,0) + 1
        #Calling the function
    print_distinct_words_and_number_of_occurance(ordered_dictionary)
