def longest_sub_string(input_str:str):
    l = 0
    res = 0
    charSet = set()
    for r in range(len(input_str)):
        while input_str[r] in charSet:
            charSet.remove(input_str[l])
            l += 1
        charSet.add(input_str[r])
        res = max(res, r-l+1)
    return res

if __name__ == "__main__":
    print(longest_sub_string("abcdefababcdefghijka"))
    