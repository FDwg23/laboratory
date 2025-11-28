year = input("Введите год")
if year.isdigit():
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Год високосный")
    else:
        print("Год не високосный")