newStr = "12/22/2018  12:55:56 PM"
newStr = newStr[12:-3]
ftr = [3600,60,1]

x = sum([a*b for a,b in zip(ftr, map(int,newStr.split(':')))])

print(newStr, x)