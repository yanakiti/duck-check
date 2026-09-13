import telebot, requests
from model import get_class
# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("8880420892:AAG9n2UPMVnk1-vqoNqCZ5opGJz04pxQ-mA")


def gen_duck_image_url():
    url = "https://random-d.uk/api/random"
    result = requests.get(url).json()
    return result

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Отправь мне изображение уток, я проанализирую его. Используй команду /duck ")

@bot.message_handler(commands=['duck'])
def duck(message):
    #возвращает фото утки
    image_url = gen_duck_image_url()
    bot.send_message(message.chat.id, image_url)


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    if not message.photo:
        return bot.send_message(message.chat.id, "Нет изображенияю. Отправь в чат картинку с утками." )

    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    result = get_class()
    bot.send_message(message.chat.id, result)

# Запускаем бота
bot.polling()