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


### SQL
from django.db import connection
from myapp.models import CModel

# 编写SQL查询
sql = """
SELECT * FROM (
    SELECT *,
    RANK() OVER (PARTITION BY field2 ORDER BY field1 DESC) as rank
    FROM myapp_cmodel
) as ranked
WHERE ranked.rank = 1;
"""

# 执行原生SQL查询
with connection.cursor() as cursor:
    cursor.execute(sql)
    results = cursor.fetchall()

# 将结果转换为CModel对象，假设你需要以Django模型的形式处理它们
cmodels = [CModel(*row) for row in results]


###subquery
from django.db.models import OuterRef, Subquery

# 创建一个子查询，用于找到每个field2的field1最大值对应的记录
subquery = CModel.objects.filter(field2=OuterRef('field2')).order_by('-field1').values('field1')[:1]

# 主查询，查询符合子查询条件的记录
resulting_queryset = CModel.objects.filter(field1=Subquery(subquery)).order_by('field2')

# 现在 resulting_queryset 包含了每个 field2 的 field1 最大值的记录

