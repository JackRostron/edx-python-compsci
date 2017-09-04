'''
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
'''

s = "bobobobboobobobobwobooboboboobvgbobobboboobobooh"

match_string = "bob"
match_count = 0
x = 0

for x in range(0, len(s)):
	subString = s[x:(x + 3)]
	if subString.count(match_string):
		match_count += 1
	x += 1

print(match_count)