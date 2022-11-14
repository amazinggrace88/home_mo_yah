import requests
import json
import pandas as pd
import openpyxl
import time

"""
example : 소상공인시장진흥공단_상가(상권)정보_API
"""
# http://apis.data.go.kr/B553077/api/open/sdsc2/오퍼레이션명/필수항목1.../필수항목n?ServiceKey=서비스키&옵션항목1=옵션항목1값......&옵션항목n=옵션항목값n

def get_key():
    # key 가져오기
    key_df = pd.read_excel('/Users/grace/PycharmProjects/home_mo_yah/dataset/소상공인시장진흥공단_상가(상권)정보_활용가이드/20220809_소상공인시장_주요상권현황.xlsx')
    key_list = key_df['상권번호'].tolist()
    return key_list


def get_response(key, serviceKey, operation, type):
    url = f'http://apis.data.go.kr/B553077/{operation}?key={key}&ServiceKey={serviceKey}&type={type}'
    try:
        response = requests.get(url).json()
    except:
        time.sleep(5)
        response = requests.get(url).json()
    return response


if __name__ == '__main__':
    serviceKey = 'AR4UatAaPl9WoEinY9o0FlCGJz%2FX8mhDxpu4ePf8%2BH5DlpXXjzryeS%2FJQ6r2%2FROB6ik2iIhO4fI9fh1FBYWpUA%3D%3D'
    operation = 'api/open/sdsc2/storeZoneOne'  # 소상공인 상가업소 정보서비스 중 지정 상권조회 오퍼레이션 명세
    type = 'json'
    key_list = get_key()
    for idx, key in enumerate(key_list):
        print(f'=={idx}, {key} start ==')
        response = get_response(key=key, serviceKey=serviceKey, operation=operation, type=type)
        columns = response.get('header')['columns']
        row = pd.json_normalize(response.get('body')['items'])
        if idx==0:
            df = pd.DataFrame(row)
        else:
            df = pd.concat([df, row], axis=0)
        print(df)
        print(f'=={idx}, {key} done ==')
        time.sleep(10)
        if key==9249: # 서울특별시만 크롤링
            break
    df = df.rename(columns=columns)
    print(df)
    df.to_csv('/dataset/sdsc2_storeZoneOne.csv')