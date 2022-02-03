import requests
import json
from tkinter import *
import time

def translate(word):
    # 有道词典 api
    # url = 'https://fanyi.youdao.com/'
    # url = 'https://openapi.youdao.com/api'
    # url = 'http://fanyi.youdao.com/openapi.do?keyfrom=<keyfrom>&key=<key>&type=data&doctype=<doctype>&version=1.1&q=要翻译的文本'
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        return response.text
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        return None
 
 
def get_main(word):
    list_trans = translate(word)
    result = json.loads(list_trans)
    s = ''
    for paragraph in result['translateResult']:
        for sentence in paragraph:
            s += sentence['tgt']
    return s


def update_window(original, translation):
    text_displayed = original + '\n\n' + translation + '\n\n\n'
    text_window.insert('1.0', text_displayed)  # insert to the beginning
    text_window.pack()


if __name__ == '__main__':
    window = Tk()
    window.title('Translator')
    window.geometry('300x200')
    text_window = Text(window, font=('Microsoft YaHei', 9))
    text_window.configure(state='normal')  # normal/disabled: able/not able to edit
    window.attributes('-topmost', True)

    old_text = ''
    while True:
        window.update()
        new_text = window.clipboard_get()
        if new_text != old_text and new_text != '':
            # the clipboard is updated
            translated = get_main(new_text)
            # print(translated)
            update_window(new_text, translated)
            old_text = new_text
            
        time.sleep(0.1)
