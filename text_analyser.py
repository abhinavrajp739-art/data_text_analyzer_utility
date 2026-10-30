"""
Python Data & Text Analyzer Utility
Created by: Abhinav Raj P

This utility script demonstrates basic string handling, mathematical operations,
and dictionary/list manipulations common in data preprocessing and logical tasks.
"""

def analyze_text(input_string):
    """Analyzes text for word count, character count, and unique words."""
    if not input_string or not isinstance(input_string, str):
        print("Error: Please provide a valid, non-empty text string.")
        return

    print("\n--- TEXT ANALYSIS RESULTS ---")
    
    # 1. Basic Counts
    total_characters = len(input_string)
    words = input_string.split()
    total_words = len(words)
    
    print(f"Original Text: '{input_string}'")
    print(f"Total Characters: {total_characters}")
    print(f"Total Words: {total_words}")

    # 2. Logic: Identify Long Words ( > 8 characters)
    long_words = [word for word in words if len(word) > 8]
    print(f"Long Words (> 8 chars): {long_words if long_words else 'None found'}")

    # 3. Frequency Count using Dictionary
    word_frequencies = {}
    for word in words:
        clean_word = word.lower().strip('.,!?()')
        word_frequencies[clean_word] = word_frequencies.get(clean_word, 0) + 1
    
    sorted_frequencies = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)
    print("\nWord Frequencies (sorted):")
    for word, freq in sorted_frequencies[:5]:
        print(f"  '{word}': {freq}")

sample_paragraph = "Artificial Intelligence often requires strong logical reasoning and data handling skills."
analyze_text(sample_paragraph)
