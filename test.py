import pandas as pd

# 读取文件
all_df = pd.read_csv('all.txt', sep='\t', header=None, names=['code', 'date1', 'date2'])
csi300_df = pd.read_csv('csi300.txt', sep='\t', header=None, names=['code', 'date1', 'date2'])

# 标准化股票代码格式（统一大小写）
all_df['code'] = all_df['code'].str.upper()
csi300_df['code'] = csi300_df['code'].str.upper()

# 创建代码到日期的映射
date_map = dict(zip(all_df['code'], zip(all_df['date1'], all_df['date2'])))

# 更新csi300的数据
for idx, row in csi300_df.iterrows():
    if row['code'] in date_map:
        csi300_df.at[idx, 'date1'] = date_map[row['code']][0]
        csi300_df.at[idx, 'date2'] = date_map[row['code']][1]

# 保存更新后的文件
csi300_df.to_csv('csi300.txt', sep='\t', header=False, index=False)
