words_object = open("words.txt", "r")
contents = words_object.read()

contents = contents.replace("\"", "")
contents = contents.replace(",", " ")
words = contents.split(" ")


def check_triangle(num):
    pos = 1
    increment = 2
    while pos < num:
        pos += increment
        increment += 1
    if pos == num:
        return True
    return False


letter_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
                 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
                 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
                 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

triangle_word_count = 0
print(words)
for word in words:
    total = 0
    for letter in word:
        total += letter_values[letter]
    if check_triangle(total):
        triangle_word_count += 1
        print(word)
    print(total)

print(triangle_word_count)