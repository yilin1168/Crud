from django.db.models import Q
from myapp.models import Author

# 定义一个前缀列表
prefix_list = ['Alice', 'Bob', 'Charlie']

# 构建 Q 对象以排除以前缀列表中任何一个前缀开始的名字
query = Q()
for prefix in prefix_list:
    query |= Q(name__startswith=prefix)

# 使用 exclude 排除匹配的记录
authors = Author.objects.exclude(query)
