#Reilly Kurth
#3/18/2025
#program 2

print("Input a sentence with no spaces, but the first letter of each word is uppercase.")
print("Example: StopAndSmellTheRoses")

sentence = input("Enter your sentence: ")

words = []
current_word = ""

for char in sentence:
    if char.isupper() and current_word:
        words.append(current_word)
        current_word = char.lower()
    else:
        current_word += char

if current_word:
    words.append(current_word)

correct_sentence = words[0].capitalize() + " " + " ".join(word.lower() for word in words[1:])

print(correct_sentence)



