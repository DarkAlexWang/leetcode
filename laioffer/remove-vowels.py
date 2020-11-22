class Solution:
    def remove_vowels(self, string):
        vowels = ('a', 'e', 'i', 'o', 'u')
        for x in string.lower():
            if x in vowels:
                string = string.replace(x, '')
