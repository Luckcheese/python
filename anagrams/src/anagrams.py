def remove_letter(word, i):
    return word[i], word[0:i] + word[i + 1:]


def break_word(prefix, word):
    if len(word) > 0:
        fish_letters = [remove_letter(word, i) for i in range(len(word))]
        return " ".join([break_word(prefix + p, r) for p, r in fish_letters])
    else:
        return prefix


def anagram(word):
    return break_word("", word)

print anagram("sadness")