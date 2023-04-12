from flask import Flask, request, render_template
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.graph_objs as go
import json

app = Flask(__name__)
df = pd.read_csv('clean.csv')
vectorizer = TfidfVectorizer()
tfidf_vectors = vectorizer.fit_transform(df.name)

@app.route('/')
def home():
    global df
    df = pd.read_csv('clean.csv')
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_recommendation():
    global df
    gender = request.form['gender']
    category = request.form['category']
    keyword = request.form['keyword']
    # 이제 추천 로직을 수행합니다.
    # 결과는 HTML 문자열로 생성합니다.
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

    if gender == '남':
        filtered_df = df[df['gender'].isin(['남', '남 여'])]
    elif gender == '여':
        filtered_df = df[df['gender'].isin(['여', '남 여'])]
    else:
        filtered_df = df
    
    model = TfidfVectorizer()
    tfidf_vectors = model.fit_transform(filtered_df['name'])
    keyword_vector = model.transform([keyword])

    cosine_similarities = cosine_similarity(keyword_vector, tfidf_vectors)

    results = cosine_similarities[0].argsort()[:-4:-1]
    recommended_products = filtered_df.iloc[results]
    reco_brand = recommended_products['brand']
    recommended_products = recommended_products['name']


    
    result = '<h1>당신을 위한 추천 아이템</h1>'
    result += '<p>Gender : {}</p>'.format(gender)
    result += '<p>Category : {}</p>'.format(category)
    result += '<p>Keyword : {}</p>'.format(keyword)
    result += '<h1>1위 브랜드 : {}</h1>'.format(reco_brand.iloc[0])
    result += '<p>추천 아이템 1위 : {}</p>'.format(recommended_products.iloc[0])
    result += '<p>추천 아이템 2위 : {}</p>'.format(recommended_products.iloc[1])
    result += '<p>추천 아이템 3위 : {}</p>'.format(recommended_products.iloc[2])
    # 추천 결과를 반환합니다.
    return result

@app.route('/dashboard')
def dashboard():
    # 데이터 로드
    df1 = pd.read_csv('final.csv')
    group_brand = df1.groupby('브랜드명')['누적판매량(1년)']
    
    brand_list = []
    for row in df1['브랜드명']:
        brand_list.append(row)
    
    sales_list = []
    for amount in df1['누적판매량(1년)']:
        sales_list.append(amount)
        


    # 대시보드 출력
    return render_template('brand_for_sales.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('brand_for_gender.html')

@app.route('/dashboard3')
def dashboard3():
    return render_template('brand_for_total.html')


if __name__ == '__main__':
    app.run(debug=True)