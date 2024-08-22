def is_leap(year):
    leap = False
      for year in range (1900,10**5):
        if (year%4==0 and year%400==0):
            if (year%100==0):
                continue
            leap=True
    return leap

year = int(input())
