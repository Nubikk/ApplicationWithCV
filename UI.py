from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import face_detect_2
import bd_function

'''      
##################################################################################
##################################################################################
'''
# Созданиет окна приложения
app = QApplication([])
window = QWidget()
window.setWindowTitle('looking vault')
window.resize(800,600)
idn_btn = QPushButton("Идентификация",window)
main_layout = QVBoxLayout()
main_layout.addWidget(idn_btn)
window.setLayout(main_layout)
'''      
##################################################################################
##################################################################################
'''
#Создание диалоговых окон
main_dialog = QDialog()
add_dialog_win = QDialog()
del_dialog = QDialog()
search_dialog = QDialog()
'''      
##################################################################################
##################################################################################
'''
# Работа с "Главным" диалоговым окном
add_btn = QPushButton("Добавить информацю",main_dialog)#добавление инфы
del_btn = QPushButton("Удалить информацию",main_dialog)#удаление инфы
search_btn = QPushButton("Найти информацию",main_dialog)#найти инфу
main_dialog_layout = QVBoxLayout()
main_dialog_layout.addWidget(search_btn)
main_dialog_layout.addWidget(add_btn)
main_dialog_layout.addWidget(del_btn)
main_dialog.setLayout(main_dialog_layout)
main_dialog.hide()
'''      
##################################################################################
##################################################################################
'''
# Работа с добавлением
lgn_line = QLineEdit("Логин",add_dialog_win) # поле для логина
pass_line = QLineEdit("Пароль",add_dialog_win)# поле для пароля
site_line = QLineEdit("Сайт",add_dialog_win)# поле для сайта
add_info_btn = QPushButton("Добавить",add_dialog_win)#кнопка сохранения инфы в БД
add_back_btn = QPushButton("Назад",add_dialog_win) # вернутся назад из добавления


add_layout = QVBoxLayout()
add_layout.addWidget(lgn_line)
add_layout.addWidget(pass_line)
add_layout.addWidget(site_line)
add_layout.addWidget(add_info_btn)
add_layout.addWidget(add_back_btn)


add_dialog_win.setLayout(add_layout)
add_dialog_win.hide()
'''      
##################################################################################
##################################################################################
'''
# Работа с удалением
del_line = QLineEdit("Поиск осуществляется по сайту: ",del_dialog)# поле для удаления
del_info_btn = QPushButton("Удалить",del_dialog) #кнопка удаления информации
del_back_btn = QPushButton("Назад", del_dialog)#вернутся назад из удаления инфы
del_layout = QVBoxLayout()
del_layout.addWidget(del_line)
del_layout.addWidget(del_info_btn)
del_layout.addWidget(del_back_btn)
del_dialog.setLayout(del_layout)
del_dialog.hide()
del_dialog.resize(300,200)
'''      
##################################################################################
##################################################################################
'''
#Работа с поиском
search_line = QLineEdit(search_dialog) # поле для поиска
lgn_label = QLabel(search_dialog)
pass_label = QLabel(search_dialog)
search_info_btn = QPushButton("Найти",search_dialog)#запуск поиска инфы
search_back_btn = QPushButton("Назад",search_dialog)#вернутся назад из поиска

search_layout = QVBoxLayout()
search_layout.addWidget(search_line)
search_layout.addWidget(lgn_label)
search_layout.addWidget(pass_label)
search_layout.addWidget(search_info_btn)
search_layout.addWidget(search_back_btn)
search_dialog.setLayout(search_layout)
search_dialog.hide()
'''      
##################################################################################
##################################################################################
'''
# Функция для перехода от идентификации к поиску, добавлению, удалению
def window_funct():
    main_dialog.show()
    window.hide()
idn_btn.clicked.connect(window_funct)
'''      
##################################################################################
##################################################################################
'''
# Работа с функциями для окна добавления
def add_btn_funct():
    main_dialog.hide()
    add_dialog_win.show()

#нажатие на кнопку назад
def add_return_btn():
    add_dialog_win.hide()
    main_dialog.show()

add_btn.clicked.connect(add_btn_funct)
add_back_btn.clicked.connect(add_return_btn)
add_info_btn.clicked.connect(lambda: bd_function.add(lgn_line.text(), pass_line.text(), site_line.text()))

'''      
##################################################################################
##################################################################################
'''
#Работа с функциями окна удаления

def del_return_btn():
    del_dialog.hide()
    main_dialog.show()

def del_btn_funct():
    main_dialog.hide()
    del_dialog.show()

del_btn.clicked.connect(del_btn_funct)
del_back_btn.clicked.connect(del_return_btn)
del_info_btn.clicked.connect(lambda: bd_function.drop(del_line.text()))
'''      
##################################################################################
##################################################################################
'''
#Работа с функциями окна поиска
def search_return_btn():
    search_dialog.hide()
    main_dialog.show()

def search_btn_funct():
    main_dialog.hide()
    search_dialog.show()

def show_search_info(lnk):
   l,p = bd_function.show(lnk)
   lgn_label.setText(l)
   pass_label.setText(p)



search_btn.clicked.connect(search_btn_funct)
search_back_btn.clicked.connect(search_return_btn)
search_info_btn.clicked.connect(lambda: show_search_info(search_line.text()))
'''      
##################################################################################
##################################################################################
'''
window.show()
app.exec()
