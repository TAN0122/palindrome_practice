"""
409. Longest Palindrome

Given a string text which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

For this question, letters are case-sensitive, for example, "Aa" is not considered a palindrome.
"""


def longest_palindrome_length(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    length = 0
    has_odd = False

    for count in char_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            has_odd = True

    if has_odd:
        length += 1

    return length


if __name__ == '__main__':
    test_cases = [('abccccdd', 7),      # dccaccd / dccbccd
                  ('a', 1),             # a
                  ('school', 3)]        # oso / oco / oho / olo

    for test_text, expected in test_cases:
        result = longest_palindrome_length(test_text)
        msg = 'Correct' if expected == result else 'Wrong'
        print(f'[{msg:7s}] longest_palindrome_length("{test_text}") should be {expected}')
