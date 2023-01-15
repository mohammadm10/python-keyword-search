#!/usr/bin/env python3
import sys

def addSpaces(lineInput, lineFilter): #add spaces in front and end of each keywords and input line
    i = 0
    while i < len(lineInput):
        lineInput[i] = lineInput[i].rstrip()
        k = len(lineInput[i])+1
        lineInput[i] = lineInput[i].ljust(k)
        lineInput[i] = lineInput[i].rjust(k+1)
        i+=1

    i = 0
    while i < len(lineFilter):
        lineFilter[i] = lineFilter[i].rstrip()
        k = len(lineFilter[i])+1
        lineFilter[i] = lineFilter[i].ljust(k)
        lineFilter[i] = lineFilter[i].rjust(k+1)
        i+=1


def removeSpace(keywordList): #accomodate for extra space in keywords
    i = 0
    while(i < len(keywordList)):
        if(keywordList[i] == "  "):
            keywordList.pop(i)
            i = i-1
        i = i+1


def modifyInput(keywords, input): #make both lists all lower-case so they match properly
    i = 0
    j= 0
    while i < len(keywords):
        keywords[i] = keywords[i].lower()
        i+=1
    while(j < len(input)):
        input[j] = input[j].lower()
        j+=1
        

def findKeyword(keyword, lineFilter):
    i = 0
    while i < len(keyword):
        keyword[i] = keyword[i].rstrip()
        k = len(keyword[i])+1
        keyword[i] = keyword[i].ljust(k)
        keyword[i] = keyword[i].rjust(k+1)
        i+=1
    keyword.remove('  ')
    k = 0
    while(k < len(keyword)):
        j = 0
        while(j < len(lineFilter)):
            x = lineFilter[j].find(keyword[k].lower()) #checks if unwanted word is in both keywors-list and linefilter-list
            if(x != -1):
                keyword.remove(keyword[k]) #if word is in both lists, remove it
                k-=1
                break
            j+=1
        k+=1

def countOccurences(input, keyword): #reference to codespeedy.com
    found = 0
    x = 0
    while(1):
        x = input.find(keyword, x)
        if(x != -1):
            found+=1
            x+=1
        else:
            break
    return found


def printFinal(keywords, originalInput, modifiedInput):
    i = 0
    j = 0
    k = 0
    #First find the longest keywords to be printed, this will help with printing with proper indexing
    maximum = len(keywords[0]) #set first element as max
    while(k < len(keywords)):  
        if(len(keywords[k]) > maximum): #constantly check if the next one is bigger than current
            maximum = len(keywords[k])
        k+=1
    maximum = maximum-1  #subtract to account for spaces from each side of word

    while(i < len(originalInput)):
        while(j < len(keywords)):
            lineNum = i + 1 #holds line number of current index 
            found = countOccurences(modifiedInput[i], keywords[j]) #checks number of occurences of each keyword in each line
            if(found == 0): #if keywords is not found in current input, check the next
                i+=1
            if(found > 1): #if keyword is found more than once in the input line
                print(keywords[j].upper().strip().ljust(maximum), originalInput[i].strip(), '('+str(lineNum)+'*)')
                j+=found
                if(j != len(keywords)):
                    if(keywords[j] == keywords[j-1]):
                        i+=1 #checks if current keyword is same as before and increments i if true, else start at beginning
                    else:
                        i = 0         
            if(found == 1): #if keyword is only found once in the input line
                print(keywords[j].upper().strip().ljust(maximum), originalInput[i].strip(), '('+str(lineNum)+')')
                j+=1
                if(j != len(keywords)):
                    if(keywords[j] == keywords[j-1]):
                        i+=1 #checks if current keyword is same as before and increments i if true, else start at beginning
                    else:
                        i = 0          
            if(i == len(originalInput)):
                i = 0
            if(j == len(keywords)):
                i = len(originalInput)+1 #checks if it's gone through all keyword, if true break the while


def main():
    
    #file decleration/scanning
    flag = '-e'
    if(len(sys.argv) == 4):
        if(flag == sys.argv[1]): #if the input starts with '-e' then filter is inputted second
            filterIndex = 2
            inputIndex = 3

        if(flag == sys.argv[2]): #if the input doesn't start with '-e' then then filter is inputted last
            inputIndex = 1
            filterIndex = 3

        scanFilter = sys.argv[filterIndex]
        scanInput = sys.argv[inputIndex]

        lf = open(scanFilter)
        lineFilter = lf.readlines() #read filter file into list

        li = open(scanInput)
        lineInput = li.readlines() #read input file into list

    else: #if there is not filter file
        inputIndex = 1
        lineFilter = []
        scanInput = sys.argv[inputIndex]
        li = open(scanInput)
        lineInput = li.readlines() #read input file into list

    keywordList = list() #list/variable declerations
    lowerList = list()   #to be used in main
    i = 0

    #add space between either side of input inorder to differentiate keywords & non-keywords
    #Ex. test 10 had "ab" as a keyword but it appeard in unwanted words such as "habe", this accounts for these cases
    addSpaces(lineInput, lineFilter) 
    
    while i < len(lineInput):
        tempInput = lineInput[i].split(" ")
        tempInput.remove('')
        findKeyword(tempInput, lineFilter) #find the keywords
        keywordList.extend(tempInput) #store found keywords into keywordslist
        i+=1
    
    removeSpace(keywordList) #removes extra space in the first keywords due to the addSpaces function
             
    lowerList = lineInput.copy() #this list will hold the input with all lowercase letters

    modifyInput(keywordList, lowerList) #switch to lowercase

    keywordList.sort() #sort the keywords in alphabetical 

    if(len(keywordList)!=0): #checks if there actually is an input
        printFinal(keywordList, lineInput, lowerList) #prints final output with keyword, sentence, line Number and proper indexing
        

if __name__ == "__main__":
        main()