punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", "#", "@", "\n"]

def strip_punctuation(s):
    for item in punctuation_chars:
        s = s.replace(item, "")
    return s

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ";" and lin[0] != "\n":
            positive_words.append(lin.strip())

def get_pos(s):
    words = s.split(" ")
    count = sum(1 for word in words if strip_punctuation(word).lower() in positive_words)
    return count

negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ";" and lin[0] != "\n":
            negative_words.append(lin.strip())

def get_neg(s):
    words = s.split(" ")
    count = sum(1 for word in words if strip_punctuation(word).lower() in negative_words)
    return count  
print("Enter a tweet: ")
tweet = input()

p = get_pos(tweet)
n = get_neg(tweet)

print("Tweet:", tweet, "\nPositive words:", p, "\nNegative words:", n, "\nOverall:", p - n)
