import imp_exp as ie
import menu
import view
import add_mod as ad
import find_mod as fm
# import export as exp

menu_continue = 1
work_data = ie.open_base()
while menu_continue:
    choise = menu.main_menu()
    if choise == "1": view.view_baase(work_data)
    if choise == "2": work_data = ad.add_data(ie.open_base())
    if choise == "3": ie.export(work_data)
    if choise == "4": fm.find_value(work_data)
    if choise == "5": 
        ie.exit(work_data)
        break 