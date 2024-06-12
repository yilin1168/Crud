import subprocess

# 定义可执行程序的路径和参数
exe_path = "path/to/your/executable.exe"
args = ["arg1", "arg2"]  # 可执行程序的参数列表

# 使用 subprocess.run 来调用可执行程序
result = subprocess.run([exe_path] + args, capture_output=True, text=True)

# 输出结果
print("Return code:", result.returncode)
print("Output:", result.stdout)
print("Error:", result.stderr)
