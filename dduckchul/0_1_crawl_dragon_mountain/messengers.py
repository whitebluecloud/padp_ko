import telegram, discord, requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from discord import ChannelType
from dateutil import parser

telegram_info = {
    "token" : "텔레그램 토큰값",
    "test_chnl_id" : "테스트용으로 전송할 채널 아이디",
    "chnl_id" : "실제 전송할 채널 아이디"
}

discord_info = {
    '_TOKEN' : '디스코드 토큰 값',
    '_TEST_SERVER_NM' : '디스코드 테스트용 서버명',
    '_SERVER_NM' : '실제전송할 디스코드 서버 명',
    '_CHNL_NM' : '전송할 채널명'
}

headers = {
    'X-Naver-Client-Id': '네이버 클라이언트 id',
    'X-Naver-Client-Secret': '네이버 api 코드',
    'Content-Type' : 'application/json'
}


def make_plain_messages(compare_result):
    msg_list = []
    for date, value in compare_result.items():
        d = parser.parse(date)
        date_str = d.strftime('%Y/%m/%d')
        for movie, value2 in value.items():
            movie_str = movie
            for hall, value3 in value2.items():
                hall_str = hall
                time_str = ' '.join(value3.keys())
                for time, value4 in value3.items():
                    continue
                msg_str = date_str + ' ' + movie_str + ' ' + hall_str + ' ' + time_str
                msg_list.append(msg_str)
    return msg_list


def make_telegram_messages(compare_result):
    msg_list = []
    for date, value in compare_result.items():
        d = parser.parse(date)
        date_str = d.strftime('%Y/%m/%d') + '일 예매 시작'
        for movie, value2 in value.items():
            movie_str = movie
            naver_movie_info = naver_movie_request(movie_str)
            for hall, value3 in value2.items():
                hall_str = hall
                msg_dic = dict()
                temp_list = []
                time_list = list()
                for time, value4 in value3.items():
                    inlineKeyboardButton = InlineKeyboardButton(text=time, url='http://www.cgv.co.kr' + value4['href'])
                    temp_list.append(inlineKeyboardButton)
                time_list.append(temp_list)
                msg_str = date_str + '\n' + movie_str + '\n' + hall_str
                if naver_movie_info['user_rating']:
                    msg_str = msg_str + '\n' + '네이버 유저 평점 ' + '(' + naver_movie_info['user_rating'] + ')'
                if naver_movie_info['image']:
                    msg_dic['image'] = naver_movie_info['image']
                msg_dic['msg'] = msg_str
                msg_dic['inline'] = InlineKeyboardMarkup(time_list)
                msg_list.append(msg_dic)
    return msg_list


def telegram_messaging(compare_result):
    msg_list = make_telegram_messages(compare_result)
    bot = telegram.Bot(token=telegram_info['token'])
    for msg in msg_list:
        print(msg)
        if msg['image']:
            bot.sendPhoto(chat_id=telegram_info['chnl_id'], photo=msg['image'], caption=msg['msg'],
                          reply_markup=msg['inline'])
        else:
            bot.sendMessage(chat_id=telegram_info['chnl_id'], text=msg['msg'], reply_markup=msg['inline'])


def discord_messaging(compare_result):
    if compare_result:
        msg_list = make_plain_messages(compare_result)
        client = discord.Client()

        @client.event
        async def on_ready():
            print('Logged in')
            # 테스트용
            ch_movie_info = discord.utils.get(client.get_all_channels(), server__name=discord_info['_SERVER_NM'],
                                              name=discord_info['_CHNL_NM'], type=ChannelType.text)
            for msg in msg_list:
                await client.send_message(ch_movie_info, msg)
            await client.close()

        client.run(discord_info['_TOKEN'])


def naver_movie_request(movie_str):
    params = (
        ('query', movie_str),
        ('display', '1'),
        ('start', '1'),
    )
    response = requests.get('https://openapi.naver.com/v1/search/movie.json', headers=headers, params=params)
    naver_movie_info = response.json()
    if naver_movie_info['items']:
        print(naver_movie_info['items'][0])
        image = naver_movie_info['items'][0]['image']
        user_rating = naver_movie_info['items'][0]['userRating']
        return {'image': image, 'user_rating': user_rating}