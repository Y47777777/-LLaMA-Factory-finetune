import json
import random

with open('alpaca_data_en.json', 'r') as file:
    data_en = json.load(file)
with open('alpaca_data_zh.json', 'r') as file:
    data_zh = json.load(file)
# # for info in data:
# #     del info['en_instruction']
# #     del info['en_input']
# #     del info['en_output']
data = []
data.extend(data_zh)
data.extend(data_en)

# with open('self_alpaca_52k_bak.json', 'r') as file:
#     data = json.load(file)
random.shuffle(data)
with open('self_alpaca_52k.json', 'w') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)