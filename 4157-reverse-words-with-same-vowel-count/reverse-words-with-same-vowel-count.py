# # class Solution(object):
# #     def reverseWords(self, s):
# #         """
# #         :type s: str
# #         :rtype: str
# #         """
# #         vowels = {'a', 'e', 'i', 'o', 'u'}
        
# #         # Helper function to count vowels in a word
# #         def get_vowel_count(word):
# #             return sum(1 for char in word if char in vowels)
        
# #         # Split the string into individual words
# #         words = s.split(' ')
        
# #         # Determine the target vowel count from the first word
# #         target_count = get_vowel_count(words[0])
        
# #         # Process each word
# #         for i in range(len(words)):
# #             if get_vowel_count(words[i]) == target_count:
# #                 words[i] = words[i][::-1]  # Reverse the word
                
# #         # Rejoin the words with a single space
# #         return " ".join(words)


# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         vowels = {'a', 'e', 'i', 'o', 'u'}
        
#         # Helper function to count vowels in a word
#         def get_vowel_count(word):
#             return sum(1 for char in word if char in vowels)
        
#         # Split the string by spaces while preserving empty strings from consecutive spaces
#         words = s.split(' ')
        
#         # Find the first non-empty word to determine the target vowel count
#         target_count = 0
#         for word in words:
#             if word:  # Found the first actual word
#                 target_count = get_vowel_count(word)
#                 break
        
#         # Process each word
#         for i in range(len(words)):
#             # Only process actual words (skip empty strings from consecutive spaces)
#             if words[i] and get_vowel_count(words[i]) == target_count:
#                 words[i] = words[i][::-1]
                
#         # Rejoin using the exact single space delimiter
#         return " ".join(words)


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        def get_vowel_count(word):
            return sum(1 for char in word if char in vowels)

        # Split into words (keeps any extra spacing intact if needed, 
        # or standard split if it's single-space separated)
        words = s.split(' ')
        
        # Find the index and vowel count of the first non-empty word
        target_count = None
        first_word_idx = -1
        
        for i, word in enumerate(words):
            if word:
                target_count = get_vowel_count(word)
                first_word_idx = i
                break
                
        # If no valid word is found, return the original string
        if target_count is None:
            return s

        # Process each word
        for i in range(len(words)):
            # Skip the first reference word itself, and skip empty spacing strings
            if i == first_word_idx or not words[i]:
                continue
                
            # Reverse only if it matches the target vowel count
            if get_vowel_count(words[i]) == target_count:
                words[i] = words[i][::-1]

        return " ".join(words)