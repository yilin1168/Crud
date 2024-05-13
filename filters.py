# 首先计算每个 field2 的 field1 最大值：这可以通过 annotate 和 group by 完成。
# 然后根据这些最大值找到对应的记录：使用这些最大值作为过滤条件，查询原始数据表


from django.db.models import Max, Q
from myapp.models import CModel

# 计算每个field2的field1最大值
field2_max_field1 = CModel.objects.values('field2').annotate(max_field1=Max('field1'))

# 准备查询条件，用于筛选每个field2对应的field1最大值的记录
query_conditions = Q()
for item in field2_max_field1:
    query_conditions |= (Q(field2=item['field2']) & Q(field1=item['max_field1']))

# 查询符合条件的记录
max_records = CModel.objects.filter(query_conditions).values('field1', 'field2', 'field3', 'field4')
