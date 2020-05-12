#stringtype.py
#string on one line
s="   You are awesome   "
print(s)

#string across lines
s1="""You are 
the creator
of your destiny"""
print (s1)

#indexing to get to first character
print(s[0])

#indexing to get to another a character, just use the number that character is in the string
#u is 2
#a is 4
print(s[2])
print(s[4])

#repetition: repeat the string twice
print(s*2)

#length
print(len(s1))
print(len(s))

#slicing - starts with index 0 to 4 0:5
print(s[0:5])

#slicing - start to finish
print(s[0:])

#slicing - start at 0 end before 8
print(s[:8])

#slicing - negative numbers starts from end of string
print(s[-3:-1])

#step value - if you change to 2, it will give alternate characters. 1 is default step value
print(s[0:9:2])

#step value - using negatives, reverses the string. Both commands will produce the same.
print(s[15::-1])
print(s[::-1])

#strip function - add spaces in the string and then use strip to remove the spaces. lstrip and rstrip will let you remove spaces from one side or the other
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#find - find a where a substring begins
print(s.find("awe"))

#find - find but stop at a specific place. returns -1 when it can't be found
print(s.find("awe"),0,len(s))
print(s.find("awe",0,8))

#count - counts the number of occurances of a given substring
print(s.count("a"))

#replace - replace one string with another. 1st word is the current string, 2nd word is the new string
print(s.replace("awesome", "super"))

#upper - displays string in upper case
print(s.upper())

#lower
print(s.lower())

#Title
print(s.title())