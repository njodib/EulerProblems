'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3+15+12+9+14=53 is the 938th name in the list. So COLIN obtains a score of 938x53=49714
What is the total of all the name scores in the file?
'''
import requests

def name_score(name):
    return sum(ord(c)-ord('A')+1 for c in name)

file_url = 'https://projecteuler.net/resources/documents/0022_names.txt'
names = requests.get(file_url).text.split(",")
names = sorted(name.strip('"') for name in names)
s = sum(i*name_score(name) for i, name in enumerate(names,1))
print("total name score:", s)