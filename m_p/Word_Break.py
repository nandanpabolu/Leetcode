class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = collections.deque([s])
        visited = set()

        while queue:
            word = queue.popleft()

            if word in visited:
                continue
            else:
                if not word:
                    return True
                
                visited.add(word)
                
                for start_word in wordDict:
                    if word.startswith(start_word):
                        queue.append(word[len(start_word):])
        return False