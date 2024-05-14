
# views.py
from django.contrib.auth.models import User, Group
from django.shortcuts import render

def is_boss(user):
    return user.groups.filter(name='Boss').exists()


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    context = {
        'can_edit': request.user.groups.filter(name='Boss').exists(),
        'value': 'Some data to display'
    }
    return render(request, 'my_template.html', context)



# html templates
<table>
    <tr>
        {% if can_edit %}
            <td><input type="text" value="{{ value }}"></td>
        {% else %}
            <td>{{ value }}</td>
        {% endif %}
    </tr>
</table>
<!-- 假设你有一个表格，并且某些单元格需要根据权限决定是否可编辑 -->
<table>
    <tr>
        <td>
            <!-- 使用 Django 模板标签来条件渲染 -->
            {% if can_edit %}
                <input type="text" value="Editable Value">
            {% else %}
                Non-Editable Value
            {% endif %}
        </td>
        <!-- 其他 td 元素 -->
    </tr>
</table>


