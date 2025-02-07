

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

main()


def counting_words():
    with open("books/frankenstein.txt") as f:
        words = [word for line in f for word in line.split()] # Good use of list comprehension
        final_word = str(len(words))
        print(final_word)
         


counting_words()

def spotting_frequencies():
    with open("books/frankenstein.txt") as f:
        text = f.read().lower()

    char_f = {}

    for char in text:
        if char in char_f:
            char_f[char] +=1
        else:
            char_f[char] = 1
    return char_f

final_output = spotting_frequencies()
print(final_output)

def final_report(): # Mock function ignoreeeee
    with open("books/frankenstein.txt") as f:
        text = f.read().lower()

    char_f = {}

    for char in text:
        if char in char_f or char.isalpha():
            char_f[char] +=1
        else:
            char_f[char] = 1
    return char_f

final_output = final_report()
print(final_output)


def final_report():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        text = f.read().lower()

    char_f = {char: text.count(char) for char in set(text) if char.isalpha() or char == " "}
    sorted_chars = dict(sorted(char_f.items(), key=lambda x: x[1], reverse=True))

    return sorted_chars  


char_counts = final_report()


for char_ff, num_o in char_counts.items():
    if char_ff == " ":
        continue
    print(f"The '{char_ff}' character was found {num_o} times")





