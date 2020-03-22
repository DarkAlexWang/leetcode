#
# [595] Big Countries
#
# https://leetcode.com/problems/big-countries/description/
#
# database
# Easy (71.54%)
# Total Accepted:    37.7K
# Total Submissions: 52.7K
# Testcase Example:  '{"headers": {"World": ["name", "continent",\t"area",\t"population", "gdp"]}, "rows": {"World": [["Afghanistan", "Asia", 652230, 25500100, 20343000000], ["Albania", "Europe", 28748, 2831741, 12960000000], ["Algeria", "Africa", 2381741, 37100000, 188681000000], ["Andorra", "Europe", 468, 78115,\t3712000000], ["Angola", "Africa", 1246700, 20609294, 100990000000]]}}'
#
# There is a table World 
# 
# +-----------------+------------+------------+--------------+---------------+
# | name            | continent  | area       | population   | gdp           |
# +-----------------+------------+------------+--------------+---------------+
# | Afghanistan     | Asia       | 652230     | 25500100     | 20343000      |
# | Albania         | Europe     | 28748      | 2831741      | 12960000      |
# | Algeria         | Africa     | 2381741    | 37100000     | 188681000     |
# | Andorra         | Europe     | 468        | 78115        | 3712000       |
# | Angola          | Africa     | 1246700    | 20609294     | 100990000     |
# 
# +-----------------+------------+------------+--------------+---------------+
# 
# 
# A country is big if it has an area of bigger than 3 million square km or a
# population of more than 25 million.
# 
# Write a SQL solution to output big countries' name, population and area.
# 
# 
# For example, according to the above table, we should output:
# 
# +--------------+-------------+--------------+
# | name         | population  | area         |
# +--------------+-------------+--------------+
# | Afghanistan  | 25500100    | 652230       |
# | Algeria      | 37100000    | 2381741      |
# +--------------+-------------+--------------+
# 
# 
#
# Write your MySQL query statement below
SELECT
    name, population, area
FROM
    world
WHERE
    area > 3000000 OR population > 25000000
;
