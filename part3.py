import pandas as pd
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from scipy.sparse import vstack, hstack
from flask import Flask, render_template, request

app = Flask(__name__)

# 데이터셋 불러오기
df = pd.read_csv('clean.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gender = request.form['gender']
        category = request.form['category']
        keyword = request.form['keyword']
        
        # 카테고리에 따른 필터링
        if category == '상의':
            filtered_df = df[df['category'].isin(['상의'])]
            df = filtered_df.drop(['category'], axis=1)

        elif category == '하의':
            filtered_df = df[df['category'].isin(['하의'])]
            df = filtered_df.drop(['category'], axis=1)
        
        elif category == '아우터':
            filtered_df = df[df['category'].isin(['아우터'])]
            df = filtered_df.drop(['category'], axis=1)
        
        elif category == '가방':
            filtered_df = df[df['category'].isin(['가방'])]
            df = filtered_df.drop(['category'], axis=1)
        
        elif category == '신발':
            filtered_df = df[df['category'].isin(['신발'])]
            df = filtered_df.drop(['category'], axis=1)
        
        else: df = df
        

        # 성별에 따른 필터링
        if gender == '남':
            filtered_df = df[df['성별'].isin(['남', '남 여'])]
        elif gender == '여':
            filtered_df = df[df['성별'].isin(['여', '남 여'])]
        else:
            filtered_df = df
        
        # 키워드에 따른 필터링
        result = filtered_df

        return jsonify({'result': result})
    return jsonify({'result': result})


    

if __name__ == '__main__':
    app.run(debug=True)

