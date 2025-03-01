import os
import collections
import socket

# Ensure file paths match correct names
file1_path = "/home/data/IF.txt"  # Previously IF-1.txt
file2_path = "/home/data/AlwaysRememberUsThisWay.txt"  # Previously AlwaysRememberUsThisWay-1.txt
output_path = "/home/data/output/result.txt"

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Function to read file and count words
def count_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            words = file.read().lower().split()
            return collections.Counter(words)
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return collections.Counter()

# Function to expand contractions
def expand_contractions(text):
    contractions = {
        "I'm": "I am",
        "can't": "cannot",
        "don't": "do not",
        "it's": "it is",
        "you're": "you are",
        "they're": "they are",
        "I've": "I have",
        "isn't": "is not"
    }
    for contraction, full_form in contractions.items():
        text = text.replace(contraction.lower(), full_form.lower())
    return text

# Process both files
counts1 = count_words(file1_path)  # Count words in IF.txt
counts2 = count_words(file2_path)  # Count words in AlwaysRememberUsThisWay.txt

# Grand total word count
total_words_file1 = sum(counts1.values())
total_words_file2 = sum(counts2.values())
grand_total = total_words_file1 + total_words_file2

# Top 3 most frequent words in IF.txt
top_3_file1 = counts1.most_common(3)

# Expand contractions and re-count words in AlwaysRememberUsThisWay.txt
with open(file2_path, 'r', encoding='utf-8') as file:
    expanded_text = expand_contractions(file.read().lower())
    counts2 = collections.Counter(expanded_text.split())

# Top 3 most frequent words in AlwaysRememberUsThisWay.txt after expanding contractions
top_3_file2 = counts2.most_common(3)

# Get container's IP Address
ip_address = socket.gethostbyname(socket.gethostname())

# Prepare the output results
output = f"""
Total words in IF.txt: {total_words_file1}
Total words in AlwaysRememberUsThisWay.txt: {total_words_file2}
Grand total words: {grand_total}

Top 3 words in IF.txt:
{top_3_file1}

Top 3 words in AlwaysRememberUsThisWay.txt (after handling contractions):
{top_3_file2}

Machine IP Address: {ip_address}
"""

# Write results to /home/data/output/result.txt
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(output)

# Print results to console before exiting
print(output)
