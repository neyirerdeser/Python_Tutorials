def get_words():
    return input('sentence: ')


word_list = get_words().split()  # ' ' indicates a single space, no argument means white space

rev_sentence = ' '.join(word_list[::-1])
print(rev_sentence)