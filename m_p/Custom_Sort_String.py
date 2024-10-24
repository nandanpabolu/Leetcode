class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_s = Counter(s)

        result = []

        for char in order:
            if char in count_s:
                result.append(char * count_s[char])

                del count_s[char]

        for char, count in count_s.items():
            result.append(char * count)

        return ''.join(result)
