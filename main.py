import telebot

from utils import ConversionCurrency, ConversionException
from config import keys, TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Hello to currency exchange bot! To see this message type /start or '
                                      '/help.'
                                      'Usage: from_currency to_currency value. '
                                      'You can check list of currencies using /list')


@bot.message_handler(commands=['list'])
def handle_list(message):
    list_keys = keys.keys()
    list_keys = ', '.join(map(str, list_keys))
    bot.send_message(message.chat.id, f'Supported currencies: {list_keys}. For example, if you need to '
                                      'convert 13.28 dollars to rubles you should type: \n'
                                      'dollar ruble 13.28 \n')


@bot.message_handler()
def function_name(message):
    msg = message.text.lower()
    try:
        values = msg.split()
        if len(values) != 3:
            raise ConversionException('You should fill 3 items.')
        else:
            base, target, amount = values
            amount = amount.replace(',', '.')
        new_amount = ConversionCurrency.convert(base, target, amount)
    except ConversionException as e:
        bot.reply_to(message, str(e))
    except Exception as e:
        bot.reply_to(message, str(e))
    else:
        bot.reply_to(message, f"{amount} {base} in {target} = {new_amount:.4f}")


bot.polling(none_stop=True)
