class Solution:
	def find_strength(self, password):
		vowels = {'a', 'e', 'i', 'o', 'u'}
		count = 0

		v_found, c_found = False, False
		for p in password:
			if p in vowels:
				c_found = True
			else:
				v_found = True
			if v_found and c_found:
				count += 1
				v_found, c_found = False, False
		return count

if __name__ == "__main__":
	password1 = "thisisbeautiful"
	password2 = "hackerrank"
	password3 = "aeiou"
	solution = Solution()
	print(solution.find_strength(password1))
	print(solution.find_strength(password2))
	print(solution.find_strength(password3))
