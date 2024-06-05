from datetime import datetime, timedelta

# 获取当前日期
today = datetime.today()

# 计算前一天的日期
yesterday = today - timedelta(days=1)

# 将日期格式化为所需的字符串格式
formatted_yesterday = yesterday.strftime('%Y%m%d')

print(formatted_yesterday)
