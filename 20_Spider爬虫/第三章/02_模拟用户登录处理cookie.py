# _*_ coding : utf-8 _*_
# @Time : 2024/8/10 16:26
# @Author : chalet.you
# @File : 02_模拟用户登录处理cookie
# @Project : bigdata_python_course

# 登录 -> 得到cookie
# 带着cookie 去请求到书架url -> 书架上的内容

# 必须得把上面得两个操作连起来
# 我们可以使用session进行请求 -> session你可以认为是一连串得请求。在这个过程中得cookie不会丢失
import requests

# 会话
session = requests.session()

data = {
    "user": "18721055830",
    "password": "Youxuan52188"
}

# 1.登录
url = "https://passport.17k.com/login/"
resp = session.post(url, data=data)
print(resp.status_code)
print(resp.text)
print(resp.cookies)  # 看cookie

# 2.拿书架上的数据
# # 刚才的哪个session中是由cookie的
# resp = session.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919')
# print(resp.json())


# resp = requests.get('https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919', headers={"cookie":"GUID=d1c7bfe0-55d8-4c91-bce5-440741440c34; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1722862300,1723278399; HMACCOUNT=9C4E23BE0B87EC89; acw_sc__v2=66b72be30ef7179b8902517fa9503222ef11ce6d; ssxmod_itna=QqAxgD0DcQ0==YKGHmojxmOGxBDheQK7bq3FDlxEYxA5D8D6DQeGTb2eCYb7Y73i0ExfGqmDOe4a4HKCoxD9jm3PoDU4i8DCkqbbD4fKGwD0eG+DD4DWDmnFDnxAQDjxGpnXvTs=DEDmb8DWPDYxDrE=KDRxi7DDydOx07DQ5kYDDzYjo4KDGiuiiGKIp+RooCq7B5ExG1W40H3Dd4Eg7ju+DzKfS5VhR7DlF0DCK1RpyFb4GdjEH1VcqxAGxxb0T5bAG3qDx5KiD4qepcohxeqlqSFvxxIGrejQhlHqDWiG0eCA6DD=; ssxmod_itna2=QqAxgD0DcQ0==YKGHmojxmOGxBDheQK7bq3iD6h4hx7TnDDsi67DLA2O5+i02Pqh=Y9BnYA6xPwxAP+3xSQE6wQa9RFLIH6OAohjWk+PknKPMttjHImufKCWjHVtp=Bka2vIg/AyYf3pUo3+ebdEYSXhbTY+8rxmYRd5PLbGYSrmYCKCKSAQPdWQZnLiwmAkQ13bqjTPMmurpCEicSRtP4YCLeq4AcPYAZwhwjbwZl+hXp2wfCa5rDEeoi8he4ake4wtp+nqMzR0HSKX5Vk235F+mRdc6oRRgl1GW+Eg6EZ7jvTM1PjMZKDRExbUlot/aLqIUPbfDSi=2tOE6pYeEGhjgYFGehQDnhxEOYCYQdI3b90COEPbEPfjbUqUZbQeuPSjP4RWRbEnDtG4DQKxYidBG4Qc9Q2i72te3r=afiS5DeKvhwB0GziHiG0/0iB0=0DFxrYwIbQ2TKid/PHhD43L4e+xQSiW0CAxt8G8um4tuDjdk2DDFqD+O6G+y4Qw7UaYYD==; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F01%252F21%252F18%252F103691821.jpg-88x88%253Fv%253D1722862362000%26id%3D103691821%26nickname%3Dchalet%26e%3D1738833592%26s%3Dce26c7816732707e; tfstk=fTcst0s5JGjsU_uQmRLUdGnmHGNjGcOy1ZaxrqCNk5FtkSgxoora3okQ9zngHfPZ7DTjv00a35hjKsgoof8ggFViSSVv43RrcV0gijvBZnG_96USJ1UTkFuDeRPv43RFLweMbSHVvSQKR2E3lPQTBmQpRra0M1eA69ILxrFYDmEY9yU0uPITHlBKMy77ldZi5eQiyrXDGMm0AsC5rP2OzVWVw_hY5RGxWka_5Xa_Cueed5SE6Dux_f2HCOFm8YijH0KFQlH7PDwrC31sVc4xlrn6ZaZK1qGQIvSOBzN_f8hTeI5j5-HIO5l9mT0ERle7TvJHb-PsfYquBpxnc2ZZDfwdfHrqU2lTd0KFOm2jHfPK6Hd54j5zVgOchwwlMyZyRe6c3r2DiM609L2bBy4_LeTCXx2T-yZyRe6cnRU35z8BRGHc.; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22103691821%22%2C%22%24device_id%22%3A%2219122986c5a50a-043e8721c8d034-26001e51-2073600-19122986c5c7ea%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22d1c7bfe0-55d8-4c91-bce5-440741440c34%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1723281656"})
# print([li['bookName'] for li in resp.json()['data']])
#
