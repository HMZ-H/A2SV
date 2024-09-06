# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

units = ["", "One", "Two", "Three", "Four", "Five", "Six", 
"Seven", "Eight", "Nine"]
tenths = [
    "", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
    "Seventy", "Eighty", "Ninety"
]

# 1 -> 99
def sayTenths(x):
    unit = x % 10
    dec = x // 10

    if x < 10: return units[unit]
    if dec == 1:
        if x == 10: return "Ten"
        if x == 11: return "Eleven"
        if x == 12: return "Twelve"
        if x == 13: return "Thirteen"
        if x == 14: return "Fourteen"
        if x == 15: return "Fifteen"
        if x == 16: return "Sixteen"
        if x == 17: return "Seventeen"
        if x == 18: return "Eighteen"
        if x == 19: return "Nineteen"
        
    if unit > 0:
        return tenths[dec] + " " + units[unit]
    else:
        return tenths[dec]
     

# 100 to 999
def sayHundreds(x):
    if x < 100: return sayTenths(x)
    if x == 0: return ""
    decs = x % 100
    if decs > 0:
        return sayTenths(x // 100) + " Hundred " + sayTenths(decs)
    else:
        return sayTenths(x // 100) + " Hundred"

class Solution:
    # 2,147,483,647
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        n = len(str(num))
        res = []
        if n > 9:
            bi = (num % 1000000000000) // 1000000000
            if bi != 0: 
                res.append(sayTenths( bi ) + " Billion")
        if n > 6:
            thou = (num % 1000000000) // 1000000
            if thou != 0:
                res.append(sayHundreds( thou )  + " Million")
        if n > 3:
            hun = (num % 1000000) // 1000
            if hun != 0: 
                res.append(sayHundreds( hun ) + " Thousand")
        if num % 1000 > 0:
            res.append(sayHundreds(num % 1000))

        return ' '.join(filter(None, res))