def longestSubstring(s):
    start = 0
    maxLenght= 0
    map = {}
    for i in range(len(s)):
        if s[i] in map and  map[s[i]] >= start:
            # Increment start value
            start = map[s[i]]+1
        else:
            # find the max
            maxLenght = max(maxLenght, i-start+1)

        map[s[i]] = i
        print ("i>>", i)
        print ("start->>", start)
        print ("s[i] ->>", s[i])
        print ("map[s[i]] ->>", map[s[i]])
        print (map)
        print ("maxLenght>>", maxLenght)
        print()

    return maxLenght

    
print (longestSubstring("abcdabc"))