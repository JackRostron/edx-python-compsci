
################################################################################
################################################################################

print("\nPROBLEM SET #1")
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

s = "aioepoapoeapioeioae"
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0

for char in s:
    if char in vowels:
        vowel_count += 1

print("Number of vowels: " + str(vowel_count))


################################################################################
################################################################################

print("\nPROBLEM SET #2")
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

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


################################################################################
################################################################################

print("\nPROBLEM SET #3")
# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

s = "azcbobobegghakl"               # beggh
# s = "mtdlggfweevgyqdcwsx"           # eev
# s = "gbnmtzupfdlvudokdymfnhuv"      # atz
# s = "mcwskpxrajqykuxhwfvedfk"       # ajqy
# s = "mlkesybfb"                     # esy
# s = "mkjlrihwzmjzvwl"               # jlr
# s = "qsyltcgwwpjestttqulxdpi"       # esttt
# s = "ditjkcbpjpmbdvjud"             # dit
# s = "abcdefghijklmnopqrstuvwxyz"    # abcdefghijklmnopqrstuvwxyz
# s = "mevrpuwmokxqxqnrchl"           # puw
# s = "djydsumvhzprb"                 # djy
# s = "ejasbeveq"                     # bev
# s = "zyxwvutsrqponmlkjihgfedcba"    # z
# s = "yzlxgczaxebkoxuaglt"           # bkox
# s = "nsrjmhlp"                      # hlp
# s = "qiaupeqktfvxnpgjnjptieix"      # fvx
# s = "yzobxrptwszneqkoliyrv"         # ptw
# s = "tpwgfnfjdhcaqbvpfoh"           # pw
# s = "hawodjzfjzhtvwtgw"             # htvw
# s = "ngmjfhbwupusslctwjdgc"         # ctw
# s = "trvlmguddvzvfkywhcygsppw"      # ddvz

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]

iteration = 0
current_phrase = ""
longest_phrase = ""

check_length = len(s)

while iteration < check_length:

    if len(current_phrase) > len(longest_phrase):
        longest_phrase = current_phrase

    starting_letter = s[iteration]
    starting_letter_index = alphabet.index(starting_letter)

    # Make a current phrase with the starting letter
    current_phrase = starting_letter

    # We aren't out of bounds, keep going
    if (iteration + 1) < check_length:

        last_letter = starting_letter
        last_letter_index = starting_letter_index

        # Iterate over the remaining letters until we bail
        for x in range(iteration + 1, check_length):
            next_letter = s[x]
            next_index = alphabet.index(next_letter)
            if next_index >= last_letter_index:
                current_phrase = current_phrase + next_letter

                # Assign our values for the next loop
                last_letter = next_letter
                last_letter_index = next_index

                iteration = x
            else:
                # Assign our current phrase, reposition the index and go again
                if len(current_phrase) > len(longest_phrase):
                    longest_phrase = current_phrase
                    # print("New longest phrase: " + longestPhrase)

                iteration = x
                # print("Done: " + currentPhrase)
                break
    else:
        iteration = check_length

        # print("Running " + str(iteration) + " " + str(checkLength))
        break

print("Longest substring in alphabetical order is: " + longest_phrase)