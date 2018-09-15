# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 20:02:37 2018

@author: Radam
"""
#Found online
import pathlib
from string import punctuation

dicta = {}
line_count = 0
user_in = " "


#Step 4
#Method prompts the user for a word(s) they'd like to search throughout the file
def prompt():
    #prompts the user for a word(s). Each word should be seperated by a whitespace
    user_in = input("Input the word(s) you'd like to search, seperated by a whitespace each time (q:quit): ")
    
    if (user_in == "q"):
        print("Exiting...")
        return
    else:
        #takes the users input and splits it by each word into a list
        user_in = user_in.split()
        #returns the list
        return user_in
    

#Step 3
#Method removes all punctuation from a string
def remove_punctuation(s1):
    #returns the string with all punctuation removed
    return ''.join(word for word in s1 if word not in punctuation)

#print(remove_punctuation("@Hel%lo!! how are you?"))

#Step 2
#Method processes the file 
def process():
    
    #opens the file
    with open("prob3.txt") as f:
        while True:
            #breaks out of the while loop if the use enters "q" 
            if(user_in == "q"):
                break
            else:
                #counter for counting the number of lines in the file
                line_count = 0
                #loops through the file line by line
                for line in f:
                    line_count += 1
                    #strips all punctuation line by line and saves it a "newLine"
                    newLine = remove_punctuation(line)
                    #takes "newLine" and changes all characters to lower case and strips each word so now "list1" is a list
                    list1 = newLine.lower().split()
                    for word in list1:
                        if word not in dicta:
                            dicta[word] = [line_count]
                        else:
                            if(line_count not in dicta[word]):
                                dicta[word].append(line_count)
                lista = []
                #loops through the words in the list returned from prompt()  
                for x in prompt():
                    try:
                        #if the word is a key in dicta
                        if x in dicta.keys():
                            lista.append(dicta.get(x))
                            #convert list of list to list of sets
                            sets = map(set, lista)
                            #perform intersection on each set present in list
                            common_items = set.intersection(*sets)
                            
                        else:
                            print("Word not Found")

                    except TypeError:
                        pass
                #print common_items
                print(common_items)
                #This acts as an answer key
                print()
                print("Complete file dictionary:")             
                print(dicta)
                
#Step 1
#Main method that prompts the user for a filename
def main():
    #prommpts the user for a filename 
    filename = input("Give me a file name with extension (q:quit): ")
    #loops through until the user inputs"q" to stop
    while True:
        #breaks out of the while loop if the use enters "q" 
        if(filename == "q"):
            break
        else:
            try:
                #"path" is an embred function that looks to see if the path of your filename exist
                path = pathlib.Path(filename)
                #if the path exists then do something..
                if(path.exists()):
                    #run the process() method above 
                    process()
                    return
                else:
                    #prints an error message if the filename DOES NOT exist 
                    print("ERROR!! File not found. Let's try again...")
                    #prompts the user for the name of the file again 
                    filename = input("Give me a file name with extension (q:quit): ")
                    
            except NameError:
                #prints an error message if the filename DOES NOT exist 
                print("ERROR!! File not found. Let's try again...")
                #prompts the user for the name of the file again 
                filename = input("Give me a file name with extension (q:quit): ")
main()