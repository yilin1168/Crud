from datetime import datetime
import pytz

# 输入的GMT时间字符串
gmt_time_str = "22/10/2024 15:30:00"  # dd/mm/yyyy HH:MM:SS 格式

# 将字符串解析为datetime对象
gmt_time = datetime.strptime(gmt_time_str, "%d/%m/%Y %H:%M:%S")

# 设置时区为GMT（UTC）
gmt_timezone = pytz.timezone('UTC')

# 将解析的时间对象设为GMT时区
gmt_time = gmt_timezone.localize(gmt_time)

# 设置SGT时区
sgt_timezone = pytz.timezone('Asia/Singapore')

# 将GMT时间转换为SGT时间
sgt_time = gmt_time.astimezone(sgt_timezone)

# 输出转换后的SGT时间
print("SGT Time:", sgt_time.strftime("%d/%m/%Y %H:%M:%S"))