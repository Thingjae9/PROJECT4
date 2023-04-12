import pandas as pd
import sqlite3

#상의
csv_files = ['musinsa_ranking_category1_page1.csv','musinsa_ranking_category1_page2.csv','musinsa_ranking_category1_page3.csv','musinsa_ranking_category1_page4.csv','musinsa_ranking_category1_page5.csv']
data_frames = []
for file in csv_files:
    data_frames.append(pd.read_csv('csv/'+file))

merged_df1 = pd.concat(data_frames, ignore_index=True)
conn = sqlite3.connect('up_cloth.db')

table_name = 'up_cloth'
merged_df1.to_sql(table_name, conn)
merged_df1 = merged_df1[['브랜드명','의류명','성별']]
merged_df1['category'] = '상의'
conn.close()

# 아우터
csv_files = ['musinsa_ranking_category2_page1.csv','musinsa_ranking_category2_page2.csv','musinsa_ranking_category2_page3.csv','musinsa_ranking_category2_page4.csv','musinsa_ranking_category2_page5.csv']
data_frames = []
for file in csv_files:
    data_frames.append(pd.read_csv('csv/'+file))

merged_df2 = pd.concat(data_frames, ignore_index=True)
conn = sqlite3.connect('outer_cloth.db')

table_name = 'outer_cloth'
merged_df2.to_sql(table_name, conn)
merged_df2 = merged_df2[['브랜드명','의류명','성별']]
merged_df2['category'] = '아우터'
conn.close()

# 하의
csv_files = ['musinsa_ranking_category3_page1.csv','musinsa_ranking_category3_page2.csv','musinsa_ranking_category3_page3.csv','musinsa_ranking_category3_page4.csv','musinsa_ranking_category3_page5.csv']
data_frames = []
for file in csv_files:
    data_frames.append(pd.read_csv('csv/'+file))

merged_df3 = pd.concat(data_frames, ignore_index=True)
conn = sqlite3.connect('down_cloth.db')

table_name = 'down_cloth'
merged_df3.to_sql(table_name, conn)
merged_df3 = merged_df3[['브랜드명','의류명','성별']]
merged_df3['category'] = '하의'
conn.close()

# 가방
csv_files = ['musinsa_ranking_category4_page1.csv','musinsa_ranking_category4_page2.csv','musinsa_ranking_category4_page3.csv','musinsa_ranking_category4_page4.csv','musinsa_ranking_category4_page5.csv']
data_frames = []
for file in csv_files:
    data_frames.append(pd.read_csv('csv/'+file))

merged_df4 = pd.concat(data_frames, ignore_index=True)
conn = sqlite3.connect('bag_cloth.db')

table_name = 'bag_cloth'
merged_df4.to_sql(table_name, conn)
merged_df4 = merged_df4[['브랜드명','의류명','성별']]
merged_df4['category'] = '가방'
conn.close()

# 신발
csv_files = ['csv\musinsa_ranking_category5_page1.csv','csv\musinsa_ranking_category5_page2.csv','csv\musinsa_ranking_category5_page3.csv','csv\musinsa_ranking_category5_page4.csv','csv\musinsa_ranking_category5_page5.csv']
data_frames = []
for file in csv_files:
    data_frames.append(pd.read_csv(file))

merged_df5 = pd.concat(data_frames, ignore_index=True)
conn = sqlite3.connect('shoes_cloth.db')

table_name = 'shoes_cloth'
merged_df5.to_sql(table_name, conn)
merged_df5 = merged_df5[['브랜드명','의류명','성별']]
merged_df5['category'] = '신발'
conn.close()

result = pd.concat([merged_df1, merged_df2, merged_df3, merged_df4, merged_df5], axis=0)

result.to_csv('csv/result.csv')