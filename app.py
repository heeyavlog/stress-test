import streamlit as st

def run_bepsi_test():
    st.title('스트레스 자가진단 테스트 (BEPSI-K)')
    st.write('지난 한 달 동안 귀하가 느끼고 경험했던 내용에 대해 가장 적절한 답을 선택해주세요.')
    
    questions = [
        "지난 한달 동안 생활하면서 힘들었던 일이 얼마나 있었습니까?",
        "지난 한달 동안 자신의 생활신념에 맞지 않는 일을 해야할 때가 얼마나 있었습니까?",
        "지난 한달 동안 한번에 너무 많은 일을 해야 했던 적이 얼마나 있었습니까?",
        "지난 한달 동안 자신의 능력이나 기술로 감당하기 어려운 일을 해야 했던 때가 얼마나 있었습니까?",
        "지난 한달 동안 할 일이 너무 많아 정작 중요한 일을 잊었던 적이 얼마나 있었습니까?"
    ]
    
    options = {
        "전혀 없었다": 1,
        "간혹 있었다": 2,
        "가끔 있었다": 3,
        "자주 있었다": 4,
        "매우 자주 있었다": 5
    }
    
    scores = []
    
    st.write('---')
    
    for i, question in enumerate(questions, 1):
        st.subheader(f'{i}. {question}')
        answer = st.radio(
            "빈도를 선택하세요:",
            options.keys(),
            key=f"q{i}"
        )
        scores.append(options[answer])
        st.write('---')
    
    if st.button('결과 확인하기'):
        total_score = sum(scores) / len(scores)  # 평균 점수 계산
        st.subheader('검사 결과')
        st.write(f'평균 점수: {total_score:.1f}점')
        
        if total_score < 2.0:
            st.success('정상 범위의 스트레스 수준입니다.')
        elif total_score < 2.4:
            st.info('약간 높은 스트레스 수준입니다. 스트레스 관리에 관심을 가져보세요.')
        elif total_score < 2.8:
            st.warning('중등도의 스트레스 상태입니다. 스트레스 해소 방법을 찾아보세요.')
        else:
            st.error('심한 스트레스 상태입니다. 전문가의 도움을 받아보시는 것이 좋겠습니다.')
        
        st.write('---')
        st.write('주의: 이 테스트는 참고용이며, 정확한 진단을 위해서는 반드시 전문가와 상담하시기 바랍니다.')
        
        if total_score >= 2.4:
            st.write('''
            ### 도움받을 수 있는 곳
            - 정신건강상담전화: 1577-0199
            - 스트레스 상담전화: 1899-3073
            - 가까운 정신건강복지센터 찾기: [링크](https://www.mentalhealth.go.kr/portal/health/fac/PotalHealthFacListTab2.do)
            - 좀더 많은 정보를 알고 싶다면: [링크](https://lzhakko.tistory.com/)
            
            ### 스트레스 관리 방법
            1. 규칙적인 운동
            2. 충분한 수면
            3. 명상이나 심호흡
            4. 취미 활동
            5. 주변 사람들과의 대화
            ''')

if __name__ == '__main__':
    run_bepsi_test()
