# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def getFebruaryDays(year):
    if year%4 != 0:
        return 28
    elif year%100 != 0:
        return 29
    elif year%400 != 0:
        return 28
    else:
        return 29

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ##
    # Your code here.
    ##
    current_month = month1
    current_year = year1
    total_days = 0
    while current_year <= year2:
        while current_month <= 12:
            if current_year == year1 and current_year == year2:
                if current_month == month1:
                    if current_month == 2:
#                        print '1 - Adding year, month, days',current_year, current_month, getFebruaryDays(current_year) - day1
                        total_days = getFebruaryDays(current_year) - day1
                    else:
#                        print 'Adding year, month, days',current_year, current_month, daysOfMonths[current_month - 1] - day1
                        total_days = daysOfMonths[current_month - 1] - day1
                elif current_month == month2:
#                    print 'Adding year, month, days',current_year, current_month, day2
                    total_days = total_days + day2
                elif current_month < month2:
                    if current_month == 2:
#                        print 'Adding year, month, days',current_year, current_month, getFebruaryDays(current_year)
                        total_days = total_days + getFebruaryDays(current_year)
                    else:
#                        print 'Adding year, month, days',current_year, current_month, daysOfMonths[current_month - 1]
                        total_days = total_days + daysOfMonths[current_month - 1]
                else:
                    break
            elif current_year == year1 and current_year != year2:
                if current_month == month1:
                    if current_month == 2:
#                        print '2 - Adding year, month, days',current_year, current_month, getFebruaryDays(current_year) - day1
                        total_days = getFebruaryDays(current_year) - day1
                    else:
#                        print '2 - Adding year, month, days',current_year, current_month, daysOfMonths[month1-1] - day1
                        total_days = daysOfMonths[month1-1] - day1
                else:
                    if current_month == 2:
#                        print '2 - Adding year, month, days',current_year, current_month, getFebruaryDays(current_year)
                        total_days = total_days + getFebruaryDays(current_year)
                    else: # month is not february
#                        print '2 - Adding year, month, days',current_year, current_month, daysOfMonths[current_month -1]
                        total_days = total_days + daysOfMonths[current_month -1]
            elif current_year > year1 and current_year < year2:
                if current_month == 2:
                    total_days = total_days + getFebruaryDays(current_year)
                else: # month is not february
                    total_days = total_days + daysOfMonths[current_month -1]
            else: # Last year
                if current_month == month2:
                    total_days = total_days + day2
                elif current_month < month2:
                    if current_month == 2:
#                        print '3 - Adding year, month, days',current_year, current_month, getFebruaryDays(current_year)
                        total_days = total_days + getFebruaryDays(current_year)
                    else: # month is not february
#                        print '3 - Adding year, month, days',current_year, current_month, daysOfMonths[current_month -1]
                        total_days = total_days + daysOfMonths[current_month -1]
                else:
                    break
            current_month = current_month + 1
        current_year = current_year + 1
        current_month = 1
    return total_days


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
