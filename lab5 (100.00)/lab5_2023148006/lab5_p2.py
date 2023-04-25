# vowels in english
vowels = ['A', 'a', 'I', 'i', 'U', 'u', 'E', 'e', 'O', 'o']

# counter variable
cnt = 0
# input
inp = input("Enter a sentence: ")
# iterate through string, increment counter if inp[i] is a vowel e.g. inp[i] is in vowels
for i in range(len(inp)):
    if inp[i] in vowels:
        cnt += 1

# inline if to differentiate between plural and singular
print(f"Your sentence contains {cnt} vowel" + ("s." if cnt != 1 else "."))
