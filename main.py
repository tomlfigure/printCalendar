from year import Year
from month import Month

if __name__ == '__main__':
    #创建年份2023
    year=Year(2023)
    year.display()

    #创建2005年6月，并进行显示，星期和日期完全对的上
    m=Month(6)
    m.display(2005)
