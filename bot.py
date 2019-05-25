from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s- %(message)s', 
    level = logging.INFO, 
    filename ='bot.log')

def greet_user(bot,update):
    text = "Вызван/start"
    print(text)
    # принты перед коммитами лучше убирать, ну и давай сюда перечень возможностей бота добавим
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    # а что произойдет, если имя не указано у человека?
    logging.info(
        "User: %s, Chat id: %s, Message: %s ", 
        update.message.chat.username,
        update.message.chat.id, 
        update.message.text
    )
    # выге более удобный и читабельный способ форматирования
    update.message.reply_text(user_text)



def main():
    mybot = Updater("723030173:AAEH6hRIuxxne8JFHK1rYpOq6Q0PVwlfPfI")
     # токен для бота - как ключ от квартиры, лучше в публичных местах типа гитхаба не оставлять, а то кто угодно может его взять
     # обычно его выносят в отдельный файл, который добвляют в .gitignore и не "светят" наружу
   
    logging.info("Бот запускается")
    # логирования - супер!!!!

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

main()


    
