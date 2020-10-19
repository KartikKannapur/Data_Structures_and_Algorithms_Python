"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.


Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        """
        Method 1:

        Your runtime beats 49.89 % of python3 submissions.
        """

        def canMatchPattern(word, pattern):
            """
            Method same as function in Q290
            """
            d = {}
            for index, letter in enumerate(word):
                if letter in d:
                    if d[letter] != pattern[index]:
                        return False
                elif pattern[index] in d.values():
                    return False
                else:
                    d[letter] = pattern[index]

            return True

        res = []
        for word in words:
            if canMatchPattern(word, pattern):
                res.append(word)

        return res