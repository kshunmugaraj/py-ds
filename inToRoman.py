def intToRoman(number:int)->str:
    symList = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000],
        ]
    res = ""    
    for sym, val in reversed(symList):
        if number // val:
            count = number // val
            res += sym*count
            number = number % val
    return res