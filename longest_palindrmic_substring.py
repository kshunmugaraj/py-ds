def longest_palindromic_substring(inputStr:str)->str:
    r,l = 0,0
    longPalString = ""
    longPalStrLen = 0
    
    for i in range(len(inputStr)):
        #odd length
        l, r = i,i
        while l >= 0 and r < len(inputStr) and inputStr[l] == inputStr[r]:
            if (r - l + 1) > longPalStrLen:
                longPalString = inputStr[l : r+1]
                longPalStrLen = r - l + 1
            l -= 1
            r +=1
        
        l, r = i , i+1
        while l >=0 and r < len(inputStr) and inputStr[l] == inputStr[r]:
            if (r-1+1) > longPalStrLen:
                longPalString = inputStr[l:r+1]
                longPalStrLen = r-1+1
            l -=1
            r +=1
    return longPalString


if __name__ == "__main__":
    print(longest_palindromic_substring("abccba"))
        