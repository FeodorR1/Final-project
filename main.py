import telebot

from additional import mu_funk, wörterbuch, check_db, parcing
from config import token


if __name__ == '__main__':

    bot = telebot.TeleBot(token)


    @bot.message_handler(commands=['start'])
    def hello_0(message):
        bot.send_message(message.chat.id,
                         f"Halo, {str(message.from_user.username)}, ich bin nicht sehr nützlicher bot(")


    @bot.message_handler(commands=['link'])
    def send_link(message):
        bot.send_message(message.chat.id, f"Ein bisschen deutsche Wörter sind hier: 127.0.0.1:2000")


    @bot.message_handler(content_types=['text'])
    def deutsch_request(message):
        text = message.text
        if text in wörterbuch:
            if check_db(text) is False:
                soup_dict_deutsch = parcing(text)
                answer_1 = soup_dict_deutsch.find_all('div', id='bedeutung')
                answer_2 = soup_dict_deutsch.find_all('dd', class_='tuple__val')
                if answer_1:
                    pass
                else:
                    answer_1 = soup_dict_deutsch.find_all('div', id='bedeutungen')
                for text_1, text_2 in zip(answer_1, answer_2):
                    mu_funk(text, text_1, text_2)
                bot.send_message(message.chat.id, f'http://127.0.0.1:2000/wort/{text}')
            elif check_db(text):
                bot.send_message(message.chat.id, f'http://127.0.0.1:2000/wort/{text}')
            else:
                bot.send_message(message.chat.id, 'Schick mir bitte das deutsche Wort')
        else:
            bot.send_message(message.chat.id, 'Schick mir bitte das deutsche Wort')


    bot.polling(none_stop=True)
