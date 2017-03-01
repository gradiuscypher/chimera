import requests
import hashlib
from bs4 import BeautifulSoup


def login(domain, username, password):
    login_url = domain + "/login.php?do=login"
    md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
    body = {
        'do': 'login',
        'vb_login_md5password': md5,
        'vb_login_md5password_utf': md5,
        's': '',
        'vb_login_username': username,
        'security_token': 'guest'
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'es-es,es;q=0.8,en-us;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
        'Connection': 'keep-alive',
        'Referer': login_url,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Lenght': '205'
    }

    result = requests.post(login_url, data=body, headers=headers)
    return result


def get_index(domain, cookies):
    result = requests.get(domain, cookies=cookies)
    soup = BeautifulSoup(result.text, 'html.parser')
    threads = soup.find_all('td', {'class': 'alt1Active'})

    for thread in threads:
        print(thread.find('a').text)


def get_forum_threads(domain, cookies, forum_id):
    # TODO: Need way to select pages.
    # TODO: is last result correct?
    result = requests.get(domain + "/forumdisplay.php?f={}".format(forum_id), cookies=cookies)
    soup = BeautifulSoup(result.text, 'html.parser')
    post_list = soup.find('tbody', {'id': 'threadbits_forum_{}'.format(forum_id)})
    posts = post_list.find_all('tr')

    for p in posts:
        print(p.div.a)


def get_thread(domain, cookies, thread_id):
    result = requests.get(domain + "/showthread.php?t={}".format(thread_id), cookies=cookies)
    soup = BeautifulSoup(result.text, 'html.parser')
    return soup
