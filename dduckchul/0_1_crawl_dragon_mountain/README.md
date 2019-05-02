# 용산 CGV 크롤러

* 파이썬 라이브러리를 이용한 웹 크롤링 + 메신저 전송 서비스

## 1. 준비물
- 파이썬 3.? 버전
  - pip 설치 가능하도록 / 아래 라이브러리들 호환
  - 파이썬 라이브러리들
    - Html Parser
      - beatifulsoup
    - 메신저 라이브러리
      - 텔레그램 라이브러리
      - 디스코드 라이브러리
    
- 텔레그램 봇
- 디스코드 서버
- 네이버 영화 API
    
## 2. 준비단계
  1. 파이썬 3.? 버전 설치
  2. pip로 필요한 라이브러리들 설치
```python
# HTML 파싱
pip install beautifulsoup4

# HTTP 리퀘스트 쉽게 날리는 라이브러리
pip install requests

# 메신저 전송하기 위한 라이브러라
pip install python-telegram-bot
pip install discord.py
``` 
## 3. crawl_dragon_mountain.py
### CGV의 용산 특별관 정보 긁어오는 작업 수행
* make_soup(url) : url 입력하면 해당하는 url의 soup 객체 반환
* crawl_schedules(url) : url 대상 파싱, 파싱후 result라는 파싱 결과 dictionary 만들어서 저장해둠
* compare_file(result) : 이전 크롤링 결과 값 (theater.json) 과 현재 크롤링 한 result dictionary 비교해 차이 비교하는 dictionary
* make_file(result) : 현재 크롤링 결과 값을 json파일로 미리 만들어둔다

## 4. messengers.py
### 메신저 및 네이버 영화 API 콜 해서 템플릿 만든 후 전송
* make_plain_messages : 스트링 형태의 영화 파싱 리스트 반환
* make_telegram_messages : 텔레그램 라이브러리 사용하여 inlinebutton object로 만들어둔다
* telegram_messaging : 위에서 작성한 텔레그램 메시지 실제로 봇 서버로 전송
* discord_messageing : 위에서 작성한 메시지 디스코드 서버로 전송
* naver_movie_request : 메시지 만들때 네이버 영화 api 검색하여 이미지, 네이버 영화 유저평점 가져온다

## 5. 참고자료
* 뷰티풀 숲 - https://www.crummy.com/software/BeautifulSoup/
* 텔레그램 파이썬 라이브러리 - https://python-telegram-bot.org/
* 디스코드 파이썬 라이브러리 - https://pypi.org/project/discord.py/
* 쉽게 시작하는 텔레그램 봇 - https://steemit.com/kr-dev/@maanya/30
* 네이버 영화 API - https://developers.naver.com/docs/search/movie/