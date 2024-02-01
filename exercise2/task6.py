def list_years(dates: list):
    years_list = []

    for date_object in dates:
        if len(date_object) == 3:
            years_list.append(date_object[0])

    years_sorted = sorted(years_list)

    return years_sorted


date1 = (2019, 2, 3)
date2 = (2006, 10, 10)
date3 = (1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)
