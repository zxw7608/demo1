import time
import winsound

# 提示用户输入专注时间（以分钟为单位）
focus_time = int(input("How many minutes would you like to focus? "))

# 将专注时间转换为秒数
focus_seconds = focus_time * 60

# 记录开始时间
start_time = time.time()

# 在专注时间结束之前一直运行
while time.time() < start_time + focus_seconds:
    # 计算剩余专注时间并格式化为易于阅读的字符串
    remaining_time = int(start_time + focus_seconds - time.time())
    remaining_minutes, remaining_seconds = divmod(remaining_time, 60)
    remaining_time_string = "{:02d}:{:02d}".format(remaining_minutes, remaining_seconds)

    # 输出剩余专注时间
    print("Remaining focus time:", remaining_time_string, end="\r")

    # 等待一秒钟以进行下一个更新
    time.sleep(1)

# 播放提示音，表示专注时间已结束
winsound.Beep(440, 1000)
print("Focus time complete!")
