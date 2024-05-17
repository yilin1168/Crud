from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    event_time = models.CharField(max_length=20)  # 用 CharField 存储特定格式的日期时间字符串

    def get_formatted_event_time(self):
        from datetime import datetime
        try:
            # 将字符串解析为 datetime 对象
            event_time = datetime.strptime(self.event_time, '%d/%m/%Y %H:%M:%S')
            # 格式化为新的日期时间字符串
            return event_time.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            return self.event_time
