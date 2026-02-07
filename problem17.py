# Number Letter Counts
# one two three four five = 19 letters
# How many letters in "one two ... one thousand"
# Do not count spaces or hyphens
# e.g. 342 = three hundred and forty-two = 23 letters
# e.g. 115 = one hundred and fifteen = 20 letters

def count_letters(n):
    if n >= 1000:
        return len("onethousand")
    count = 0
    if n >= 100:
        count += len(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][n//100-1])
        count += len("hundred")
        if n%100 > 0:
            count += len("and")
    n = n%100
    if n >= 20:
        count += len(["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][n//10-2])
        n = n%10
    if n > 0:
        count += len(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                      "ten", "eleven", "twelve", "thirteen", "fourteen",
                      "fifteen", "sixteen", "seventeen", "eighteen",
                      "nineteen"][n-1])
    return count

print("COUNT LETTERS 1->5:",sum(count_letters(i) for i in range(1, 6)))
print("COUNT LETTERS 115:",count_letters(115))
print("COUNT LETTERS 342:",count_letters(342))
print("COUNT LETTERS 1->1000:",sum(count_letters(i) for i in range(1, 1001)))