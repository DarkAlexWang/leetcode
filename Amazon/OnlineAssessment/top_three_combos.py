class Solution:
	def topThreeCombos(self, popularities, k):
		rlt = [-float('inf')] * k

		def dfs(idx, total):
			# if reach leaf node
			if idx == len(popularities):

				if total >= rlt[0]:
					rlt[2] = rlt[1]
					rlt[1] = rlt[0]
					rlt[0] = total
				elif total >= rlt[1]:
					rlt[2] = rlt[1]
					rlt[1] = total
				elif total >= rlt[2]:
					rlt[2] = total

			return

			# don't add current product to the combo
			dfs(idx+1, total)

			# add current product to the combo
			dfs(idx+1, total + popularities[idx])            


		dfs(0, 0)
		# assume always have more than three kinds of combos for similarity
		return rlt

if __name__ == "__main__":
	s = Solution()
	print(s.topThreeCombos([3, 5, -2], 3))
