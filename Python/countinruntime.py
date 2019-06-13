wordCount = 0
lineCount = 0
charCount = 0

print("Enter input \nType 'done' to end\n")

while True:
    line = input()
    if line=='done':
        break
    else:
        lineCount = lineCount + 1
        wordCount = wordCount + len(line.split())
        charCount = charCount + len(line)    

print("Number of lines      :   ",lineCount)
print("Number of Words      :   ",wordCount)
print("Number of Chars      :   ",charCount)
