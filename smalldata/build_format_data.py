

# 这个脚本将raw_data.txt转换为data.txt
# raw_data.txt从https://github.com/MarkWuNLP/MultiTurnResponseSelection下载的
# 将data.txt转化成preprocess_raw_data()的标准处理格式
'''
想看你的美照
亲我一口就给你看
我亲两口
讨厌人家拿小拳拳捶你胸口

下一组语料
'''
path = 'raw_data.txt'
out = 'data.txt'
fw = open(out,'w',encoding='utf-8')
for line in open(path,'r',encoding='utf-8').readlines():
    # 用'\t'将句子划分成对话
    parts = line.split('\t')
    for one_sent in parts[1:]:
        # 把每个人说的每句话连词成句
        one_sent = ''.join(one_sent.strip().split(' '))
        # 用'\n'换行
        fw.write(one_sent+'\n')
    fw.write('\n')
fw.close()
print('finish')