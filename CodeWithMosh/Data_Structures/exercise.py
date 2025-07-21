"""find the letter with the highest occurence in this sentence string"""

sentence = "This is a common interview question"

letters = [*sentence]
max_count = 0
highest_letter = ""
for i, letter_i in enumerate(letters):
    current_count = 0
    for j, letter_j in enumerate(letters):
        if letter_i == letter_j:
            current_count += 1

    if current_count > max_count:
        max_count = current_count
        highest_letter = letter_i
print(f"the letter with the highest occurrence is '{highest_letter}' with a total of {max_count} occurences")


char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequency_sorted[0][0])