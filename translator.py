from googletrans import Translator
# pip install googletrans==4.0.0-rc1
from tkinter import *
import time

t = Translator(service_urls=['translate.google.com'])
# list of more common lang used by myself
lang_lst = [None, 'zh-cn', 'en', 'zh-tw', 'ja', 'ko']


def config():
##    is_default = input('Go default by translating text to simplified Chinese? '
##                       '(y or enter/n)')
##    if is_default == '' or is_default.lower() == 'y':  # enter/y/Y
##        return 1

    while True:
        lang = input('Translate to: \n1: Simplified Chinese\t2:English\t'
                     '3:Traditional Chinese\t4:Japanese\t5:Korean'
                     '\n')
        try:
            lang = int(lang)
            if 0 < lang <= len(lang_lst):  # make sure lang is valid integer
                return lang
            else:
                raise KeyError
        except Exception:
            print(f'Option is not valid, please enter an integer between '
                  f'1 and {len(lang_lst)}')


lang_opt = config()

window = Tk()
window.title('Translator')
window.geometry('300x200')
text_window = Text(window, font=('Microsoft YaHei', 9))
text_window.configure(state='normal')  # normal/disabled: able/not able to edit
window.attributes('-topmost', True)


def update_translation(original, translation):
    text_displayed = original + '\n\n' + translation + '\n\n\n'
    text_window.insert('1.0', text_displayed)  # insert to the beginning
    text_window.pack()


old_text = ''
while True:
    window.update()
    new_text = window.clipboard_get()
    if new_text != old_text and new_text != '':
        print('New text read')
        # the clipboard is updated
        translated = t.translate(new_text, dest=lang_lst[lang_opt]).text
        update_translation(new_text, translated)
        old_text = new_text
    else:
        print('No new text copied, retry in 0.1s')
    time.sleep(0.1)
