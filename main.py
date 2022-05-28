# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count

def read_file_content(filename):
    with open(filename) as file:
        story=file.read()
    return story

def count_words():
    text = read_file_content("./story.txt")
    count=dict()
    words=text.split(' ')
    for i in words:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count
print(count_words())
    
    