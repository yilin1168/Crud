from datetime import datetime, timedelta
import os


def check_today_files(directory):
    # 获取今天的日期
    today = datetime.today().date()
    
    # 获取目录中的所有文件
    files = os.listdir(directory)
    
    # 过滤出今天生成的文件
    today_files = []
    for file in files:
        if file.startswith(('Data1', 'Data2')):
            file_path = os.path.join(directory, file)
            # 获取文件的修改时间
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path)).date()
            if file_mod_time == today:
                today_files.append(file)
    
    return today_files

# 示例使用
directory_path = 'your_directory_path_here'  # 替换为你的目录路径
today_files = check_today_files(directory_path)
print(f"Today's files starting with 'Data1' or 'Data2': {today_files}")

# Today.py
# 获取当前日期
# today = datetime.today()
# # 计算前一天的日期
# yesterday = today - timedelta(days=1)
# # 将日期格式化为所需的字符串格式
# formatted_yesterday = yesterday.strftime('%Y%m%d')
# print(formatted_yesterday)
