"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

import string


def isPalindrome(s: str) -> bool:
    s = s.replace(" ", "")
    s = s.translate(str.maketrans('', '', string.punctuation))
    print(s)
    for i in range(len(s)):
        if s[i].lower() != s[-i - 1].lower():
            return False
    return True
