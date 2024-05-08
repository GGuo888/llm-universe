# 导入定位env文件的模块
from dotenv import load_dotenv,find_dotenv
_ = load_dotenv(find_dotenv())

import qianfan 

def get_wenxin_message(prompt):
    '''
    构造请求参数
    '''
    message = [dict(role='user',content=prompt)]
    return message

def get_wenxin_completion(prompt,model='ERNIE-Bot',temperature=0.1):
    '''
    调用文心大模型生成对问题的回答
    '''
    chat_comp = qianfan.ChatCompletion()
    # 调用message函数构成信息序列
    message = get_wenxin_message(prompt)
    # 调用文心大模型进行回答prompt
    resp = chat_comp.do(messages=message,
                        model=model,
                        temperature=temperature,
                        system='you are a helpful assistant')
    return resp['result']

text_1 = f"""
泡一杯茶很容易。首先，需要把水烧开。\
在等待期间，拿一个杯子并把茶包放进去。\
一旦水足够热，就把它倒在茶包上。\
等待一会儿，让茶叶浸泡。几分钟后，取出茶包。\
如果您愿意，可以加一些糖或牛奶调味。\
就这样，您可以享受一杯美味的茶了。
"""

prompt = f"""
您将获得由三个引号括起来的文本。\
如果它包含一系列的指令，则需要按照以下格式重新编写这些指令：
第一步 - ...
第二步 - …
…
第N步 - …
如果文本中不包含一系列的指令，则直接写“未提供步骤”。"
{text_1}
"""


print(get_wenxin_completion(prompt))

