

def count_characters(s):
    return len(s)

def count_words(s):
    return len(s.split())

def average_word_length(s):
    words = s.split()
    return sum(len(word) for word in words) / len(words) if words else 0

if __name__ == "__main__":
    sample = "Hello world"
    print("Characters:", count_characters(sample))
    print("Words:", count_words(sample))
    print("Average word length:", average_word_length(sample))
