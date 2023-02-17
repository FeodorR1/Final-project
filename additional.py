import re
import requests
import sqlite3
from bs4 import BeautifulSoup as BS


def parcing(text: str):
    url_dict_deutsch = f'https://www.duden.de/rechtschreibung/{text}'
    r_dict_deutsch = requests.get(url_dict_deutsch)
    return BS(r_dict_deutsch.text, 'html.parser')


def replace_multiple_newlines_with_one(string: str) -> str:
    return re.sub(r'\n+', '\n', string)


def some_words() -> list[str]:
    with open('wortliste.txt', 'r', encoding='utf8') as f:
        deutsch_list_of_words = f.read()
        dlist = deutsch_list_of_words.split('\n')
    return dlist


wörterbuch = some_words()


def mu_funk(message: str, *text):
    error_char = 'ⓘ〈〉'
    for_db = []
    for info in text:
        for i in info:
            if not isinstance(i, str):
                for_db.append(''.join(filter(lambda x: x not in error_char,
                                             replace_multiple_newlines_with_one(i.getText()))))
            else:
                for_db.append(''.join(filter(lambda x: x not in error_char,
                                             replace_multiple_newlines_with_one(info.getText()))))
                break
    inserted = (message, f'\n'.join(for_db), message)
    # bot.send_message(message.chat.id, f"`{text.getText()}`", parse_mode='Markdown')
    with sqlite3.connect('setting/db.sqlite3') as con:
        cur = con.cursor()
        cur.execute(f'''INSERT INTO blog_blog (title, content, slug) VALUES (?, ?, ?)''', inserted)


def check_db(message):
    request_for_db = str(message)
    with sqlite3.connect('setting/db.sqlite3') as con:
        cur = con.cursor()
        search_result = cur.execute(f"""SELECT * FROM blog_blog WHERE title=?""", (request_for_db, )).fetchall()
        if search_result:
            return True
        else:
            return False


def my_count_and_all_indeces(someth, fi) -> int and list:
    counter = -1
    positions = []
    for i in someth:
        if i == fi:
            counter += 1
            positions.append(counter)
    counter += 1
    return counter, positions
