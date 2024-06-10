# models.py
from django.db import models

class MyModel(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=255)
    field3 = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['field1', 'field2'], name='unique_field1_field2')
        ]

#handler.py
# 定义默认值
defaults = {'field3': 'new_value'}

# 使用 update_or_create 方法
obj, created = MyModel.objects.update_or_create(
    field1='value1',  # 用于查询的字段
    field2='value2',  # 用于查询的字段
    defaults=defaults  # 用于更新或创建时使用的默认值
)

# 输出结果
if created:
    print("A new object was created.")
else:
    print("The object was updated.")

print(f"Object: {obj}")


# deal with integrity error
# 定义默认值
defaults = {'field3': 'new_value'}

try:
    # 尝试执行 update_or_create
    obj, created = MyModel.objects.update_or_create(
        field1='value1',  # 用于查询的字段
        field2='value2',  # 用于查询的字段
        defaults=defaults  # 用于更新或创建时使用的默认值
    )

    if created:
        print("A new object was created.")
    else:
        print("The object was updated.")

    print(f"Object: {obj}")

except IntegrityError:
    # 处理唯一约束错误
    print("A unique constraint violation occurred.")
    obj = MyModel.objects.get(field1='value1', field2='value2')
    for key, value in defaults.items():
        setattr(obj, key, value)
    obj.save()
    print("The object was updated manually.")

