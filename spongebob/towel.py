import streamlit as st
import requests
import pandas as pd
import time


if 'page' not in st.session_state:
    st.session_state['page'] = 'home'
def change_page(page):
    st.session_state['page'] = page


if st.session_state['page'] == 'home':
    st.title("☘️취미 입문 가이드☘️") # 나중에 더 나은 이름으로 바꾸던지 하기
    st.header("알아보고 싶은 취미를 선택해주세요!")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button('⚾️ 야구', on_click=change_page, args=['baseball'])
    with col2:
        st.button('📽️ 영화감상', on_click=change_page, args=['movie'])
    with col3:
        st.button('🎤 아이돌', on_click=change_page, args=['idol'])
    with col4:
        st.button('📚독서', on_click=change_page, args=['book'])
    st.markdown("------")
    st.info("각 취미를 클릭하면 소개 페이지로 이동합니다")
elif st.session_state['page'] == 'baseball':
    st.title("⚾️ 야구")
    st.header("🍀야구 입문 가이드!")
    st.subheader("❕야구란?")
    st.write("경기 인원 9~10명으로 구성된 두 팀이 공격과 수비를 번갈아 가며 진행하며, 18세기 중반 잉글랜드에서 시작된 스포츠")
    st.write("룰: ① 점수 획득🏏: 투수가 던진 공을 타자가 쳐내고 1루, 2루, 3루를 거쳐 홈 베이스까지 무사히 돌아오면 1점을 얻는다.")
    st.write("    ② 공수 교대🏟️: 한 팀의 타자 3명이 아웃되면 공격과 수비가 교대되며, 이것을 이닝이라고 한다.")
    st.write("    ③ 경기 승리🏆: 보통 9이닝 동안 진행하며, 경기 종료 시점에 더 많은 점수를 얻은 팀이 승리한다. (동점 시 연장전 진행 가능)")
    st.write("    ④ 아웃🧢: 타자가 친 공이 땅에 닿기 전에 수비수에게 잡히거나, 타자 또는 주자가 아웃되는 방법(태그 아웃, 포스 아웃, 삼진 등)으로 세 번 아웃이 되면 이닝이 종료된다.")
    st.markdown("---")
    st.subheader("❕구단 소개")
    team = st.selectbox(
    '상세 정보를 볼 구단을 선택해주세요:',
    [                              
        '두산 베어스', 'LG 트윈스', '키움 히어로즈', 'SSG 랜더스', 'KT 위즈',
        '삼성 라이온즈', 'KIA 타이거즈', '롯데 자이언츠', 'NC 다이노스', '한화 이글스'
    ]                          
    )
    if team == '두산 베어스':
        img_col, text_col = st.columns([0.15, 0.85])
        with img_col:
            st.image('두산.PNG', width=80)
        with text_col:
            st.subheader('두산 베어스')
        st.write('=> 창단연도: 1982년')
        st.write('=> 연고지: 서울')
        st.caption('#연고지란: 스포츠에서 구단이 홈구장을 두고, 구단 존립의 근거로 하는 지역')
        st.write('=> 홈구장: 잠실 야구장')
        st.write('=> 우승 횟수: 6회 (1982, 1995, 2001, 2015, 2016, 2019)')
        st.image('철웅.PNG', width=200)
    elif team == 'LG 트윈스':
        img_col, text_col = st.columns([0.15, 0.85])
        with img_col:
            st.image('LG.PNG', width=80)
        with text_col:
            st.subheader('LG 트윈스')
        st.write('=> 창단연도: 1990년')
        st.write('=> 연고지: 서울')
        st.caption('#연고지란: 스포츠에서 구단이 홈구장을 두고, 구단 존립의 근거로 하는 지역')
        st.write('=> 홈구장: 잠실 야구장')
        st.write('=> 우승 횟수: 3회 (1990, 1994, 2023)')
        st.image('럭키와스타.PNG', width=200)
    elif team == '키움 히어로즈':
        img_col, text_col = st.columns([0.15, 0.85])
        with img_col:
            st.image('키움.PNG', width=80)
        with text_col:
            st.subheader('키움 히어로즈')
        st.write('=> 창단연도: 2008년')
        st.write('=> 연고지: 서울')
        st.caption('#연고지란: 스포츠에서 구단이 홈구장을 두고, 구단 존립의 근거로 하는 지역')
        st.write('=> 홈구장: 고척 스카이돔')
        st.write('=> 우승 횟수: 0회')
        st.image('턱돌이.PNG', width=200)
    elif team == 'SSG 랜더스':
        img_col, text_col = st.columns([0.15, 0.85])
        with img_col:
            st.image('SSG.PNG', width=80)
        with text_col:
            st.subheader('SSG 랜더스')
        st.write('=> 창단연도: 2021년')
        st.write('=> 연고지: 인천')
        st.caption('#연고지란: 스포츠에서 구단이 홈구장을 두고, 구단 존립의 근거로 하는 지역')
        st.write('=> 홈구장: 인천 SSG 랜더스필드')
        st.write('=> 우승 횟수: 5회 (2007, 2008, 2010, 2018, 2022)')
        st.image('랜디.PNG', width=200)
    elif team == 'KT 위즈':
        img_col, text_col = st.columns([0.15, 0.85])
        with img_col:
            st.image('KT.PNG', width=80)
        with text_col:
            st.subheader('KT 위즈')
        st.write('=> 창단연도: 2013년')
        st.write('=> 연고지: 수원')
        st.caption('#연고지란: 스포츠에서 구단이 홈구장을 두고, 구단 존립의 근거로 하는 지역')
        st.write('=> 홈구장: 수원 KT 위즈 파크')
        st.write('=> 우승 횟수: 1회 (2021)')
        st.image('빅또리.PNG', width=200)
    elif team == '삼성 라이온즈':
        img_col, text_col = st.columns([0.15, 0.85])
        with img_col:
            st.image('삼성.PNG', width=80)
        with text_col:
            st.subheader('삼성 라이온즈')
        st.write('=> 창단연도: 1982년')
        st.write('=> 연고지: 대구')
        st.caption('#연고지란: 스포츠에서 구단이 홈구장을 두고, 구단 존립의 근거로 하는 지역')
        st.write('=> 홈구장: 대구 삼성 라이온즈 파크')
        st.write('=> 우승 횟수: 8회 (1985, 2002, 2005, 2006, 2011~2014)')
        st.image('블레오.PNG', width=200)
    elif team == 'KIA 타이거즈':
        img_col, text_col = st.columns([0.15, 0.85])
        with img_col:
            st.image('기아.PNG', width=80)
        with text_col:
            st.subheader('KIA 타이거즈')
        st.write('=> 창단연도: 2001년')
        st.write('=> 연고지: 광주')
        st.caption('#연고지란: 스포츠에서 구단이 홈구장을 두고, 구단 존립의 근거로 하는 지역')
        st.write('=> 홈구장: 기아 챔피언스 필드')
        st.write('=> 우승 횟수: 12회 (1983, 1986~1989, 1991, 1993, 1996, 1997, 2009, 2017, 2024)')
        st.image('호걸호연.PNG', width=200)
    elif team == '롯데 자이언츠':
        img_col, text_col = st.columns([0.15, 0.85])
        with img_col:
            st.image('롯데.PNG', width=80)
        with text_col:
            st.subheader('롯데 자이언츠')
        st.write('=> 창단연도: 1982년')
        st.write('=> 연고지: 부산')
        st.caption('#연고지란: 스포츠에서 구단이 홈구장을 두고, 구단 존립의 근거로 하는 지역')
        st.write('=> 홈구장: 사직 야구장')
        st.write('=> 우승 횟수: 2회 (1984, 1992)')
        st.image('윈지.PNG', width=200)
    elif team == 'NC 다이노스':
        img_col, text_col = st.columns([0.15, 0.85])
        with img_col:
            st.image('NC.PNG', width=80)
        with text_col:
            st.subheader('NC 다이노스')
        st.write('=> 창단연도: 2011년')
        st.write('=> 연고지: 창원')
        st.caption('#연고지란: 스포츠에서 구단이 홈구장을 두고, 구단 존립의 근거로 하는 지역')
        st.write('=> 홈구장: 창원NC파크')
        st.write('=> 우승 횟수: 1회 (2020)')
        st.image('단디.PNG', width=200)
    elif team == '한화 이글스':
        img_col, text_col = st.columns([0.15, 0.85])
        with img_col:
            st.image('한화.PNG', width=80)
        with text_col:
            st.subheader('한화 이글스')
        st.write('=> 창단연도: 1986년')
        st.write('=> 연고지: 대전')
        st.caption('#연고지란: 스포츠에서 구단이 홈구장을 두고, 구단 존립의 근거로 하는 지역')
        st.write('=> 홈구장: 대전 한화생명 볼파크')
        st.write('=> 우승 횟수: 1회 (1999)')
        st.image('수리.PNG', width=200)
    st.markdown("------")
    st.link_button('⚾️KBO 공식 홈페이지', 'https://www.koreabaseball.com/Default.aspx')
    st.markdown("---")
    st.subheader("❕야구팀 응원 댓글")
    if 'b_posts' not in st.session_state:
        st.session_state['b_posts'] = []
    nb_post = st.text_area('좋아하는 야구팀과 응원메세지/자랑글을 남겨주세요!',
                           height=100,
                           key='baseball_input')
    if st.button('공유하기', key = 'baseball_share'):
        if nb_post:
            st.session_state['b_posts'].insert(0, nb_post)
            st.success('댓글이 공유되었습니다!')
    if st.session_state['b_posts']:
        st.subheader('다른 사람들의 댓글')
        for post in st.session_state['b_posts']:
            st.write(f'💬 {post}')
            st.markdown("---")
    else:
        st.info('아직 공유된 댓글이 없습니다. 첫 댓글을 남겨보세요!')
        st.markdown("---")
    st.button('🏠 홈으로 돌아가기', on_click=change_page, args=['home'])
elif st.session_state['page'] == 'movie':
    st.title("📽️ 영화감상")
    st.header("🍀영화 입문 가이드!")
    st.subheader("🎧장르별 추천")
    movies = {
        '액션': [
    {
        '영화명': '부산행',
        '파일명': '부산행.PNG',
        '등급': '15세 이상 관람가',
        '개봉일': '2016년 7월 20일',
        '배우': '공유, 정유미, 마동석',
        '예고편': 'https://www.youtube.com/watch?v=UOTOjA0ngmk'
    },
    {
        '영화명': '밀수',
        '파일명': '밀수.PNG',
        '등급': '15세 이상 관람가',
        '개봉일': '2023년 7월 26일',
        '배우': '김혜수, 염정아, 조인성',
        '예고편': 'https://www.youtube.com/watch?v=Yh7J-HhXZjw'
    }
        ],
        '코미디': [
    {
        '영화명': '극한직업',
        '파일명': '극한직업.PNG',
        '등급': '15세 이상 관람가',
        '개봉일': '2019년 1월 23일',
        '배우': '류승룡, 이하늬',
        '예고편': 'https://www.youtube.com/watch?v=BaIRaKXrLPk'
    },
    {
        '영화명': '청년경찰',
        '파일명': '청년경찰.PNG',
        '등급': '15세 이상 관람가',
        '개봉일': '2017년 8월 9일',
        '배우': '박서준, 강하늘',
        '예고편': 'https://www.youtube.com/watch?v=uflYEv_0JoY'
    },
    {
        '영화명': '미스터 빈',
        '파일명': '미스터빈.PNG',
        '등급': '전체 관람가',
        '개봉일': '2007년 8월 15일',
        '배우': '로완 앳킨슨',
        '예고편': 'https://www.youtube.com/watch?v=LZfIzJ6XwPQ'
    }
        ],
        '로맨스': [
    {
        '영화명': '말할 수 없는 비밀',
        '파일명': '말할수없는비밀.PNG',
        '등급': '12세 이상 관람가',
        '개봉일': '2008년 1월 10일',
        '배우': '주걸륜, 계륜미',
        '예고편': 'https://www.youtube.com/watch?v=Ceoe2wf-bbo'
    },
    {
        '영화명': '라라랜드',
        '파일명': '라라랜드.PNG',
        '등급': '12세 이상 관람가',
        '개봉일': '2016년 12월 7일',
        '배우': '라이언 고슬링, 엠마 스톤',
        '예고편': 'https://www.youtube.com/watch?v=DBUXcNTjviI'
    },
    {
        '영화명': '로미오와 줄리엣',
        '파일명': '로미오.PNG',
        '등급': '15세 이상 관람가',
        '개봉일': '1996년 12월 28일',
        '배우': '레오나르도 디카프리오, 클레어 데인즈',
        '예고편': 'https://www.youtube.com/watch?v=MQNbf8aBPs4'
    }
        ],
        '판타지': [
    {
        '영화명': '이상한 나라의 앨리스',
        '파일명': '앨리스.PNG',
        '등급': '전체 관람가',
        '개봉일': '2010년 3월 4일',
        '배우': '미아 바시코브스카, 조니 뎁',
        '예고편': 'https://www.youtube.com/watch?v=9POCgSRVvf0'
    },
    {
        '영화명': '해리포터 시리즈',
        '파일명': '해리포터.PNG',
        '등급': '전체 관람가',
        '개봉일': '(1편 기준) 2001년 12월 14일',
        '배우': '다니엘 래드클리프, 엠마 왓슨, 루퍼트 그린트',
        '예고편': 'https://www.youtube.com/watch?v=PbdM1db3JbY'
    },
    {
        '영화명': '찰리와 초콜릿 공장',
        '파일명': '찰리.PNG',
        '등급': '전체 관람가',
        '개봉일': '2005년 9월 16일',
        '배우': '조니 뎁, 프레디 하이모어',
        '예고편': 'https://www.youtube.com/watch?v=hflg1arvGaU'
    }
        ],
        '애니메이션': [
    {
        '영화명': '너의이름은',
        '파일명': '너의이름은.PNG',
        '등급': '12세 이상 관람가',
        '개봉일': '2017년 1월 4일',
        '배우': '-',  
        '예고편': 'https://www.youtube.com/watch?v=enRm-9qF2L8'
    },
    {
        '영화명': '주토피아',
        '파일명': '주토피아.PNG',
        '등급': '전체 관람가',
        '개봉일': '2016년 2월 17일',
        '배우': '-',
        '예고편': 'https://www.youtube.com/watch?v=K4OJXmoakF4'
    },
    {
        '영화명': '미니언즈',
        '파일명': '미니언즈.PNG',
        '등급': '전체 관람가',
        '개봉일': '2015년 7월 29일',
        '배우': '-',  
        '예고편': 'https://www.youtube.com/watch?v=hpfJ8S1Q4KI'
    }
        ]
    }
    option_movies = list(movies.keys())
    genre = st.selectbox('좋아하는 장르를 선택해주세요' , options=option_movies)
    display_movies = movies.get(genre, [])
    st.subheader(f"추천 {genre} 영화")
    for i in display_movies:
        img_col, info_col = st.columns([0.4, 0.6])
        with img_col:
            st.image(
                i['파일명'], width=300
            )
        with info_col:
            st.subheader(f'{i["영화명"]}')
            st.write(f'등급: {i["등급"]}')
            st.write(f'개봉일: {i["개봉일"]}')
            st.write(f'출연: {i["배우"]}')
            st.link_button('예고편 바로가기', url=f'{i["예고편"]}')
        st.markdown("---")
    st.subheader("🎧명대사 모음")
    quotes = [
        {"quote": "눈을 감지 말고 똑바로 봐. 두려움의 실체는 생각과 다를 수 있어.", "movie": "니모를 찾아서"},
        {"quote": "길은 모두에게 열려있지만 모두가 그 길을 가질 수 있는 건 아니다.", "movie": "인턴"},
        {"quote": "부자인데 착한 게 아니고 부자라서 착한 거야.", "movie": "기생충"},
        {"quote": "소중한 시간을 진짜 자신을 끌어내는데 쓰세요", "movie": "소울"},
        {"quote": "두려움은 당신을 포로로 묶어 놓지만, 희망은 당신을 자유롭게 한다.", "movie": "쇼생크 탈출"},
        {"quote": "지구가 둥근 이유는, 멀리 있는 그대롤 보지 못하게 하기 위해서예요.", 'movie': "아웃 오브 아프리카"}
    ]
    for q in quotes:
        st.write(f'💬 "{q["quote"]}" - {q["movie"]}')
    st.markdown("------")
    st.subheader("🎧영화 추천 댓글")
    if 'm_posts' not in st.session_state:
        st.session_state['m_posts'] = []
    nm_post = st.text_area('좋아하는 영화/명대사를 남겨주세요!',
                           height=100,
                           key='m_input')
    if st.button('공유하기', key = 'movie_share'):
        if nm_post:
            st.session_state['m_posts'].insert(0, nm_post)
            st.success('댓글이 공유되었습니다!')
    if st.session_state['m_posts']:
        st.subheader('다른 사람들의 댓글')
        for post in st.session_state['m_posts']:
            st.write(f'💬 {post}')
            st.markdown("---")
    else:
        st.info('아직 공유된 댓글이 없습니다. 첫 댓글을 남겨보세요!')
        st.markdown("---")
    st.button('🏠 홈으로 돌아가기', on_click=change_page, args=['home'])
elif st.session_state['page'] == 'idol':
    st.title("🎤 아이돌")
    st.header("🍀아이돌 입문 가이드!")
    st.subheader("💿덕질 용어 정리")
    st.write("💬입덕 : 덕질 시작")
    st.write("💬탈덕 : 덕질 끝")
    st.write("💬늦덕 : 늦게 덕질하기 시작한 팬")
    st.write("💬머글 : 해리포터에서 유래된 말로 팬이 아닌 일반인")
    st.write("💬일코 : 일반인 코스프레")
    st.write("💬스밍 : 스트리밍")
    st.write("💬음방 : 음악방송")
    st.write("💬팬싸 : 팬싸인회")
    st.write("💬떡밥 : 새로 알게된 아티스트 관련된 정보 & 스케줄")
    st.write("💬굿즈 : 아티스트 관련 상품")
    st.write("💬포카 : 포토카드")
    st.markdown("---")
    st.subheader("💿아이돌 그룹 소개")
    groups = {
'밴드🎸': [
    {'그룹명': 'DAY6', '파일명': 'DAY6.PNG', '데뷔': '2015년 9월 7일', '소속사': 'JYP', '멤버': '성진, Young K , 원필, 도운', '대표곡': '한 페이지가 될 수 있게, 예뻤어', '유튜브': 'https://www.youtube.com/@DAY6Official'},
    {'그룹명': 'LUCY', '파일명': 'LUCY.PNG', '데뷔': '2020년 5월 8일', '소속사': '미스틱스토리', '멤버': '신예찬, 최상엽, 조원상, 신광일', '대표곡': '개화, 아니 근데 진짜', '유튜브': 'https://www.youtube.com/@LUCYISLAND'},
    {'그룹명': '엔플라잉', '파일명': '엔플라잉.PNG', '데뷔': '2015년 5월 20일', '소속사': 'FNC엔터테인먼트', '멤버': '이승협, 차훈, 김재현, 유회승, 서동성', '대표곡': '옥탑방, Blue Moon', '유튜브': 'https://www.youtube.com/@nflyingofficial'},
    {'그룹명': '잔나비', '파일명': '잔나비.PNG', '데뷔': '2014년 4월 28일', '소속사': '페포니뮤직', '멤버': '최정훈, 김도형', '대표곡': '주저하는 연인들을 위해, 사랑하긴 했었나요 스쳐가는 인연이었나요 짧지않은 우리 함께했던 시간들이 자꾸 내 마음을 가둬두네', '유튜브': 'https://www.youtube.com/@BandJannabi'},
],
'보이그룹🕺': [
    {'그룹명': 'NCT DREAM', '파일명': 'DREAM.PNG', '데뷔': '2016년 8월 25일', '소속사': 'SM엔터테인먼트', '멤버': '마크, 런쥔, 제노, 해찬, 재민, 천러, 지성', '대표곡': 'Hello Future, Candy', '유튜브': 'https://www.youtube.com/@NCTDREAM'},
    {'그룹명': 'NCT WISH', '파일명': 'WISH.PNG', '데뷔': '2024년 2월 21일', '소속사': 'SM엔터테인먼트', '멤버': '시온, 리쿠, 유우시, 재희, 료, 사쿠야', '대표곡': 'Steady, WISH', '유튜브': 'https://www.youtube.com/@NCTWISH'},
    {'그룹명': 'TXT', '파일명': 'TXT.PNG', '데뷔': '2019년 3월 4일', '소속사': '빅히트 뮤직', '멤버': '연준, 수빈, 범규, 태현, 휴닝카이', '대표곡': '9와 4분의 3 승장강에서 너를 기다려, Sugar Rush Ride', '유튜브': 'https://www.youtube.com/@TXT_bighit'},
    {'그룹명': 'BOYNEXTDOOR', '파일명': 'BND.PNG', '데뷔': '2023년 5월 30일', '소속사': 'KOZ엔터테인먼트', '멤버': '성호, 리우, 명재현, 태산, 이한, 운학', '대표곡': '오늘만 I LOVE YOU, Earth, Wind&Fire', '유튜브': 'https://www.youtube.com/@boynextdoor_official'},
    {'그룹명': 'RIIZE', '파일명': 'RIIZE.PNG', '데뷔': '2023년 9월 4일', '소속사': 'SM엔터테인먼트', '멤버': '쇼타로, 은석, 성찬, 원빈, 소희, 앤톤', '대표곡': 'Get A Guitar, Boom Boom Bass', '유튜브': 'https://www.youtube.com/@RIIZE_official'},
],
'걸그룹💃': [
    {'그룹명': 'aespa', '파일명': '에스파.PNG', '데뷔': '2020년 11월 17일', '소속사': 'SM엔터테인먼트', '멤버': '카리나, 지젤, 윈터, 닝닝', '대표곡': 'Next Level, Supernova', '유튜브': 'https://www.youtube.com/@aespa'},
    {'그룹명': 'IVE', '파일명': 'IVE.PNG', '데뷔': '2021년 12월 1일', '소속사': '스타쉽엔터테인먼트', '멤버': '안유진, 가을, 레이, 장원영, 리즈, 이서', '대표곡': 'Eleven, Love Dive', '유튜브': 'https://www.youtube.com/@IVEstarship'},
    {'그룹명': 'ILLIT', '파일명': '아일릿.PNG', '데뷔': '2024년 3월 25일', '소속사': '빌리프랩', '멤버': '윤아, 민주, 모카, 원희, 이로하', '대표곡': 'Magnetic, Cherish', '유튜브': 'https://www.youtube.com/@ILLIT_official'},
    {'그룹명': 'KISS OF LIFE', '파일명': '키오프.PNG', '데뷔': '2023년 7월 5일', '소속사': 'S2엔터테인먼트', '멤버': '쥴리, 나띠, 벨, 하늘', '대표곡': 'Sticky, Midas Touch', '유튜브': 'https://www.youtube.com/@KISSOFLIFE_official'},
    {'그룹명': '아이들', '파일명': '아이들.PNG', '데뷔': '2018년 5월 2일', '소속사': '큐브엔터테인먼트', '멤버': '미연, 민니, 소연, 우기, 슈화', '대표곡': 'TOMBOY, Nxde', '유튜브': 'https://www.youtube.com/@official_i_dle'},
],
'혼성/솔로🎼': [
    {'그룹명': 'ALL DAY PROJECT', '파일명': '올데프.PNG', '데뷔': '2025년 6월 23일', '소속사': 'THEBLACKLABEL', '멤버': '애니, 타잔, 베일리, 우찬, 영서', '대표곡': 'FAMOUS, WICKED', '유튜브': 'https://www.youtube.com/@ALLDAY_PROJECT'},
    {'그룹명': '아이유', '파일명': '아이유.PNG', '데뷔': '2008년 9월 18일', '소속사': '이담엔터테인먼트', '멤버': '-', '대표곡': '밤편지, Blueming', '유튜브': 'https://www.youtube.com/@dlwlrma'},
    {'그룹명': '이무진', '파일명': '이무진.PNG', '데뷔': '2018년 5월 4일', '소속사': '빅플래닛메이드엔터', '멤버': '-', '대표곡': '에피소드, 청춘만화', '유튜브': 'https://www.youtube.com/@LEEMUJINofficial'},
    {'그룹명': '10cm', '파일명': '10cm.PNG', '데뷔': '2010년 4월 22일', '소속사': '씨에이엠위더스', '멤버': '-', '대표곡': '그라데이션, 서랍', '유튜브': 'https://www.youtube.com/@10CMofficial_channel'},
    {'그룹명': '악뮤', '파일명': '악뮤.PNG', '데뷔': '2014년 4월 7일', '소속사': 'YG엔터테인먼트', '멤버': '이찬혁, 이수현', '대표곡': '오랜 날 오랜 밤, DINOSAUR ', '유튜브': 'https://www.youtube.com/@AKMU'},
]
            }
    CATEGORY_OPTIONS = list(groups.keys())
    team = st.selectbox("알아보고 싶은 그룹 종류를 선택하세요"
                 , options=CATEGORY_OPTIONS)
    display = groups.get(team, [])
    st.subheader(f"추천 {team}")
    for g in display:
        img_col, info_col = st.columns([0.4, 0.6])
        with img_col:
            st.image(
                g['파일명'], width=700
            )
        with info_col:
            st.subheader(f'{g["그룹명"]}')
            st.write(f'데뷔: {g["데뷔"]}')
            st.write(f'소속사: {g["소속사"]}')
            st.write(f'멤버: {g["멤버"]}')
            st.write(f'대표곡: {g["대표곡"]}')
            st.link_button('유튜브 바로가기', url=f'{g["유튜브"]}')
        st.markdown("---")
    st.subheader("💿아이돌 소개 댓글")
    if 'i_posts' not in st.session_state:
        st.session_state['i_posts'] = []
    ni_post = st.text_area('좋아하는 아이돌을 자랑해주세요!',
                           height=100,
                           key='idol_input')
    if st.button('공유하기', key = 'idol_share'):
        if ni_post:
            st.session_state['i_posts'].insert(0, ni_post)
            st.success('댓글이 공유되었습니다!')
    if st.session_state['i_posts']:
        st.subheader('다른 사람들의 댓글')
        for post in st.session_state['i_posts']:
            st.write(f'💬 {post}')
            st.markdown("---")
    else:
        st.info('아직 공유된 댓글이 없습니다. 첫 댓글을 남겨보세요!')
        st.markdown("---")
    st.button('🏠 홈으로 돌아가기', on_click=change_page, args=['home'])
elif st.session_state['page'] == 'book':
    st.title("📚 독서")
    st.header("🍀독서 입문 가이드!")
    st.subheader("🌼장르별 추천")
    recommend_books = {
        '소설': [
            {'제목': '내가 죽기 일주일 전', '사진명': '내죽일.PNG', '작가': '서은채', '책소개': '오래 전에 죽은 첫사랑이 저승사자가 되어 찾아오는 이야기를 그린 감성 미스터리 판타지 소설. "저승사자는 사랑하는 사람의 모습을 하고 찾아온다"라는 무서움과 호기심을 동시에 불러일으키는 문구로 시작되는 이 작품은 황금가지의 온라인 소설 플랫폼 브릿G 연재를 통해 계약된 최초의 경장편이기도 하다.'},
    {'제목': '나미야 잡화점의 기적', '사진명': '나잡기.PNG', '작가': '히가시노 게이고', '책소개': '인생의 중요한 고비마다 찾아가고 싶은 우체통, 평범하지만 뭔가 하나를 마음속에 꼭 붙잡고 있는 우리들에게 보내는 답신과도 같은 소설. 『나미야 잡화점의 기적』은 아직도 저에게는 ‘오래도록 남을 명작’입니다._옮긴이 양윤옥'},
    {'제목': '소년이 온다', '사진명': '소온.PNG', '작가': '한강', '책소개': '책장을 덮어도 결코 잊을 수 없는 이야기. 끝나지 않는 오월, 피지 못한 아이들의 영혼을 위한 간절한 노래 -책 소개 중'},
    {'제목': '구의 증명', '사진명': '구증.PNG', '작가': '최진영', '책소개': '"만약 네가 먼저 죽는다면 나는 너를 먹을 거야. 그래야 너 없이도 죽지 않고 살 수 있어." 사랑 후 남겨진 것들에 관한 숭고할 만큼 아름다운 이야기 -책 소개 중'},
        ],
        '시집': [
            {'제목': '꽃을 보듯 너를 본다', '사진명': '꽃너.PNG', '작가': '나태주', '책소개': '만인의 심금을 울릴 수 있는 서정시의 진수. 평범한 것에 아름다움을 보는 눈, 별 볼일 없다고 생각했던 무언가를 다시보게 하는 힘이 이 시집에 있다. -책 소개 중'},
    {'제목': '나는 오래된 거리처럼 너를 사랑하고', '사진명': '나오.PNG', '작가': '진은영', '책소개': '“한 사람을 조금 덜 외롭게 해보려고 애쓰던 시간들이 흘러갔다.” 우리 삶 속에 상실과 슬픔을 끌어안는 사랑의 공통감각, 십 년을 기다려온 단 하나의 온전한 고백. 누추한 현실에서 불현듯 아름다움을 발견하는 시인 진은영 10년 만의 신작 시집'},
    {'제목': '없음의 대명사', '사진명': '없대.PNG', '작가': '오은', '책소개': '“없음은 있었음을 끊임없이 두드릴 것이다." ‘웃음’과 ‘울음’이 나란히 놓이고 ‘무표정’으로 ‘표정’을 지을 때 ‘없다’와 ‘있었다’ 사이에서 떠오르는 ‘잃었다’의 자리 -책 소개 중'},
    {'제목': '하늘과 바람과 별과 시', '사진명': '하늘바람별시.PNG', '작가': '윤동주', '책소개': '한국인이 가장 사랑하는 시인, 윤동주. 그가 남긴 단 하나의 유고시집 〈하늘과 바람과 별과 詩〉. 끊임없는 자아 성찰을 통한 시작(詩作)으로 민족의 암울한 시대를 위로한 시인, 윤동주의 단 하나의 시집! -책 소개 중'},
        ],
        '과학': [
            {'제목': '코스모스', '사진명': '코스모스.PNG', '작가': '칼 세이건', '책소개': '현대 천문학을 대표하는 저명한 과학자인 칼 세이건이 완성한 과학 교양서의 고전.'},
    {'제목': '이기적 유전자', '사진명': '이유.PNG', '작가': '리쳐드 도킨스', '책소개': '독특한 발상과 놀라운 주장으로 40여 년간 수많은 찬사와 논쟁의 중심에 선 과학 교양서의 바이블'},
    {'제목': '사피엔스', '사진명': '사피엔스.PNG', '작가': '유발 하라리', '책소개': '“인공지능의 시대, 우리가 알아야 할 것은 코딩보다 인간의 마음.” 인간의 역사와 미래에 대한 가장 논쟁적이고 대담한 대서사'},
        ]
    }
    book_options = list(recommend_books.keys())
    book = st.selectbox('좋아하는 책 장르를 선택해주세요', options=book_options)
    display_books = recommend_books.get(book, [])
    st.subheader(f"추천 {book} 도서")
    for b in display_books:
        img_col, info_col = st.columns([0.3, 0.7])
        with img_col:
            st.image(
                b['사진명'], width=400
            )
        with info_col:
            st.subheader(f'{b["제목"]}')
            st.write(f'작가: {b["작가"]}')
            st.write(f'책소개: {b["책소개"]}')
        st.markdown("-----")
    st.subheader("🌼독서템 추천")
    items = [
    {
        '제품명': '1. 아크릴 페이퍼 문진',
        '파일명': '추천1.PNG',
        '기능': '필사할 때 유용하게 사용!'
    },
    {
        '제품명': '2. 클립조명',
        '파일명': '추천2.PNG',
        '기능': '잠들기 전 침대에서 도서감상할 때 사용!'
    },
    {
        '제품명': '3. 북홀더',
        '파일명': '추천3.PNG',
        '기능': '한 손으로 책 들고 읽을 때 유용하게 사용!'
    },
    {
        '제품명': '4. 펜클립',
        '파일명': '추천4.PNG',
        '기능': '책 읽으며 메모하고 싶은 부분에 편하게 사용!'
    },
    {
        '제품명': '5. 북커버',
        '파일명': '추천5.PNG',
        '기능': '가방 속 책에 흠집나지 않게 보호할 때 사용!'
    }
]
    for z in items:
        img_col, info_col = st.columns([0.3, 0.7])
        with img_col:
            st.image(
                z['파일명'], width=400
            )
        with info_col:
            st.subheader(f'{z["제품명"]}')
            st.write(f'{z["기능"]}')
    st.markdown("-----")

    st.button('🏠 홈으로 돌아가기', on_click=change_page, args=['home'])

