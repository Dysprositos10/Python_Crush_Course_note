#喜欢的数
from pathlib import Path
import json
number = input('please input your favoriate number:')
path = Path('favoriate_number.txt')
contents = json.dumps(number) #json.dumps() 函数生成指定json文件的字符串
path.write_text(contents) #写入