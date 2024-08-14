<form id="myForm" method="get" action="/your-endpoint">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <input type="submit" value="Submit">
</form>

<script>
document.getElementById('myForm').onsubmit = function(event) {
    // 阻止表单的默认提交行为
    event.preventDefault();
    
    // 获取表单数据
    const name = document.getElementById('name').value;
    
    // 构造查询字符串
    const queryString = `name=${encodeURIComponent(name)}`;

    // 使用 Fetch API 向后端发送 GET 请求
    fetch(`/your-endpoint?${queryString}`)
        .then(response => response.json())  // 假设后端返回 JSON 数据
        .then(data => {
            // 处理后端返回的数据
            console.log(data.returnvalue); // 打印返回值
            // 你可以在这里使用 data.returnvalue 更新页面或图表等
        })
        .catch(error => console.error('Error:', error));
};
</script>
