##Many software applications require a sense of time. In Unix, time is
#represented as the number of milliseconds since a particular reference point
#called the Epoch (January 1, 12:00AM, 1970), when milliseconds = 0. Create a
#class called “Date” which is initialized with single parameter: milliseconds.
#Then add the ability for this Date class to return the Month.
# NexKey interview questions.
import time
class milliesecond_to_month:
    #def monthcal(self, mill):
    #    sec = mill / 1000
    #    minutes = sec / 60
    #    hour = minutes / 60
    #    date = hour / 24
    #    date_year = date % 365
    #    dic = {1: 31, 2: 28, 3: 31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    #    for i in range(12):
    #        month = date_year - dic[i]
    #        if month < 28:
    #            return
    #    return month + 1

    millis = int(round(time.time() * 1000))

    def ms_to_month(self, millis):
        days = millis // 86400000
        millisToday = millis % 86400000
        years_passed_approx = days / 365
        days_passed_this_year = days - (years_passed_approx * 365 + self.leap_years_count(years_passed_approx))
        year = years_passed_approx + 1970
        mydate = self.get_monthandday(year, days_passed_this_year)
        hours = millisToday // 3600000
        minutes = (millisToday % 3600000) // 60000
        seconds = (millisToday % 60000) // 1000

        print("Output")
        print("Year: " + year)
        #print("Month: " + month)
        print("Day: " + days_passed_this_year)
        print("Hour: " + hours)
        print("Minutes: " + minutes)
        print("Seconds: " + seconds)

    def get_monthandday(self, year, days_passed_this_year):
        days_left = days_passed_this_year
        leep_year = self.isleepyear(year)
        daysinmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(len(daysinmonth)):
            days = daysinmonth[i]
            if leep_year and i == 1:
                days += 1
            if days <= days_left:
                days_left -= days
            else:
                return
        return mydate(i + 1, days_left + 1)

    def leap_years_count(self, years_passed):
        count = 0
        for i in range(1970, 1970 + int(years_passed)):
            if self.isleapyear(i):
                count += 1
        return count

    def isleapyear(self, year):
        return (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0

if __name__ == "__main__":
    solution = milliesecond_to_month()
    solution.ms_to_month(3242342343242342)
