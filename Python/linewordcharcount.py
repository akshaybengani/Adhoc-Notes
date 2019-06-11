filename = input("Please Enter a file name ")
myfile=open(filename)

lineCount = 0
wordCount = 0
charCount = 0
for lines in myfile:
    lineCount = lineCount + 1
    wordCount = wordCount + len(lines.split())
    charCount = charCount + len(lines)

print("No of Lines      :   ",lineCount)
print("No of Words      :   ",wordCount)
print("No of Characters :   ",charCount)