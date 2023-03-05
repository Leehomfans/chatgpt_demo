import openai
openai.api_key='sk-xxxxxxxxxxxxxxxxxxxxx' 
class bcolors: # 文本颜色
  GREEN = '\033[92m'
  BLUE = '\033[94m'

def print_w(s): #打印文本，内容宽度设置
  width = 150
  while len(s) > width:
    print(f'{s[:width]:<{width}}')
    s = s[width:]
  print(s)
  
def chatGPT_api(list_msg,list_ans,message): # API调用函数
  # 设置system role
  system_role = "\u5C06\u6587\u672C\u7FFB\u8BD1\u4E3A\u82F1\u8BED"  #@param {type:"string",title:""}   
  send_msg=[{"role":"system","content": system_role}]

  # 读取历史对话记录
  for i in range(len(list_msg)):
    _msg={"role":"user","content": list_msg[i]}
    send_msg.append(_msg)
    _ans={"role":"assistant","content": list_ans[i]}
    send_msg.append(_ans)

  # 准备用户的新消息
  _msg={"role":"user","content": message}
  send_msg.append(_msg)

  # 调用API，返回结果
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=send_msg
  )
  #返回结果
  return response["choices"][0]["message"]["content"]

def main():
  # 历史对话记录列表
  history_list_msg=[]
  history_list_ans=[]
  
  while(True):
    # 等待用户输入
    print(f"👧 {bcolors.GREEN}", end="")
    message = input()

    # 调用API，返回结果
    answer = chatGPT_api(history_list_msg, history_list_ans, message)
    print(f"⚛️ {bcolors.BLUE}")
    print_w(answer)

    history_list_msg.append(message)
    history_list_ans.append(answer)

if __name__ == "__main__":
  main()

