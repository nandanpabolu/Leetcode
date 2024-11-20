class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        words = sentence.split()
        result = []

        for i, word in enumerate(words):
            if word[0] in vowels:
                # Word starts with a vowel
                goat_word = word + "ma"
            else:
                # Word starts with a consonant
                goat_word = word[1:] + word[0] + "ma"
            
            # Append "a" based on the index
            goat_word += "a" * (i + 1)
            result.append(goat_word)
        
        return ' '.join(result)
