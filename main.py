import requests
import urllib3
import time
import json

def get_all_school_code():
    url = "https://weiban.mycourse.cn/pharos/login/getTenantListWithLetter.do"
    r = requests.post(url)
    #print(r.text)
    res = json.loads(r.text)
    return res
def search_school_code_by_school_name(name,school_infos):
    for zimu in school_infos['data']:
        for school in zimu['list']:
            if name in school['name']:
                print('学校全名为：' + school['name'])
                print('学校代码为：'+school['code'])
                return school
    print('为搜索到您的学校，请尝试其他方法获取学校代码')
    return ''

school_infos = get_all_school_code()
school_info = search_school_code_by_school_name(input('请输入您的学校全名:'),school_infos)
print('学校提示：'+school_info['popPrompt'])
print('学校提示[用户名]：'+school_info['userNamePrompt'])
print('学校提示[密码]：'+school_info['passwordPrompt'])
username = input('请输入用户名：')
password = input('请输入密码：')
