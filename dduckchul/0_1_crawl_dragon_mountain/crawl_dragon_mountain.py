import requests, time, datetime, re, json, os, locale
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse, parse_qsl, urljoin, urlencode, urlunparse
from messengers import telegram_messaging, discord_messaging

curr_date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d')

cgv_url = 'http://www.cgv.co.kr/common/showtimes/'
theater_url = str('./iframeTheater.aspx?areacode=01&theatercode=0013&date='+curr_date)
visited_urls = []

json_file = 'theater.json'
result = {}


# 페이지 읽어서 뷰티풀숲으로 만들기
def make_soup(url):
    req = requests.Session()
    res = req.get(url)
    soup = bs(res.text, 'html.parser')
    return soup


# 크롤해서 결과값 만들기
def crawl_schedules(url):
    visited_urls.append(url)
    date = dict(parse_qsl(urlparse(url).query)).get('date')
    soup = make_soup(url)
    movie_dict = dict()

    # 날짜 확인
    schedules = soup.find('div', class_='sect-schedule').find_all('div', class_='day')
    # 해당 날짜 상영 확인
    showtimes = soup.find('div', class_='sect-showtimes').find_all('div', class_='col-times')

    # 특별 상영관 찾기
    for show in showtimes:
        type_halls = show.find_all('div', class_='type-hall')
        info_movie = show.find('div', class_='info-movie')
        if type_halls:
            for type_hall in type_halls:
                info_hall = type_hall.find('div', class_='info-hall')
                info_timetable = type_hall.find('div', class_='info-timetable')
                if info_hall:
                    hall = info_hall.ul.li.string.strip().upper()
                    if "IMAX" in hall or "SCREENX" in hall or "4DX" in hall:
                        movie = info_movie.a.string.strip()
                        movie_dict[movie] = dict()
                        movie_dict[movie][hall] = dict()
                        # 특별 상영관 있으면 시간 찾기
                        if info_timetable:
                            for time in info_timetable.find_all('li'):
                                # 매진 아닌애들만 링크에 추가
                                if time.a:
                                    time_str = time.a.em.string
                                    movie_dict[movie][hall][time_str] = dict()
                                    movie_dict[movie][hall][time_str]['href'] = time.a['href']

    # 해당 페이지 파싱 결과 Result에 담아주기
    if movie_dict:
        result[date] = movie_dict

    # 일자별로 순환
    for day in schedules:
        schedule_link = day.a['href']

        # 주소 가져오는 곳에서 예외처리
        full_link = cgv_url + schedule_link
        full_link_list = list(urlparse(full_link))
        query = dict(parse_qsl(full_link_list[4]))
        query.pop('screenratingcode', None)
        full_link_list[4] = urlencode(query)
        parsed_full_link = urlunparse(full_link_list)

        if parsed_full_link not in visited_urls:
            crawl_schedules(parsed_full_link)


# 저장되어있는 파일과 현재 크롤링 결과값 비교
def compare_file(result):
    compare_result = {}
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            prev_result = json.load(f)
            for date, value in result.items():
                # 현재 크롤링 결과에 새로운 날짜 들어왔을때
                if date not in prev_result.keys():
                    compare_result.setdefault(date, {})
                    compare_result[date] = value
                    continue
                for movie, value2 in value.items():
                    # 현재 크롤링 결과애 새로운 영화 들어왔을 때
                    if movie not in prev_result[date].keys():
                        compare_result.setdefault(date, {}).setdefault(movie, {})
                        compare_result[date][movie] = value2
                        continue
                    for hall, value3 in value2.items():
                        #  현재 크롤링 결과에 새로운 영화관 들어왔을 때
                        if hall not in prev_result[date][movie].keys():
                            compare_result.setdefault(date, {}).setdefault(movie, {}).setdefault(hall, {})
                            compare_result[date][movie][hall] = value3
                            continue
                        for time, value4 in value3.items():
                            # 현재 크롤링 결과에 새로운 시간 들어왔을때
                            if time not in prev_result[date][movie][hall]:
                                compare_result.setdefault(date, {}).setdefault(movie, {}).setdefault(hall,
                                                                                                     {}).setdefault(
                                    time, {})
                                compare_result[date][movie][hall][time] = value4
                                continue
    return compare_result


# 크롤링결과 파일로 떨구기
def make_file(result):
    with open(json_file, 'w+') as f:
        f.write(json.dumps(result))

# 실제 호출
crawl_schedules(str(cgv_url + theater_url))
compare_result = compare_file(result)
make_file(result)

# telegram_messaging(compare_result)
# discord_messaging(compare_result)

print("==============json result==============")
print(result)
print("==============compare result==============")
print(compare_result)