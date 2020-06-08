import yaml

file = open('a.yml', encoding='utf-8')
res = yaml.load(file,Loader=yaml.FullLoader)
# 打印成为字典的格式
print(res)