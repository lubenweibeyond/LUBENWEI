import time

def countdown(t):
    """进行倒计时，每秒更新输出"""
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def main():
    work_time = 25 * 60  # 25分钟
    rest_time = 5 * 60   # 5分钟
    cycles = 4

    for _ in range(cycles):
        print("开始工作！")
        countdown(work_time)
        print("工作完成，开始休息！")
        countdown(rest_time)
        print("休息结束，准备继续工作！")

    print("所有周期完成！休息一下吧！")

if __name__ == '__main__':
    main()
