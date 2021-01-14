class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        elif len(s) == 2:
            return len(set(s))
        else:
            substr = []
            lenght = 0
            for letter in s:
                if letter in substr:
                    substr = substr[substr.index(letter)+1:]
                substr.append(letter)    
                lenght = max(lenght, len(substr))
            return lenght
            
