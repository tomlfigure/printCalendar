from Month import Month

class Year:
    def __init__(self,year_value):
        self.year_value=year_value
        months = []
        for mType in range(1, 13):
            m = Month(str(mType))
            months.append(m)
        self.months=months

    def display(self):

        #打印年份标识
        self.months[0].printSpaces(12)
        print(self.year_value,end='')
        self.months[0].printSpaces(3)
        print("年",end='')

        #\n
        print()

        #对每一个月份进行打印
        for month in self.months:
            month.display(self.year_value)
        print("-"*35,end='')

