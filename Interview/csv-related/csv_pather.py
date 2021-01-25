from csv import DictReader
class Solution:
    def csvPather(self, PathInfo):
        f = open('dataset3.csv', f)
        d = DictReader(f)
        data = []
        for row in d:
            data.append(row)

        print(data[0]['Country'])
        print(data[2]['Email'])
