import subprocess
import json

# 定义curl命令
# curl1 = "export PATH='/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH'"
curl_command = """
/usr/bin/curl --location 'https://api.bnm.gov.my/public/exchange-rate' \
--header 'Accept: application/vnd.BNM.API.v1+json' \
--header 'Cookie: 6faa1a9cb04f644c6b76dd2d6810bb5a=7d43fa7fde710f0b9c2a73eb39e95069; TS01efcbd3=012be42521c740f6c6955c227af6dc6852a76277101acade3e83ae60ac8b0b89c518b8ab8fcc047ca141ad1bd899027e9449d23307929d3b80e35a12d9b85a914ced9090b1'
"""

# 使用subprocess运行curl命令
# result1 = subprocess.run(curl1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result = subprocess.run(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 检查命令执行结果
if result.returncode == 0:
    # 成功，打印结果
    try:
        # 尝试解析JSON输出
        data = json.loads(result.stdout)
        print(data)
    except json.JSONDecodeError:
        # 处理非JSON输出
        print(result.stdout)
else:
    # 失败，打印错误信息
    print(f"Error: {result.stderr}")
