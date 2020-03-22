#
# [620] Not Boring Movies
#
# https://leetcode.com/problems/not-boring-movies/description/
#
# database
# Easy (59.51%)
# Total Accepted:    21.7K
# Total Submissions: 36.5K
# Testcase Example:  '{"headers":{"cinema":["id", "movie", "description", "rating"]},"rows":{"cinema":[[1, "War", "great 3D", 8.9], [2, "Science", "fiction", 8.5], [3, "irish", "boring", 6.2], [4, "Ice song", "Fantacy", 8.6], [5, "House card", "Interesting", 9.1]]}}'
#
# X city opened a new cinema, many people would like to go to this cinema.
# The cinema also gives out a poster indicating the movies’ ratings and
# descriptions. 
# ⁠
# Please write a SQL query to output movies with an odd numbered ID and a
# description that is not 'boring'. Order the result by rating.
# 
# 
# For example, table cinema:
# 
# +---------+-----------+--------------+-----------+
# |   id    | movie     |  description |  rating   |
# +---------+-----------+--------------+-----------+
# |   1     | War       |   great 3D   |   8.9     |
# |   2     | Science   |   fiction    |   8.5     |
# |   3     | irish     |   boring     |   6.2     |
# |   4     | Ice song  |   Fantacy    |   8.6     |
# |   5     | House card|   Interesting|   9.1     |
# +---------+-----------+--------------+-----------+
# 
# For the example above, the output should be:
# 
# +---------+-----------+--------------+-----------+
# |   id    | movie     |  description |  rating   |
# +---------+-----------+--------------+-----------+
# |   5     | House card|   Interesting|   9.1     |
# |   1     | War       |   great 3D   |   8.9     |
# +---------+-----------+--------------+-----------+
# 
# 
#
SELECT * FROM cinema WHERE (id % 2 = 1) AND (description <> 'boring') ORDER BY rating DESC
