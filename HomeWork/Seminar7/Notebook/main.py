# from HomeWork.Seminar7.Notebook.menu import main_menu_export
import imp_exp as ie
import menu
import view
import add_mod as ad
import find_mod as fm
# import export as exp

menu_continue = True
menu_exp_continue =True
work_data = ie.open_base()
while menu_continue:
    choise = menu.main_menu()
    if choise == "1": view.view_baase(work_data)
    if choise == "2": work_data = ad.add_data(ie.open_base())
    if choise == "3": 
        # ie.export(work_data)
        while menu_exp_continue:
           choise1 = menu.main_menu_export()           
           choise = ""
           if choise1 == "1":
            ie.export_csv(work_data)
            break
           if choise1 == "2": 
            ie.export_txt(work_data)            
            break
           if choise1 == "3":break

    if choise == "4": ie.import_data(work_data)
    if choise == "5": fm.find_value(work_data)
    if choise == "6": 
        ie.exit(work_data)
        break 