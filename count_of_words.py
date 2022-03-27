#Define the method to get the count of words from a string
def word_count(str):
    counts = {}
    words = str.split()
    
    for word in words:
        word=word.replace(',','')
        word=word.replace('.','')
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

#Input
print("Enter the file name if running from the same directory or Enter the full path to the file.")
path_to_file=input()
with open(path_to_file,mode='r') as f:
    doc=f.read().rstrip('\n')

#Output
result = word_count((str(doc)))
result_rearranged = dict(sorted(result.items(), key=lambda i: i[1], reverse=True))
print("The count of words is as follows \n")
for i in result_rearranged:
        print(i,':',result_rearranged[i])