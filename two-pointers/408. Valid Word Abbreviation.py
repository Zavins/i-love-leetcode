# type: ignore

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit() and abbr[j] != "0":
                k = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                i += int(abbr[k: j])
                continue

            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1

        return i == len(word) and j == len(abbr)