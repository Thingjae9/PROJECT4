import pandas as pd

#상의
csv_files = ['musinsa_ranking_category1_page1.csv','musinsa_ranking_category1_page2.csv','musinsa_ranking_category1_page3.csv','musinsa_ranking_category1_page4.csv','musinsa_ranking_category1_page5.csv']
data_frames = []
for file in csv_files:
    data_frames.append(pd.read_csv('csv/'+file))

merged_df1 = pd.concat(data_frames, ignore_index=True)

merged_df1['category'] = '상의'


csv_files = ['musinsa_ranking_category2_page1.csv','musinsa_ranking_category2_page2.csv','musinsa_ranking_category2_page3.csv','musinsa_ranking_category2_page4.csv','musinsa_ranking_category2_page5.csv']
data_frames = []
for file in csv_files:
    data_frames.append(pd.read_csv('csv/'+file))

merged_df2 = pd.concat(data_frames, ignore_index=True)

merged_df2['category'] = '아우터'


csv_files = ['musinsa_ranking_category3_page1.csv','musinsa_ranking_category3_page2.csv','musinsa_ranking_category3_page3.csv','musinsa_ranking_category3_page4.csv','musinsa_ranking_category3_page5.csv']
data_frames = []
for file in csv_files:
    data_frames.append(pd.read_csv('csv/'+file))

merged_df3 = pd.concat(data_frames, ignore_index=True)

merged_df3['category'] = '하의'


# 가방
csv_files = ['musinsa_ranking_category4_page1.csv','musinsa_ranking_category4_page2.csv','musinsa_ranking_category4_page3.csv','musinsa_ranking_category4_page4.csv','musinsa_ranking_category4_page5.csv']
data_frames = []
for file in csv_files:
    data_frames.append(pd.read_csv('csv/'+file))

merged_df4 = pd.concat(data_frames, ignore_index=True)

merged_df4['category'] = '가방'


# 신발
csv_files = ['csv\musinsa_ranking_category5_page1.csv','csv\musinsa_ranking_category5_page2.csv','csv\musinsa_ranking_category5_page3.csv','csv\musinsa_ranking_category5_page4.csv','csv\musinsa_ranking_category5_page5.csv']
data_frames = []
for file in csv_files:
    data_frames.append(pd.read_csv(file))

merged_df5 = pd.concat(data_frames, ignore_index=True)

merged_df5['category'] = '신발'


result = pd.concat([merged_df1, merged_df2, merged_df3, merged_df4, merged_df5], axis=0)

result.to_csv('data.csv')