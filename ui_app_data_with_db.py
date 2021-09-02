from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import face_detect_2
#from create_app_data_db import *
from update_app_data_db import *
import random
import string


'''      
##################################################################################
##################################################################################
'''


nickname = ''

def idnButton(): # идентификация пользователя
    if face_detect_2.init_face() == True:
        start_btn.hide()
        btn_show()
        global nickname
        nickname = generate_random_string(nickname)

def generate_random_string(nickname):
    if  len(nickname) <= 49:
        letters = string.ascii_lowercase
        create_nickname = ''.join(random.choice(letters) for i in range(50))
        return create_nickname
    else:
        return nickname

def add_new_info():
    btn_hide()
    back_btn.show()
    accept_btn_all.show()
    edit_login.show()
    edit_password.show()
    edit_site_url.show()


def fill_url_lgn_pass():

    a = edit_site_url.text()
    b = edit_password.text()
    c = edit_login.text()
    global nikname
    data = (a,b,c,nickname)
    insert_new_data_to_bd(data)
    show_db()

def update_login():
    a = edit_site_url.text()
    global nickname


'''      
##################################################################################
##################################################################################
'''
# Созданиет окна приложения
app = QApplication([])
window = QWidget()
window.setWindowTitle('looking vault')
window.resize(750,500)
'''      
##################################################################################
##################################################################################
'''
# Создание кнопок
start_btn = QPushButton("Идентефикация")#запуск распознования
site_bt = QPushButton("Сайты")#получение логина и пароля к интересующему нас сайту
chande_site_pass = QPushButton("Сменить пароль")#смена пароля для нужного сайта
chande_site_nick = QPushButton("Сменить никнейнм")#смена логина длятнужного сайта
add_site_info = QPushButton("Добавить новую информацию")#новая связка логин + пароль + имя сайта
delete_site_info = QPushButton("Удаление аккаунта(ов)")#удаление связки логин + пароль
site_bt.hide()
chande_site_nick.hide() 
chande_site_pass.hide()
add_site_info.hide()
delete_site_info.hide()
back_btn = QPushButton('Назад') # Вернуться назад
back_btn.hide()
accept_btn_all = QPushButton('Сохранить изменения')
accept_btn_all.hide()
'''      
##################################################################################
##################################################################################
'''
# Создание надписей для вывода инфы
login = QLabel('Ваш логин')
site_url = QLabel('URL сайта')
password = QLabel('Ваш пароль')
'''      
##################################################################################
##################################################################################
'''
#Создание полей для ввода
edit_password = QLineEdit('Введите ваш пароль в это окно')
edit_login = QLineEdit('Введите ваш логин в это окно')
edit_site_url = QLineEdit('введите ссылку на сайт в это окно')

edit_login.hide()
edit_password.hide()
edit_site_url.hide()
'''      
##################################################################################
##################################################################################
'''
# Скрытие кнопок и показ кнопок
def btn_hide():
    site_bt.hide()
    chande_site_nick.hide()
    chande_site_pass.hide()
    add_site_info.hide()
    delete_site_info.hide()

def btn_show():
    chande_site_nick.show()
    chande_site_pass.show()
    add_site_info.show()
    delete_site_info.show()
'''      
##################################################################################
##################################################################################
'''
# Создание лэйаутов
v1 = QVBoxLayout()
h1 = QHBoxLayout()
'''      
##################################################################################
##################################################################################
'''
# Установка виджетов на лэйауты, связь лэйаутов друг с другом и с главным окном
v1.addWidget(start_btn)
v1.addWidget(site_bt)
v1.addWidget(chande_site_pass)
v1.addWidget(chande_site_nick)
v1.addWidget(add_site_info)
v1.addWidget(delete_site_info)
v1.addWidget(back_btn)
v1.addWidget(accept_btn_all)

h1.addWidget(edit_site_url)
h1.addWidget(edit_login )
h1.addWidget(edit_password)

v1.addLayout(h1)

window.setLayout(v1)
'''      
##################################################################################
##################################################################################
'''
# Подключение функций к кнопкам
start_btn.clicked.connect(lambda x : idnButton())
add_site_info.clicked.connect( lambda y : add_new_info())
accept_btn_all.clicked.connect(lambda z : fill_url_lgn_pass())
'''      
##################################################################################
##################################################################################
'''
window.show()
app.exec_()