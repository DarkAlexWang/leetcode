##Many software applications require a sense of time. In Unix, time is
#represented as the number of milliseconds since a particular reference point
#called the Epoch (January 1, 12:00AM, 1970), when milliseconds = 0. Create a
#class called “Date” which is initialized with single parameter: milliseconds.
#Then add the ability for this Date class to return the Month.
#
class Solution:
    def monthcal(self, mill):
        sec = mill / 1000
        minutes = sec / 60
        hour = minutes / 60
        date = hour / 24
        date_year = date % 365
        dic = {1: 31, 2: 28, 3: 31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        for i in range(12):
            month = date_year - dic[i]
            if month < 28:
                return
        return month + 1
