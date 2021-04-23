#汉子转拼音工具
from pypinyin import lazy_pinyin

def pinyinstring(inputstr):
    return ''.join(lazy_pinyin(inputstr))