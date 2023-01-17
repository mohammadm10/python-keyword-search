# python-keyword-search

This is a python script that takes in two text files:
- The input text, which is a series of sentences
- The excluded words (non-keyword strings)

The output is the keyword, which is any word in the input that is not in the excluded list, along with the sentence that the keyword was found in and the line number to which the keyword was found in
To run the script: ./kwoc2.py -e [exlcuded list] [input]

Ex: ./kwoc2.py -e english.txt in05.tx
