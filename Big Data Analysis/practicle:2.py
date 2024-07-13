countOfWords = len("Geeksforgeeks is best Computer Science Portal".split())
print("Count of Words in the given Sentence:", countOfWords)

print(len("Soham Soni is a student of parul university".split()))

print(len(input("Enter Input:").split()))

from collections import Counter

def word_count(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    
    words = text.split()
    
    word_counts = Counter(words)
    
    for word, count in word_counts.items():
        print(f"{word}: {count}")
    
    total_words = sum(word_counts.values())
    print(f"\nTotal words: {total_words}")

file_path = r"C:\Users\sonis\OneDrive\Desktop\soham.txt"

word_count(file_path)


import urllib.request
from collections import Counter

# URL of the text file
story_url = 'https://sixty-north.com/c/t.txt'

# Fetch the text from the URL
with urllib.request.urlopen(story_url) as response:
    story_text = response.read().decode('utf-8')

# Split the text into words and convert them to lowercase
words = story_text.lower().split()

# Count the occurrences of each word
word_counts = Counter(words)

# Print the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")

# Calculate total words
total_words = sum(word_counts.values())
print(f"\nTotal words: {total_words}")
