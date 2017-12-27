def duplicates(passphrase):
    passphrase_list = passphrase.split(" ")
    if len(passphrase_list) != len(set(passphrase_list)):
        return True
    return False


def palindromes(passphrase):
    p_list = passphrase.split(" ")
    sorted_words = []
    for word in p_list:
        sorted_words.append(''.join(sorted(word)))

    if len(sorted_words) != len(set(sorted_words)):
        return True
    return False


if __name__ == '__main__':
    file = open('day4.txt', 'r')
    text = file.read()

    good_phrases = 0
    for passphrase in text.split('\n'):
        if not palindromes(passphrase):
            good_phrases += 1

    print(good_phrases)
