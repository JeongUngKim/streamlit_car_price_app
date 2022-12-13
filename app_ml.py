import streamlit as st
import numpy as np
import joblib
def run_ml_app() :
    st.subheader('자동차 금액 예측')
    regressor = joblib.load('regressor.pkl')

     #성별은 여자이고,나이는 50이며, 연봉은 40000 카드빚 50000, 자산 200000
    
    # 성별 , 나이 , 연봉, 카드빚 , 자산을 유저한테 모두 입력받아서
    # 자동차 구매 금액을 예측하세요.
    
    gender = st.radio('성별을 선택해주세요. ',['여자','남자'])
    if gender == '남자' : 
        gender = 1
    else :
        gender = 0
    age = st.number_input('나이를 입력해주세요.',min_value=1,max_value=120)
    annual = st.number_input('연봉을 입력해주세요 (단위 $)',min_value=0.0)
    card_debt = st.number_input('카드빚을 입력해주세요. (단위 $)',min_value=0.0)
    net_worth = st.number_input('자산을 입력해주세요. (단위 $)',min_value=0.0)

    user_list = [gender,age,annual,card_debt,net_worth]  
    new_data = np.array(user_list).reshape(1,5)
    y_pred = regressor.predict(new_data)

    if y_pred > 0 :
        st.info('예측한 자동차 금액은 {} 달러 입니다.'.format(y_pred))
    else :
        st.info('예측이 어렵습니다.')
