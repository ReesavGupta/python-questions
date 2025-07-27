from collections import Counter
import re

class TextAnalyzer:
    def __init__(self, text):
        """
        Initialize with text to analyze
        Args:
            text (str): Text to analyze
        """
        self.original_text = text
        self.text = text.lower()

    def get_character_frequency(self, include_spaces=False):
        """
        Get frequency of each character
        Args:
            include_spaces (bool): Whether to include spaces in count
        Returns:
            Counter: Character frequencies
        """
        if not include_spaces:
            filtered_text = self.text.replace(" ", "")
        else:
            filtered_text = self.text
        return Counter(filtered_text)

    def get_word_frequency(self, min_length=1):
        """
        Get frequency of each word (minimum length filter)
        Args:
            min_length (int): Minimum word length to include
        Returns:
            Counter: Word frequencies
        """
        words = re.findall(r'\b\w+\b', self.text)
        filtered_words = [word for word in words if len(word) >= min_length]
        return Counter(filtered_words)

    def get_sentence_length_distribution(self):
        """
        Analyze sentence lengths (in words)
        Returns:
            dict: Contains 'lengths' (Counter), 'average', 'longest', 'shortest'
        """
        sentences = re.split(r'[.!?]+', self.original_text.strip())
        lengths = [len(re.findall(r'\b\w+\b', s)) for s in sentences if s.strip()]
        dist = Counter(lengths)
        return {
            "lengths": dist,
            "average": sum(lengths) / len(lengths) if lengths else 0,
            "longest": max(lengths) if lengths else 0,
            "shortest": min(lengths) if lengths else 0
        }

    def find_common_words(self, n=10, exclude_common=True):
        """
        Find most common words, optionally excluding very common English words
        Args:
            n (int): Number of words to return
            exclude_common (bool): Exclude common words like 'the', 'and', etc.
        Returns:
            list: List of tuples (word, count)
        """
        common_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of',
            'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have',
            'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
            'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he',
            'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
        }

        words = re.findall(r'\b\w+\b', self.text)
        if exclude_common:
            words = [w for w in words if w not in common_words]

        return Counter(words).most_common(n)

    def get_reading_statistics(self):
        """
        Get comprehensive reading statistics
        Returns:
            dict: Contains character_count, word_count, sentence_count,
                  average_word_length, reading_time_minutes (assume 200 WPM)
        """
        characters = len(self.text.replace(" ", ""))
        words = re.findall(r'\b\w+\b', self.text)
        sentences = re.split(r'[.!?]+', self.original_text.strip())

        word_count = len(words)
        sentence_count = len([s for s in sentences if s.strip()])
        avg_word_length = sum(len(word) for word in words) / word_count if word_count else 0
        reading_time = word_count / 200  # 200 WPM assumed

        return {
            "character_count": characters,
            "word_count": word_count,
            "sentence_count": sentence_count,
            "average_word_length": avg_word_length,
            "reading_time_minutes": round(reading_time, 2)
        }

    def compare_with_text(self, other_text):
        """
        Compare this text with another text
        Args:
            other_text (str): Text to compare with
        Returns:
            dict: Contains 'common_words', 'similarity_score', 'unique_to_first', 'unique_to_second'
        """
        words1 = set(re.findall(r'\b\w+\b', self.text))
        words2 = set(re.findall(r'\b\w+\b', other_text.lower()))

        common = words1 & words2
        unique1 = words1 - words2
        unique2 = words2 - words1

        jaccard_similarity = len(common) / len(words1 | words2) if words1 | words2 else 0

        return {
            "common_words": list(common),
            "similarity_score": round(jaccard_similarity, 2),
            "unique_to_first": list(unique1),
            "unique_to_second": list(unique2)
        }


sample_text = """
Python is a high-level, interpreted programming language with dynamic semantics.
Its high-level built-in data structures, combined with dynamic typing and dynamic binding,
make it very attractive for Rapid Application Development. Python is simple, easy to learn
syntax emphasizes readability and therefore reduces the cost of program maintenance.
Python supports modules and packages, which encourages program modularity and code reuse.
The Python interpreter and the extensive standard library are available in source or binary
form without charge for all major platforms, and can be freely distributed.
"""

analyzer = TextAnalyzer(sample_text)

print("Character frequency (top 5):", analyzer.get_character_frequency().most_common(5))
print("\nWord frequency (top 5):", analyzer.get_word_frequency().most_common(5))
print("\nCommon words:", analyzer.find_common_words(5))
print("\nReading statistics:", analyzer.get_reading_statistics())

other_text = "Java is a programming language. Java is object-oriented and platform independent."
comparison = analyzer.compare_with_text(other_text)
print("\nComparison results:", comparison)