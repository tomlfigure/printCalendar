from month import Month

class Year:
    def __init__(self,year_value):
        self.year_value=year_value
        #创建月份
        months = []
        #指定月份类型，1-12
        for mType in range(1, 13):
            m = Month(str(mType))
            months.append(m)
        self.months=months

    def display(self):

        #打印年份标识
        self.months[0].printSpaces(12)
        print(self.year_value,end='')
        #调用Month中的年份信息
        self.months[0].printSpaces(3)
        print("年",end='')

        #\n
        print()

        #对每一个月份进行打印
        for month in self.months:
            month.display(self.year_value)

        #行末标识符
        print("-"*35,end='')

