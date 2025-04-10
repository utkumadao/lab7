def count_characters(s):
    return len(s)

def count_words(s):
    words = s.split()
    return len(words)

def average_word_length(s):
    words = s.split()
    if not words:
        return 0
    sum_word = sum(len(word) for word in words)
    return sum_word / len(words)
