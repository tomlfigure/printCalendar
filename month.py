class Month:
    def __init__(self, mType):
        #常量，用字典存储
        self.days_dict = {
            '1': 31,
            '2': 28,
            '3': 31,
            '4': 30,
            '5': 31,
            '6': 30,
            '7': 31,
            '8': 31,
            '9': 30,
            '10': 31,
            '11': 30,
            '12': 31
        }
        self.mType=str(mType)
        #自动计算每个月的日期数
        self.days = self.days_dict[self.mType]
        #常量,用字典存储
        self.weekDaySimbols = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def printSpaces(self,nums):
        print(' '*nums,end='')
    def getStartWeek(self,year):
        import time
        #创建结构时间
        struct_time = (year, int(self.mType), 1, 0, 0, 0, 0, 0, 0)
        #获取该结构时间的时间戳
        timestamp = time.mktime(struct_time)
        #获取星期数
        week=int(time.strftime("%w", time.localtime(timestamp)))
        #星期日的默认数值为0 所以当week为false时，返回7
        return week if week else 7
    def display(self, year):
        # 打印标识符
        # 打印分隔符
        print("-"*35,end='')
        print()

        # 打印月份
        self.printSpaces(13)
        print(self.mType,end='')
        self.printSpaces(4)
        print("月")

        # 打印星期标志
        for wds in self.weekDaySimbols:
            print(wds, end='  ')
        print()

        # 打印日期
        #获取每月1日的日期
        startWeek=self.getStartWeek(2023)
        self.printSpaces(1+(startWeek-1)*5)
        for day in range(1,self.days+1):
            print(day,end='')
            if day<10:
                self.printSpaces(4)
            else:
                #大于10只需空3格
                self.printSpaces(3)
            #到星期天就换个行打印
            if startWeek%7==0:
                print("\n")
                #对齐上一行
                self.printSpaces(1)
            startWeek+=1

        #\n
        print()

