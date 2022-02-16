#
# @lc app=leetcode id=1152 lang=python3
#
# [1152] Analyze User Website Visit Pattern
#

# @lc code=start
from collections import defaultdict
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        packed_tuple = zip(timestamp, username, website)
        sorted_packed_tuple = sorted(packed_tuple)

        mapping = defaultdict(list)
        for t, u, w in sorted_packed_tuple:
            mapping[u].append(w)

        counter_dict = defaultdict(int)
        for website_list in mapping.values():
            combs = set(combinations(website_list, 3))
            for comb in combs:
                counter_dict[comb] += 1
        sorted_counter_dict = sorted(counter_dict, key=lambda x:(-counter_dict[x], x))
        return sorted_counter_dict[0]

        """
        packed_tuple = zip(timestamp, username, website)   # ---> [(3, 'joe', 'career'),....]
        sorted_packed_tuple = sorted(packed_tuple)  # sort by timestamp, as it didn't say timestamp is sorted array
                                                    # By default tuple always being sorted by the first item

        mapping = defaultdict(list)
        for t, u, w in sorted_packed_tuple: # joe: ['home', 'about', 'career']  websites in list are in ascending timestamp order
            mapping[u].append(w)

        counter_dict = defaultdict(int)         # use a dict for counting
        for website_list in mapping.values():
            combs = set(combinations(website_list, 3))    # size of combination is set to 3, for details see bottom
            for comb in combs:
                counter_dict[comb] += 1       # Tuple as key, counter as value,  e.g. ('home', 'about', 'career') : 2

        sorted_counter_dict = sorted(counter_dict, key=lambda x: (-counter_dict[x], x)) # sort descending by value, then lexicographically
        return sorted_counter_dict[0]
		"""
# @lc code=end
