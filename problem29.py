# number of distinct powers a^b | a,b are integers from 2 to 100
print(len(set(a**b for a in range(2,101) for b in range(2,101))))