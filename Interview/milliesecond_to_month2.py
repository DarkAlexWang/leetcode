public class Main  {

    public static class MyDate {
        int month;
        int day;

        public MyDate(int month, int day) {
            this.month = month;
            this.day = day;
        }
    }

    public static final int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    public static void main(String[] args) {
        long millis = System.currentTimeMillis();
        long days = millis / 86400000;
        long millisToday = millis % 86400000;
        int yearsPassedApprox = (int) days / 365;
        int daysPassedThisYear = (int) (days - (yearsPassedApprox * 365 + leapYearsCount(yearsPassedApprox)));
        int year = yearsPassedApprox + 1970;
        MyDate myDate = getMonthAndDay(year, daysPassedThisYear);
        int hours = (int) (millisToday / 3600000);
        int minutes = (int) ((millisToday % 3600000) / 60000);
        int seconds = (int) ((millisToday % 60000) / 1000);


        System.out.println("Year: " + year);
        System.out.println("Month: " + myDate.month);
        System.out.println("Day: " + myDate.day);
        System.out.println("Hour: " + hours);
        System.out.println("Minutes: " + minutes);
        System.out.println("Seconds: " + seconds);
    }

    public static MyDate getMonthAndDay(int year, int daysPassedThisYear) {
        int i;
        int daysLeft = daysPassedThisYear;
        boolean leapYear = isLeapYear(year);
        for (i = 0; i < daysInMonth.length; i++) {
            int days = daysInMonth[i];
            if (leapYear && i == 1) {
                days++;
            }
            if (days <= daysLeft) {
                daysLeft -= days;
            } else {
                break;
            }
        }
        return new MyDate(i + 1, daysLeft + 1);
    }

    public static int leapYearsCount(long yearsPassed) {
        int count = 0;
        for (int i = 1970; i < 1970 + yearsPassed ; i++) {
            if (isLeapYear(i)) {
                count++;
            }
        }
        return count;
    }

    public static boolean isLeapYear(int year) {
        return (year % 4 == 0 && !(year % 100 == 0)) || year % 400 == 0;
    }

}
