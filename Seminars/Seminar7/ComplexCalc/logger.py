from datetime import datetime as dt
def logger (file_name = "log.csv", text = " Что - то пыцнулось", value = None):
    if value is None:
        value = ""
    time = dt.now().strftime("%H:%M")
    with open(file_name,"a") as file:
        file.write(f"{time};{text};{value}")
