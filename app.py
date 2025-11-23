import requests  # 导入 requests 库以进行 HTTP 请求
from dotenv import load_dotenv  # 导入 dotenv 库以加载环境变量
import os  # 导入 os 库以访问环境变量
import json  # 导入 JSON 模块以处理 JSON 数据

load_dotenv()  # 加载 .env 文件中的环境变量
TOKEN = os.getenv("TOKEN")  # 从 .env 文件中获取 API Token

def chat_stream(user_text):
    url = "https://api.siliconflow.cn/v1/chat/completions"  # API 端点 URL
    payload = {
        "model": "Qwen/QwQ-32B",  # 指定使用的模型
        "messages": [
            {
                "role": "user",  # 消息角色，表示用户输入
                "content": user_text  # 用户输入的文本内容
            }
        ],
    "stream": True,  # 启用流式响应
    }
    headers = {
        "Authorization": f"Bearer {TOKEN}",  # 设置授权头，使用 Bearer Token 认证
        "Content-Type": "application/json"  # 设置请求头，指定内容类型为 JSON
    }

    with requests.post(url, headers=headers, json=payload, stream=True) as r:
        for line in r.iter_lines():  # 逐行读取流式响应（每一行是一个数据块）
            if not line:  # 过滤空行
                continue
            decoded = line.decode("utf-8").strip()  # 解码并去除多余空白
            if decoded == "data: [DONE]":  # 流结束标志
                break
            if decoded.startswith("data: "):    # 有效数据块前缀（格式：data: {JSON}）
                try:
                    data_json = json.loads(decoded[len("data: "):])  # 解析 JSON 数据
                    choices = data_json.get("choices", [])  # 提取 choices 字段（API 响应结构）
                    for choice in choices:
                        delta = choice.get("delta", {})  # 提取 delta 字段（增量内容）
                        text = delta.get("content")  # 增量文本存于 delta.content
                        if text:  # 如果存在增量文本，则打印
                            print(text, end="", flush=True)  # 实时输出增量文本
                except json.JSONDecodeError:
                    continue  # 忽略解析错误（避免单块数据异常导致整体中断）

if __name__ == "__main__":
    print("SiliconFlow ChatBot")
    while True:
        user_input = input("\n你: ")
        print("AI: ", end="", flush=True)
        chat_stream(user_input)
        print()
