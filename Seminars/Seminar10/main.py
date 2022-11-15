import telebot
 
bot = telebot.TeleBot('5790131962:AAH1zRMDq8Yxp8YFTP202YxZhVjTZJ2Xnsg')
 
 
# dct = {}
  
# @bot.message_handler()
# def answer(msg: telebot.types.Message):
#     if msg.from_user.id not in dct:
#         dct[msg.from_user.id] = [1]
 
#     if dct[msg.from_user.id][0] == 1:
#         bot.send_message(msg.from_user.id, 'Введите первое число.')
#         bot.send_message(msg.from_user.id, f'{dct}')
#         dct[msg.from_user.id][0] = 2
 
#     elif dct[msg.from_user.id][0] == 2:
#         dct[msg.from_user.id].append(msg.text)
#         bot.send_message(msg.from_user.id, 'Введите второе число.')
#         bot.send_message(msg.from_user.id, f'{dct}')
#         dct[msg.from_user.id][0] = 3
 
#     elif dct[msg.from_user.id][0] == 3:
#         bot.send_message(msg.from_user.id, f'Ваш результат '
#                                            f'{dct[msg.from_user.id][-1]} + '
#                                            f'{msg.text}')
#         bot.send_message(msg.from_user.id, f'{dct}')
#         dct[msg.from_user.id] = [1]
 
#  или

@bot.message_handler()
def start(msg: telebot.types.Message):
    bot.send_message(msg.from_user.id, 'Вас приветствует самый лучший калькулятор')

@bot.message_handler()    
def answer(msg: telebot.types.Message):
    bot.send_message(msg.from_user,id,'Введите первое число')
    bot.registrer_next_step_handler(msg, second, last=int(msg.text))

def second(msg: telebot.types.Message, last):
    bot.send_message(msg.from_user.id, f'Текущее значение{last}')
    bot.send_message(msg.from_user.id, 'Введите еще одно число')
    bot.registrer_next_step_handler(msg, second, last=last + int(msg.text))
 
bot.polling()

