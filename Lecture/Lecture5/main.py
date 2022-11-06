
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5790131962:AAH1zRMDq8Yxp8YFTP202YxZhVjTZJ2Xnsg").build()
print('servak is started')
app.add_handler(CommandHandler("hello", hello))

app.run_polling()

 


# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,3,2,7]
# plt.plot(list)

# plt.show()



# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))



# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     # Do some work
#     bar.next()
# bar.finish()


# # 24:48
# from isOdd import isOdd

# print(isOdd('1')) #//=> true
# print(isOdd('5')) #//=> true

# print(isOdd(0)) #//=> false
# print(isOdd(4)) #//=> false