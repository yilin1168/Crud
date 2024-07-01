from datetime import datetime, timedelta

# 获取今年第一天
current_year = datetime.now().year
first_day_of_this_year = datetime(current_year, 1, 1)

# 获取去年的第一天
last_year = current_year - 1
first_day_of_last_year = datetime(last_year, 1, 1)

# 获取去年的今天
today = datetime.now()
last_year_today = today.replace(year=last_year)

# 格式化为字符串
first_day_of_this_year_str = first_day_of_this_year.strftime('%Y-%m-%d')
first_day_of_last_year_str = first_day_of_last_year.strftime('%Y-%m-%d')
last_year_today_str = last_year_today.strftime('%Y-%m-%d')

print(f"今年第一天: {first_day_of_this_year_str}")
print(f"去年的第一天: {first_day_of_last_year_str}")
print(f"去年的今天: {last_year_today_str}")
