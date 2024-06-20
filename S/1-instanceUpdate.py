# 创建Model1实例
model1_instance = Model1.objects.create(number=123)

# 使用Model1实例创建Model2实例，并提供name字段的值
model2_instance = Model2.objects.create(model1=model1_instance, name="Example Name")
