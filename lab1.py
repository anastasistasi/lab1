
def sort_by_length(words):
  return sorted(words, key=len)
def create_word_dict(filename):
  word_dict = {}
  with open(filename, "r") as file:
    for line in file:
      words = line.strip().split()
      for word in words:
        word = word.lower()
        if word in word_dict:
          word_dict[word] += 1
        else:
          word_dict[word] = 1
  return word_dict

filename = "textlab1"
filename = "textlab1_2"
word_dict = create_word_dict(filename)
words = word_dict
sorted_words = sort_by_length(words)
print(sorted_words)