import config
import telebot

bot = telebot.TeleBot(config.API_KEY)


def check_message(message):
    return True


@bot.message_handler(func=check_message)
def reply(message):
    user = message.from_user
    name = user.first_name

    bot.reply_to(message, "Hello " + name + "! Working in progress...")


bot.polling()
