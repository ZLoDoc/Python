
from telebot import TeleBot
import telebot.types

bot = TeleBot('5790131962:AAH1zRMDq8Yxp8YFTP202YxZhVjTZJ2Xnsg')

wait = False

# work_base = open("pb.txt", "a", encoding="utf-8") 
# work_base.close()




def menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("View")
    btn2 = telebot.types.KeyboardButton("Find")
    btn3 = telebot.types.KeyboardButton("Export")
    markup.add(btn1, btn2, btn3)
    return markup

def exp_menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("csv")
    btn2 = telebot.types.KeyboardButton("txt")
    back = telebot.types.KeyboardButton("Back")
    markup.add(btn1, btn2, back)
    return markup

def find_contact(message: telebot.types.Message): 
    find_name = message.text    
    find_name = find_name.capitalize()
    work_base = open("pb.txt", "r", encoding="utf-8") 
    base = work_base.readlines() 
    work_base.close()      
    
    result = []
    for line in base: 
        if find_name in line: 
            result.append(line)
            
    if bool(result) is True:
        bot.send_message(chat_id=message.from_user.id, text=f"Finding result - {find_name}: ") 
        for contact in result:
            line = contact[:-1].split(";")
            bot.send_message(chat_id=message.from_user.id, text=f"{line[0]} {line[1]}  {line[2]}  {line[3]}")   
    else:
        bot.send_message(chat_id=message.from_user.id, text=f"{find_name} - No finding ")    
    bot.send_message(chat_id=message.from_user.id, text="Make your choice", reply_markup=menu())


def view_base(message: telebot.types.Message):
    work_base = open("pb.txt", "r+", encoding="utf-8") 
    base = work_base.readlines()   
    if work_base.tell() == 0:        
        bot.send_message(chat_id=message.from_user.id, text=f"The notebook is empty")                        
    else:           
        for contact in base:
            line = contact[:-1].split(";")
            bot.send_message(chat_id=message.from_user.id, text=f"{line[0]} {line[1]}  {line[2]}  {line[3]}")
    work_base.close() 
    bot.send_message(chat_id=message.from_user.id, text="Make your choice", reply_markup=menu())

def export_data(message: telebot.types.Message):
    work_base = open("pb.txt", "r+", encoding="utf-8")
    person_list = work_base.readlines()
    if work_base.tell() == 0:        
        bot.send_message(chat_id=message.from_user.id, text="The notebook is empty")
    elif message.text == "csv":
        exp_file = "pb_exp.csv"
        exp_csv(exp_file, person_list)
    elif message.text == "txt":
        exp_file = "pb_exp.txt"
        exp_txt(exp_file, person_list)
    work_base.close()              
    bot.send_document(chat_id=message.from_user.id, document=open(exp_file, 'rb'))
    bot.send_message(chat_id=message.from_user.id, text="Make your choice", reply_markup=menu())

def exp_csv(file, person_list):
    exp_file = open(file, "w", encoding="cp1251") 
    for person in person_list:
        exp_file.write(person) 
    exp_file.close()        

def exp_txt(file, person_list):
    exp_file = open(file, "w", encoding="utf-8") 
    for contact in person_list:
        result = contact[:-1].split(";")        
        for item in result:
                exp_file.write(item + "\n")   
        exp_file.write("\n")           
    exp_file.close()   


@bot.message_handler(commands=['start'])
def start(message):        
    bot.send_message(chat_id=message.from_user.id, text="Make your choice", reply_markup=menu())


@bot.message_handler(content_types=['text'])
def func(message):
    global wait    
    
    if (message.text == "View"):
        bot.send_message(chat_id=message.from_user.id, text="View person_list")
        view_base(message)   
    elif (message.text == "Find"):
        wait = True
        bot.send_message(chat_id=message.from_user.id, text="Enter the search text")
    elif wait:
        wait = False                
        find_contact(message)
    elif (message.text == "Export"):               
        bot.send_message(chat_id=message.from_user.id, text="Select format", reply_markup=exp_menu())
    elif (message.text == "txt"):
        export_data(message)
    elif (message.text == "csv"):
        export_data(message)
    elif (message.text == "Back"):        
        bot.send_message(chat_id=message.from_user.id, text="Make your choice", reply_markup=exp_menu())
    else:
        bot.send_message(chat_id=message.from_user.id, text="It's wrong choise. Replay.")        
        bot.send_message(chat_id=message.from_user.id, text="Make your choice", reply_markup=menu())
    

bot.polling()
