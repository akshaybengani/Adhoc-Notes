# Use Google liberary to fetch data from google
from googlesearch import search

searchString = input("Enter the search item ")

f = open("URL"+searchString,'w')

for i in search(searchString,stop=10):
    f.write(i)
    f.write("\n")
    print("Url is ",i)
f.close()




