# TOKEN 5265923075:AAEriIZresJtuYQ2LN0od4Uv9ZsVu94yECQ

# -------------Используемые библиотеки----------------

import telebot
from telebot import types
import sqlite3

# -------------Подключение токена бота----------------

bot = telebot.TeleBot("5265923075:AAEriIZresJtuYQ2LN0od4Uv9ZsVu94yECQ")

# -------------Кнопки, используемые в проекте----------------

keyboardmotherboardbackoradd = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboardmotherboardbackoradd.row('Добавить материнскую плату в сборку')
keyboardmotherboardbackoradd.row('Вернуться к выбору материнской платы')
keyboardcpubackoradd = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboardcpubackoradd.row('Добавить процессор в сборку')
keyboardcpubackoradd.row('Вернуться к выбору процессоров')
keyboardcorpbackoradd = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboardcorpbackoradd.row('Добавить корпус в сборку')
keyboardcorpbackoradd.row('Вернуться к выбору корпусов')
keyboardvideobackoradd = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboardvideobackoradd.row('Добавить видеокарту в сборку')
keyboardvideobackoradd.row('Вернуться к выбору видеокарт')
keyboardcoolbackoradd = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboardcoolbackoradd.row('Добавить кулер в сборку')
keyboardcoolbackoradd.row('Вернуться к выбору кулера')
keyboardrambackoradd = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboardrambackoradd.row('Добавить ОЗУ в сборку')
keyboardrambackoradd.row('Вернуться к выбору ОЗУ')
keyboardhddbackoradd = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboardhddbackoradd.row('Добавить данный ЖЕСТКИЙ ДИСК в сборку')
keyboardhddbackoradd.row('Вернуться к выбору ЖЕСТКОГО ДИСКА')
keyboardpubackoradd = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboardpubackoradd.row('Добавить данный Блок питания в сборку')
keyboardpubackoradd.row('Вернуться к выбору Блока питания')

# -------------Общий бюджет----------------
money = 0

# -------------Переменные, отвечающие за раздел бюджета----------------
motherboard = 0
CPU_value = 0
corps = 0
video_card = 0
CPU_cooling = 0
RAM_value = 0
data_storage = 0
power_unit = 0

# -------------Переменные, помогающие в сборке----------------
socketmotherboard = ""
socketproc = ""
motherboardtrue_1 = 0
motherboardtrue = 0
cputrue_1 = 0
cputrue = 0
motherboardform = ""
corptrue = 0
videocardstrue = 0
coolertrue = 0
ramtrue = 0
hddtrue = 0
putrue = 0

# -------------Итоговые переменные для вывода всей сборки----------------
motherboardname = ""
procname = ""
corp_name = ""
video_card_name = ""
cpu_cooling_name = ""
ram_value_name = ""
data_storage_name = ""
power_unit_name = ""
additional_details_name = ""
result_cost = 0

# -------------HELP VALUES----------------

xmw = 5 # Проверка начала сборки
# Проверка на то, что на введенную сумму можно подобрать компьютер (3 переменные ниже)
checkValue = 99
intermediateValue = 0
resultValue = 0


# -------------БАЗА ДАННЫХ И РАБОТА С НЕЙ----------------

# -------------Проверка на подходяющую стоимость----------------

def _checkall(records):
    global checkValue
    global resultValue
    global intermediateValue
    global motherboard
    global CPU_value
    global corps
    global video_card
    global CPU_cooling
    global RAM_value
    global data_storage
    global power_unit
    try:
        #Отслеживание корректности работы кода (для разработчика)
        print(motherboard)
        print(CPU_value)
        print(corps)
        print(video_card)
        print(CPU_cooling)
        print(RAM_value)
        print(data_storage)
        print(power_unit)

        resultValue = 0
        # Проверка материнской платы
        checkValue = 99
        intermediateValue = 0
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()
        # Подключение из базы данных элемента
        sqlite_select_query = """SELECT * from motherboards"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        # Проверка всех материнских плат на введенную сумму пользователя (ранее уже расчитан процент отведённый элемент)
        for row in records:
            balancemotherboard = int(row[24])
            print("Баланс материнской платы: ", balancemotherboard)
            if balancemotherboard < motherboard:
                checkValue = 0
            if (checkValue == 0):
                intermediateValue += 1
        if (intermediateValue > 0):
            resultValue += 1
        cursor.close()
        print("resultValue after motherboard: ", resultValue)

        # Проверка процессора
        checkValue = 99
        intermediateValue = 0
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()
        # Подключение из базы данных элемента
        sqlite_select_query = """SELECT * from cpu"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        # Проверка всех элементов(подключенных из БД) на введенную сумму пользователя (ранее уже расчитан процент отведённый элемент)
        for row in records:
            balancecpu = int(row[12])
            print("Баланс процессора: ", balancecpu)
            if (balancecpu < CPU_value):
                checkValue = 0
            if (checkValue == 0):
                intermediateValue += 1
        if (intermediateValue > 0):
            resultValue += 1
        cursor.close()
        print("resultValue after cpu: ", resultValue)

        # Проверка корпуса
        checkValue = 99
        intermediateValue = 0
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()
        # Подключение из базы данных элемента
        sqlite_select_query = """SELECT * from corp"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        # Проверка всех элементов(подключенных из БД) на введенную сумму пользователя (ранее уже расчитан процент отведённый элемент)
        for row in records:
            balancecorp = int(row[12])
            print("Баланс корпуса: ", balancecorp)
            if (balancecorp < corps):
                checkValue = 0
            if (checkValue == 0):
                intermediateValue += 1
        if (intermediateValue > 0):
            resultValue += 1
        cursor.close()
        print("resultValue after corp: ", resultValue)

        # Проверка видеокарт
        checkValue = 99
        intermediateValue = 0
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()
        # Подключение из базы данных элемента
        sqlite_select_query = """SELECT * from videocards"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        # Проверка всех элементов(подключенных из БД) на введенную сумму пользователя (ранее уже расчитан процент отведённый элемент)
        for row in records:
            balancevideo = int(row[8])
            print("Баланс корпуса: ", balancevideo)
            if (balancevideo < video_card):
                checkValue = 0
            if (checkValue == 0):
                intermediateValue += 1
        if (intermediateValue > 0):
            resultValue += 1
        cursor.close()
        print("resultValue after videocards: ", resultValue)

        # Проверка кулеров
        checkValue = 99
        intermediateValue = 0
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()
        # Подключение из базы данных элемента
        sqlite_select_query = """SELECT * from coolers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        # Проверка всех элементов(подключенных из БД) на введенную сумму пользователя (ранее уже расчитан процент отведённый элемент)
        for row in records:
            balancecoolers = int(row[9])
            if (balancecoolers < CPU_cooling):
                checkValue = 0
            if (checkValue == 0):
                intermediateValue += 1
        if (intermediateValue > 0):
            resultValue += 1
        cursor.close()

        # Проверка ОЗУ
        checkValue = 99
        intermediateValue = 0
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()
        # Подключение из базы данных элемента
        sqlite_select_query = """SELECT * from ram"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        # Проверка всех элементов(подключенных из БД) на введенную сумму пользователя (ранее уже расчитан процент отведённый элемент)
        for row in records:
            balanceram = int(row[10])
            if balanceram < RAM_value:
                checkValue = 0
            if (checkValue == 0):
                intermediateValue += 1
        if (intermediateValue > 0):
            resultValue += 1
        cursor.close()

        # Проверка жесткого диска
        checkValue = 99
        intermediateValue = 0
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()
        # Подключение из базы данных элемента
        sqlite_select_query = """SELECT * from hdd"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        # Проверка всех элементов(подключенных из БД) на введенную сумму пользователя (ранее уже расчитан процент отведённый элемент)
        for row in records:
            balancehdd = int(row[8])
            if balancehdd < data_storage:
                checkValue = 0
            if (checkValue == 0):
                intermediateValue += 1
        if (intermediateValue > 0):
            resultValue += 1

        cursor.close()

        # Проверка блока питания
        checkValue = 99
        intermediateValue = 0
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()
        # Подключение из базы данных элемента
        sqlite_select_query = """SELECT * from pu"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        # Проверка всех элементов(подключенных из БД) на введенную сумму пользователя (ранее уже расчитан процент отведённый элемент)
        for row in records:
            balancepu = int(row[8])
            if balancepu < power_unit:
                checkValue = 0
            if (checkValue == 0):
                intermediateValue += 1
        if (intermediateValue > 0):
            resultValue += 1
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

            return resultValue


# -------------Проверка //motherboard (Если пользователь выбрал начинать с материнской платы)----------------

def checkmotherboard(records):
    global xmw
    xmw = 0
    try:
        keyboardmotherboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from motherboards"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            balancemotherboard = int(row[24])

            massmotherboard = row[0]

            if balancemotherboard < motherboard:
                keyboardmotherboard.row(row[0])
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

            return keyboardmotherboard


# -------------Проверка //cpu (Если пользователь выбрал начинать с материнской платы)----------------


def checkcpu(records):
    try:
        keyboardcpu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from cpu"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            balancecpu = int(row[12])
            if (balancecpu < CPU_value):
                keyboardcpu.row(row[0])
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

            return keyboardcpu


# ----------------------------------------------------------------------------------------------------
# -------------Проверка //motherboard (Если пользователь выбрал начинать с процессора)----------------

def checkmotherboard1(records):
    try:
        keyboardmotherboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from motherboards"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            balancemotherboard = int(row[24])
            motherboardsocket = row[8]
            if (balancemotherboard < motherboard) and (motherboardsocket == socketproc):
                keyboardmotherboard.row(row[0])
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

            return keyboardmotherboard


# -------------Проверка //cpu (Если пользователь выбрал начинать с процессора)----------------


def checkcpu1(records):
    global xmw
    xmw = 1
    try:
        keyboardcpu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from cpu"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            balancecpu = int(row[12])

            if (balancecpu < CPU_value):
                keyboardcpu.row(row[0])
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

            return keyboardcpu


# -------------Проверка //corp (На соотвествие бюджету и важных для коррректной сборки деталей)----------------


def checkcorp(records):
    try:
        keyboardcorp = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from corp"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            balancecorp = int(row[12])

            formfaktorcorp1 = row[9]
            formfaktorcorp2 = row[10]
            formfaktorcorp3 = row[11]

            if (balancecorp < corps) and (
                    formfaktorcorp1 == motherboardform or formfaktorcorp2 == motherboardform or formfaktorcorp3 == motherboardform):
                keyboardcorp.row(row[0])
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

            return keyboardcorp


# -------------Проверка //videocards(На соотвествие бюджету и важных для коррректной сборки деталей)----------------


def checkvideo(records):
    try:
        keyboardvideo = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from videocards"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            balancevideo = int(row[8])

            if balancevideo < video_card:
                keyboardvideo.row(row[0])
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

            return keyboardvideo


# -------------Проверка //coolers(На соотвествие бюджету и важных для коррректной сборки деталей)----------------


def checkcool(records):
    try:
        keyboardcool = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from coolers"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            balancecoolers = int(row[9])
            heightcoolers = row[8]
            if (balancecoolers < CPU_cooling) and (heightcoolers + 3 < width_corp):
                keyboardcool.row(row[0])
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

            return keyboardcool


# -------------Проверка //ram(На соотвествие бюджету и важных для коррректной сборки деталей)----------------


def checkram(records):
    try:
        keyboardram = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from ram"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            balanceram = int(row[10])

            if balanceram < RAM_value:
                keyboardram.row(row[0])
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

            return keyboardram


# -------------Проверка //hdd(На соотвествие бюджету и важных для коррректной сборки деталей)----------------


def checkhdd(records):
    try:
        keyboardhdd = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from hdd"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            balancehdd = int(row[8])

            if balancehdd < data_storage:
                keyboardhdd.row(row[0])
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

            return keyboardhdd


# -------------Проверка //Блока питания(На соотвествие бюджету и важных для коррректной сборки деталей)----------------


def checkpu(records):
    try:
        keyboardpu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        sqlite_connection = sqlite3.connect('items.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from pu"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            balancepu = int(row[8])
            if balancepu < power_unit:
                keyboardpu.row(row[0])

        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            return keyboardpu


# ----------------------------------------------------------------------------------------------------

# -------------MOTHERBOARD DATA----------------

# функция создания конструктора
def motherboardinput(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16, k17, k18, k19, k20, k21,
                     k22, k23, k24, k25):
    cursor.execute(
        "INSERT OR IGNORE INTO `motherboards` (`name`,`guarantee`,`creator`,`model`,`release_year`,`form_factor`,`height`,`width`,`socket`,`chipset`,`memory_slots`,`form_factor_RAM`,`type_RAM`,`number_of_memory_channels`,`max_RAM`,`PCI_version`,`kol_vo_PCI`,`kol_vo_USB`,`video_output`,`sound_scheme`,`sound`,`sound_chipset`,`speed_network_adapter`,`chipset_network_adapter`,`cost`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16, k17, k18, k19, k20, k21,
         k22, k23, k24, k25))

# добавление элементов в БД
def create_motherboard_data():
    motherboardinput('GIGABYTE H610M S2H', 36, 'Китай', 'GIGABYTE H610M S2H', 2021, 'Micro-ATX', 230, 215, 'LGA 1700',
                     'Intel H610', 2, 'DIMM', 'DDR4', 2, 64, "4.0", 1, 4, "VGA (D-Sub), DVI-D, DisplayPort, HDMI",
                     "7.1", "Отсутствует",
                     "Отсутствует", 1, "Отсутствует", 8999)
    motherboardinput('MSI MAG B560M BAZOOKA', 36, 'Китай', 'MSI MAG B560M BAZOOKA', 2021, 'Micro-ATX', 244, 244,
                     'LGA 1200',
                     'Intel B560', 4, 'DIMM', 'DDR4', 2, 128, "4.0", 1, 6, "DisplayPort, HDMI",
                     "7.1", "Realtek HD Audio",
                     "Realtek ALC897", 2.5, "Realtek RTL8125B", 12999)
    motherboardinput('MSI PRO B660M-A DDR4', 36, 'Китай', 'MSI PRO B660M-A DDR4', 2022, 'Micro-ATX', 244, 244,
                     'LGA 1700',
                     'Intel B660', 4, 'DIMM', 'DDR4', 2, 128, "4.0", 2, 6, "DisplayPort, HDMI",
                     "7.1", "Realtek HD Audio",
                     "Realtek ALC897", 2.5, "Realtek RTL8125BG", 13299)


# -------------CPU DATA----------------

# функция создания конструктора
def cpuinput(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13):
    cursor.execute(
        "INSERT OR IGNORE INTO `cpu` (`name`,`guarantee`,`creator`,`model`,`socket`,`year_relase`,`potoks`,`kol_vo yader`,`rate_proc`,`type_RAM`,`max_RAM`,`temper`,`cost`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13))

# добавление элементов в БД
def create_cpu_data():
    cpuinput("Intel Core i3-12100F OEM", 36, "Китай", "Intel Core i3-12100F", "LGA 1700", 2022, 8, 4, 4.3, "DDR4,DDR5",
             128, 89, 16999)
    cpuinput("Intel Core i5-12400F OEM", 36, "Китай", "Intel Core i5-12400F", "LGA 1700", 2022, 12, 6, 4.4,
             "DDR4,DDR5",
             128, 117, 26999)
    cpuinput("Intel Core i5-11400F OEM", 12, "Вьетнам", "Intel Core i5-11400F", "LGA 1200", 2021, 12, 6, 4.4,
             "DDR4",
             128, 65, 19499)


# -------------CORP DATA----------------

# функция создания конструктора
def corpinput(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13):
    cursor.execute(
        "INSERT OR IGNORE INTO `corp` (`name`,`guarantee`,`creator`,`model`,`height`,`width`,`length`,`сolour`,`material`,`formfactor1`,`formfactor2`,`formfactor3`,`cost`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13))

# добавление элементов в БД
def create_corp_data():
    corpinput("AeroCool SI-5200 Window", 24, "Тайвань (Китай)", "AeroCool SI-5200 Window", 440.5, 196, 399, "Черный",
              "Сталь, пластик", "Micro-ATX", "Mini-ITX", "Standard-ATX", 3099)
    corpinput("DEEPCOOL MATREXX 50 MESH 4FS", 12, "Китай", "DEEPCOOL MATREXX 50 MESH 4FS", 442, 210, 479, "Черный",
              "Сталь, пластик, стекло", "Micro-ATX", "Mini-ITX", "Standard-ATX", 5099)
    corpinput("Cougar MX330-F", 12, "Китай", "Cougar MX330-F", 427, 195, 473, "Черный",
              "Сталь, пластик", "Micro-ATX", "Mini-ITX", "Standard-ATX", 4499)


# -------------VIDEOCARDS DATA----------------

# функция создания конструктора
def videocardsinput(k1, k2, k3, k4, k5, k6, k7, k8, k9):
    cursor.execute(
        "INSERT OR IGNORE INTO `videocards` (`name`,`guarantee`,`creator`,`model`,`graphproc`,`memory`,`type_memory`,`system_cold`,`cost`) VALUES (?,?,?,?,?,?,?,?,?)",
        (k1, k2, k3, k4, k5, k6, k7, k8, k9))

# добавление элементов в БД
def create_videocards_data():
    videocardsinput("ASRock AMD Radeon RX 6500 XT Phantom Gaming D OC", 36, "Китай",
                    "ASRock AMD Radeon RX 6500 XT Phantom Gaming D OC", "Radeon RX 6500 XT", 4, "GDDR6",
                    "Активное воздушное", 30999)
    videocardsinput("Palit GeForce RTX 3050 Dual OC", 36, "Китай",
                    "Palit GeForce RTX 3050 Dual OC", "GeForce RTX 3050", 8, "GDDR6",
                    "Активное воздушное", 58499)
    videocardsinput("Palit GeForce RTX 3060 Ti DUAL", 36, "Китай",
                    "Palit GeForce RTX 3060 Ti DUAL", "GeForce RTX 3060 TI", 8, "GDDR6",
                    "Активное воздушное", 105999)


# -------------СPU COOLING DATA----------------
# функция создания конструктора
def coolerinput(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10):
    cursor.execute(
        "INSERT OR IGNORE INTO `coolers` (`name`,`guarantee`,`model`,`TDP`,`heat_pipes`,`colour`,`max_speed`,`noise`,`height`,`cost`) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (k1, k2, k3, k4, k5, k6, k7, k8, k9, k10))

# добавление элементов в БД
def create_cooler_data():
    coolerinput("Cooler Master Hyper 212 Black Edition", 24, "Hyper 212 Black Edition", 180, 4, "черный", 2000, 26,
                158.5, 4699)
    coolerinput("DEEPCOOL GAMMAXX 400 V2", 12, "DEEPCOOL GAMMAXX 400 V2", 180, 4, "черный", 1600, 27.8, 155, 2199)
    coolerinput("AeroCool Verkho 2 Dual", 12, "AeroCool Verkho 2 Dual", 120, 2, "синий", 2300, 27, 135, 1250)


# -------------RAM VALUE DATA----------------
# функция создания конструктора
def raminput(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11):
    cursor.execute(
        "INSERT OR IGNORE INTO `ram` (`name`,`guarantee`,`creator`,`model`,`colour`,`type`,`volume_one`,`volume_all`,`frequency`,`timings`,`cost`) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11))

# добавление элементов в БД
def create_ram_data():
    raminput("Patriot Viper 4 Blackout", 120, "Тайвань (Китай)", "Patriot Viper 4 Blackout", "черный", "DDR4", 8, 16,
             3200, "16-20-20-40", 7699)
    raminput("Goodram Iridium", 120, "Корея,республика", "Goodram Iridium", "черный", "DDR4", 8, 16, 2666,
             "16-18-18-35", 6199)
    raminput("Kingston HyperX FURY Black", 120, "Тайвань (Китай)", "Kingston HyperX FURY Black", "черный", "DDR4", 8,
             16, 3200, "16-18-18-32", 8499)


# -------------DATA STORAGE DATA----------------
# функция создания конструктора
def data_storager_input(k1, k2, k3, k4, k5, k6, k7, k8, k9):
    cursor.execute(
        "INSERT OR IGNORE INTO `hdd` (`name`,`guarantee`,`creator`,`model`,`max_rot_speed`,`max_data_speed`,`noise`,`volume`,`cost`) VALUES (?,?,?,?,?,?,?,?,?)",
        (k1, k2, k3, k4, k5, k6, k7, k8, k9))

# добавление элементов в БД
def create_hdd_data():
    data_storager_input("WD Blue 1 TB", 24, "Таилнад", "WD Blue (WD10EZRZ)", 5400, 150, 24, "1 ТБ", 5299)
    data_storager_input("WD Blue 500 GB", 24, "Таилнад", "WD Blue (WD5000AZLX)", 7200, 150, 30, "512 ГБ", 4499)
    data_storager_input("Toshiba P300", 24, "Китай", "Toshiba P300 (HDWD105UZSVA)", 7200, 191, 26, "512 ГБ", 4599)


# -------------POWER UNIT DATA----------------
# функция создания конструктора
def puinput(k1, k2, k3, k4, k5, k6, k7, k8, k9):
    cursor.execute(
        "INSERT OR IGNORE INTO `pu` (`name`,`guarantee`,`creator`,`model`,`color`,`certificate`,`form_factor`,`power`,`cost`) VALUES (?,?,?,?,?,?,?,?,?)",
        (k1, k2, k3, k4, k5, k6, k7, k8, k9))

# добавление элементов в БД
def create_power_unit_data():
    puinput("Chieftec CORE 700W", 24, "Китай", "Chieftec CORE 700W", "черный", "80+ Gold", "ATX", 700, 6999)
    puinput("Cougar STX 700W", 36, "Китай", "Cougar STX 700W", "черный", "80+ Bronze", "ATX", 700, 3999)
    puinput("AeroCool AERO BRONZE 750W", 24, "Китай", "AeroCool AERO BRONZE 750W", "черный", "80+ Bronze", "ATX", 750,
            4899)
    puinput("Cougar GEC 650", 24, "Китай", "Cougar GEC 650", "черный", "80+ Gold", "ATX", 650, 5711)


# ----------------------------------------------------------------------------------------------------

# -------------ПОДКЛЮЧЕНИЕ И ИЗМЕНЕНИЕ БАЗЫ ДАННЫХ----------------

try:
    connect = sqlite3.connect('items.db')
    cursor = connect.cursor()

    # Создание таблицы материнских план в базе данных
    create_motherboard_data()
    # Создание таблицы процессоров в базе данных
    create_cpu_data()
    # Создание таблицы корпусов в базе данных
    create_corp_data()
    # Создание таблицы видеокарт в базе данных
    create_videocards_data()
    # Создание таблицы хранения данных в базе данных
    create_hdd_data()
    # Создание таблицы кулеров в базе данных
    create_cooler_data()
    # Создание таблицы блоков питания в базе данных
    create_power_unit_data()
    # Создание таблицы ОЗУ в базе данных
    create_ram_data()

    records = cursor.fetchall()

    # Подтверждение изменений
    connect.commit()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)

finally:
    if (connect):
        connect.close()


# ----------------------------------------------------------------------------------------------------


# -------------ОТВЕТ БОТА НА КОМАНДУ /START----------------

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    key_go = types.InlineKeyboardButton(text='Перейти к сборке компьютера.', callback_data='go')
    keyboard.add(key_go)
    key_about = types.InlineKeyboardButton(text='Об авторах.', callback_data='about')
    keyboard.add(key_about)
    bot.reply_to(message,
                 "Здравсвтуйте, я - бот-ассисент 'Computer_Constructor'\nСегодня я помогу вам собрать максимально подхоящий для вас компьютер! Давайте начнем.\nP.S. Для продожения нажмите одну из кнопок...",
                 reply_markup=keyboard)


# -------------CALLBACK ФУНКЦИИ----------------

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global motherboard
    global CPU_value
    global corps
    global video_card
    global CPU_cooling
    global RAM_value
    global data_storage
    global power_unit
    global additional_details
    global motherboardtrue_1
    global motherboardtrue
    global cputrue_1
    global cputrue
    global corptrue
    global videocardstrue
    global coolertrue
    global ramtrue
    global hddtrue
    global putrue
    global itog
    global result_cost
    global resultValue

    # ----------------------------------------------------
    if call.data == 'go':
        result_cost = 0
        bot.send_message(call.message.chat.id,
                         "Шаг 1.\nВведите ваш бюджет! Именно от него будет зависеть предлагаемые детали...")
        bot.register_next_step_handler(call.message, all_mn)

    # ----------------------------------------------------

    if call.data == 'about':
        keyboard = types.InlineKeyboardMarkup()
        key_back = types.InlineKeyboardButton(text='Вернуться к начальному сообщению!', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id,
                         text="Добрый день/вечер!\nСоздатели данного бота: Марат Шахмоведев, Сергей Алимов\nПоддержать создателей:\nСбер: 4276 7001 3436 1660\nТинькофф: 5536 9141 1563 0000",
                         reply_markup=keyboard)

    # ----------------------------------------------------

    if call.data == 'back':
        keyboard = types.InlineKeyboardMarkup()
        key_go = types.InlineKeyboardButton(text='Перейти к сборке компьютера.', callback_data='go')
        keyboard.add(key_go)
        key_about = types.InlineKeyboardButton(text='Об авторах.', callback_data='about')
        keyboard.add(key_about)
        bot.send_message(call.message.chat.id,
                         "Здравсвтуйте, я - бот-ассисент 'Computer_Constructor'\nСегодня я помогу вам собрать максимально подхоящий для вас компьютер! Давайте начнем.\nP.S. Для продожения нажмите одну из кнопок...",
                         reply_markup=keyboard)

    # ----------------------------------------------------

    if call.data == 'yes':
        _checkall(3)
        keyboard = types.InlineKeyboardMarkup()
        key_proc = types.InlineKeyboardButton(text='С процессора!', callback_data='proc')
        keyboard.add(key_proc)
        key_motherboard = types.InlineKeyboardButton(text='С материнской платы!', callback_data='motherboard')
        keyboard.add(key_motherboard)

        if (resultValue == 8):
            bot.send_message(call.message.chat.id,
                             "Шаг 2 . Переход непосредственно к сборке. Выберите с чего вы хотите начать сборку (Процессора или Материнской платы)",
                             reply_markup=keyboard)
        else:
            bot.send_message(call.message.chat.id,
                             "Ваш бюджет слишком мал, пожалуйста, введите больше, если хотите продолжить сборку!")
            bot.register_next_step_handler(call.message, all_mn)

    # ----------------------------------------------------

    if call.data == 'no':
        bot.send_message(call.message.chat.id,
                         "Введите ваш бюджет заново!")
        bot.register_next_step_handler(call.message, all_mn)

    # ----------------------------------------------------

    if call.data == 'proc':
        cputrue_1 = checkcpu1(3)
        bot.send_message(call.message.chat.id,
                         "Отлично! Выберите подходящий процессор!", reply_markup=cputrue_1)

    # ----------------------------------------------------

    if call.data == 'motherboard':
        motherboardtrue_1 = checkmotherboard(3)
        bot.send_message(call.message.chat.id,
                         "Отлично! Выберите подходящую материнскую плату!", reply_markup=motherboardtrue_1)

    # ----------------------------------------------------

    if call.data == 'proc_input':
        cputrue = checkcpu(3)
        bot.send_message(call.message.chat.id,
                         "Отлично, расчёт прошел успешно!\nВыберите подходящий процессор!", reply_markup=cputrue)

    # ----------------------------------------------------

    if call.data == 'motherboard_input':
        motherboardtrue = checkmotherboard1(3)
        bot.send_message(call.message.chat.id,
                         "Отлично, расчёт прошел успешно!\nВыберите подходящую материнскую плату!",
                         reply_markup=motherboardtrue)

    # ----------------------------------------------------

    if call.data == 'corp_input':
        corptrue = checkcorp(3)
        bot.send_message(call.message.chat.id,
                         "Отлично!\nВыберите подходящий корпус!",
                         reply_markup=corptrue)
    # ----------------------------------------------------

    if call.data == 'videocards_input':
        videocardstrue = checkvideo(3)
        bot.send_message(call.message.chat.id,
                         "Расчёт окончен!\nВыберите подходящую видеокарту!",
                         reply_markup=videocardstrue)
    # ----------------------------------------------------

    if call.data == 'cool_input':
        coolertrue = checkcool(3)
        bot.send_message(call.message.chat.id,
                         "Расчёт окончен!\nВыберите подходящий кулер!",
                         reply_markup=coolertrue)

    # ----------------------------------------------------

    if call.data == 'ram_input':
        ramtrue = checkram(3)
        bot.send_message(call.message.chat.id,
                         "Расчёт окончен!\nВыберите подходящую ОЗУ!",
                         reply_markup=ramtrue)
    # ----------------------------------------------------

    if call.data == 'hdd_input':
        hddtrue = checkhdd(3)
        bot.send_message(call.message.chat.id,
                         "Расчёт окончен!\nВыберите подходящий жесткий диск!",
                         reply_markup=hddtrue)

    # ----------------------------------------------------

    if call.data == 'pu_input':
        putrue = checkpu(4)
        bot.send_message(call.message.chat.id,
                         "Расчёт окончен!\nВыберите подходящий блок питания!",
                         reply_markup=putrue)

    # ----------------------------------------------------

    if call.data == 'itog':
        keyboard = types.InlineKeyboardMarkup()
        key_complete = types.InlineKeyboardButton(text='Подтвердить!', callback_data='complete')
        keyboard.add(key_complete)
        key_return = types.InlineKeyboardButton(text='Вернуться к началу сборки!', callback_data='go')
        keyboard.add(key_return)
        text = "Итоговая сборка:\n\nМатеринская плата: " + motherboardname + "\n\nПроцессор: " + procname + "\n\nКорпус: " + corp_name + "\n\nВидеокарта: " + video_card_name + "\n\nОхлаждение: " + cpu_cooling_name + "\n\nОперативная память (ОЗУ): " + ram_value_name + "\n\nЖесткий диск: " + data_storage_name + "\n\nБлок питания: " + power_unit_name + "\n\nОбщая стоимость: " + str(
            result_cost)
        bot.send_message(call.message.chat.id,
                         text,
                         reply_markup=keyboard)
    # ----------------------------------------------------
    if call.data == 'complete':
        keyboard = types.InlineKeyboardMarkup()
        key_mainmenu = types.InlineKeyboardButton(text='Вернуться в главное меню!', callback_data='back')
        keyboard.add(key_mainmenu)
        text = "Огромная благодарность за то, что вы выбрали именно меня в качестве вашего помощника! Надеюсь, я буду полезен вам ещё!"
        bot.send_message(call.message.chat.id,
                         text,
                         reply_markup=keyboard)


# -------------ОТВЕТ БОТА НА ЛЮБОЕ СООБЩЕНИЕ ПОЛЬЗОВАТЕЛЯ----------------

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # -------------СОЗДАНИЕ ХАРАКТЕРИСТИКИ ДЛЯ ВСЕХ ДЕТАЛЕЙ----------------

    # ПЕРЕМЕННЫЕ ДЛЯ ПРОВЕРКИ И УСПЕШНОЙ РЕАЛИЗАЦИИ СБОРКИ
    global xmw

    # -------------ХАРАКТЕРИСТИКА МАТЕРИНСКОЙ ПЛАТЫ----------------

    def charac(name):
        global socketmotherboard
        global motherboardname
        global motherboardform
        global result_cost
        try:
            sqlite_connection = sqlite3.connect('items.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from motherboards where name = ?"""
            cursor.execute(sqlite_select_query, (name,))
            record = cursor.fetchone()
            text = "ХАРАКТЕРИСТИКА МАТЕРИНСКОЙ ПЛАТЫ\nНазвание: " + str(record[0]) + "\nГарантия: " + str(
                record[1]) + "мес." + "\nСтрана-производитель: " + str(record[2]) + "\nМодель: " + str(
                record[3]) + "\nГод релиза: " + str(record[4]) + "\nФорм-фактор: " + str(
                record[5]) + "\nВысота: " + str(record[6]) + "\nШирина: " + str(record[7]) + "\nСокет: " + str(
                record[8]) + "\nЧипсет Intel: " + str(record[9]) + "\nКоличество слотов памяти: " + str(
                record[10]) + "\nФорм фактор поддерживаемой памяти: " + str(
                record[11]) + "\nТип поддерживаемой памяти: " + str(record[12]) + "\nКоличество каналов памяти: " + str(
                record[13]) + "\nМаксимальный объем памяти: " + str(record[14]) + "\nВерсия PCI Express: " + str(
                record[15]) + "\nКоличество слотов PCI-E x16: " + str(
                record[16]) + "\nКоличество USB на задней панели: " + str(record[17]) + "\nВидеовыходы: " + str(
                record[18]) + "\nЗвуковая схема: " + str(record[19]) + "\nЧипсет звукового адаптера: " + str(
                record[21]) + "\nСкорость сетевого адаптера: " + str(
                record[22]) + " Гбит/c" + "\nЧипсет сетевого адаптера: " + str(record[23]) + "\nЦЕНА: " + str(
                record[24])
            result_cost += record[24]
            socketmotherboard = record[8]
            motherboardname = record[0]
            motherboardform = record[5]
            bot.send_message(message.from_user.id, text,
                             reply_markup=keyboardmotherboardbackoradd)
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    # -------------ХАРАКТЕРИСТИКА ПРОЦЕССОРА----------------

    def charac1(name):
        global procname
        global socketproc
        global result_cost

        try:
            sqlite_connection = sqlite3.connect('items.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from cpu where name = ?"""
            cursor.execute(sqlite_select_query, (name,))
            record = cursor.fetchone()
            text = "ХАРАКТЕРИСТИКА ПРОЦЕССОРА\nНазвание: " + str(record[0]) + "\nГарантия: " + str(
                record[1]) + " мес." + "\nСтрана-производитель: " + str(record[2]) + "\nМодель: " + str(
                record[3]) + "\nСокет: " + str(record[4]) + "\nГод релиза: " + str(
                record[5]) + "\nМаксимальное число потоков: " + str(
                record[6]) + "\nКоличество производительных ядер: " + str(
                record[7]) + "\nБазовая частота процессора: " + str(
                record[8]) + "\nТип памяти: " + str(record[9]) + "\nМаксимально поддерживаемый объем памяти: " + str(
                record[10]) + "\nМаксимальная температура процессора: " + str(
                record[11]) + "\nЦена: " + str(record[12])
            procname = record[0]
            socketproc = record[4]
            result_cost += record[12]
            bot.send_message(message.from_user.id, text, reply_markup=keyboardcpubackoradd)
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    # -------------ХАРАКТЕРИСТИКА КОРПУСА----------------

    def charac2(name):
        global corp_name
        global width_corp
        global result_cost

        try:
            sqlite_connection = sqlite3.connect('items.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from corp where name = ?"""
            cursor.execute(sqlite_select_query, (name,))
            record = cursor.fetchone()
            text = "ХАРАКТЕРИСТИКА КОРПУСА\nНазвание: " + str(record[0]) + "\nГарантия: " + str(
                record[1]) + " мес." + "\nСтрана-производитель: " + str(record[2]) + "\nМодель: " + str(
                record[3]) + "\nВысота: " + str(record[4]) + "\nШирина: " + str(
                record[5]) + "\nДлина: " + str(
                record[6]) + "\nЦвет: " + str(
                record[7]) + "\nМатериал: " + str(
                record[8]) + "\nПоддерживаемые форм факторы: " + str(
                record[9]) + ", " + str(
                record[10]) + ",     " + str(
                record[11]) + "\nЦена: " + str(record[12])
            corp_name = record[0]
            width_corp = record[5]
            result_cost += record[12]
            bot.send_message(message.from_user.id, text, reply_markup=keyboardcorpbackoradd)
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    # -------------ХАРАКТЕРИСТИКА ВИДЕОКАРТЫ----------------

    def charac3(name):
        global video_card_name
        global result_cost
        try:
            sqlite_connection = sqlite3.connect('items.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from videocards where name = ?"""
            cursor.execute(sqlite_select_query, (name,))
            record = cursor.fetchone()
            text = "ХАРАКТЕРИСТИКА ВИДЕОКАРТЫ\nНазвание: " + str(record[0]) + "\nГарантия: " + str(
                record[1]) + " мес." + "\nСтрана-производитель: " + str(record[2]) + "\nМодель: " + str(
                record[3]) + "\nГрафический процессор: " + str(record[4]) + "\nВидеопамять: " + str(
                record[5]) + "\nТип памяти: " + str(
                record[6]) + "\nТип охлаждения: " + str(
                record[7]) + "\nЦена: " + str(
                record[8])
            video_card_name = record[0]
            result_cost += record[8]
            bot.send_message(message.from_user.id, text, reply_markup=keyboardvideobackoradd)
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    # -------------ХАРАКТЕРИСТИКА КУЛЕРА----------------

    def charac4(name):
        global cpu_cooling_name
        global result_cost
        try:
            sqlite_connection = sqlite3.connect('items.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from coolers where name = ?"""
            cursor.execute(sqlite_select_query, (name,))
            record = cursor.fetchone()
            text = "ХАРАКТЕРИСТИКА КУЛЕРА:\nНазвание: " + str(record[0]) + "\nГарантия: " + str(
                record[1]) + " мес." + "\nМодель: " + str(record[2]) + "\nТеплогашение: " + str(
                record[3]) + "\nТепловые трубки: " + str(record[4]) + "\nЦвет: " + str(
                record[5]) + "\nМаксимальная скорость: " + str(
                record[6]) + "\nШум: " + str(
                record[7]) + "\nВысота: " + str(
                record[8]) + "\nЦена: " + str(
                record[9])
            cpu_cooling_name = record[0]
            result_cost += record[9]
            bot.send_message(message.from_user.id, text, reply_markup=keyboardcoolbackoradd)
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    # -------------ХАРАКТЕРИСТИКА ОЗУ----------------

    def charac5(name):
        global ram_value_name
        global result_cost
        try:
            sqlite_connection = sqlite3.connect('items.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from ram where name = ?"""
            cursor.execute(sqlite_select_query, (name,))
            record = cursor.fetchone()
            text = "ХАРАКТЕРИСТИКА ОЗУ:\nНазвание: " + str(record[0]) + "\nГарантия: " + str(
                record[1]) + " мес." + "\nСтрана-производитель: " + str(record[2]) + "\nМодель: " + str(
                record[3]) + "\nЦвет: " + str(record[4]) + "\nТип: " + str(
                record[5]) + "\nОбъем одной плашки: " + str(
                record[6]) + "\nОбъем всего комплекта: " + str(
                record[7]) + "\nЧастота: " + str(
                record[8]) + "\nТайминги: " + str(
                record[9]) + "\nЦена: " + str(record[10])
            ram_value_name = record[0]
            result_cost += int(record[10])
            bot.send_message(message.from_user.id, text, reply_markup=keyboardrambackoradd)
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    # -------------ХАРАКТЕРИСТИКА HDD----------------

    def charac6(name):
        global data_storage_name
        global result_cost
        try:
            sqlite_connection = sqlite3.connect('items.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from hdd where name = ?"""
            cursor.execute(sqlite_select_query, (name,))
            record = cursor.fetchone()
            text = "ХАРАКТЕРИСТИКА ЖЕСТКОГО ДИСКА:\nНазвание: " + str(record[0]) + "\nГарантия: " + str(
                record[1]) + " мес." + "\nСтрана-производитель: " + str(record[2]) + "\nМодель: " + str(
                record[3]) + "\nМаксимальная скорость вращение: " + str(
                record[4]) + "\nМаксимальная скорость записи данных: " + str(record[5]) + "\nШум: " + str(
                record[6]) + "\nОбъем: " + str(record[7]) + "\nЦена: " + str(record[8])
            data_storage_name = record[0]
            result_cost += record[8]
            bot.send_message(message.from_user.id, text, reply_markup=keyboardhddbackoradd)
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    # -------------ХАРАКТЕРИСТИКА БЛОКА ПИТАНИЯ----------------

    def charac7(name):
        global power_unit_name
        global result_cost
        try:
            sqlite_connection = sqlite3.connect('items.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from pu where name = ?"""
            cursor.execute(sqlite_select_query, (name,))
            record = cursor.fetchone()
            text = "ХАРАКТЕРИСТИКА БЛОКА ПИТАНИЯ:\nНазвание: " + str(record[0]) + "\nГарантия: " + str(
                record[1]) + " мес." + "\nСтрана-производитель: " + str(record[2]) + "\nМодель: " + str(
                record[3]) + "\nЦвет: " + str(record[4]) + "\nСертификат: " + str(
                record[5]) + "\nФорм фактор: " + str(
                record[6]) + "\nМощность: " + str(
                record[7]) + "\nЦена: " + str(
                record[8])
            power_unit_name = record[0]
            result_cost += record[8]
            bot.send_message(message.from_user.id, text, reply_markup=keyboardpubackoradd)
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()

    # -------------ОТВЕТЫ НА СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЯ----------------

    if message.text == 'GIGABYTE H610M S2H':
        charac("GIGABYTE H610M S2H")
        ph = open("img/motherboard_img/GIGABYTE_H610M_S2H/ph1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'MSI MAG B560M BAZOOKA':
        charac("MSI MAG B560M BAZOOKA")
        ph = open("img/motherboard_img/MSI_MAG_B560M_BAZOOKA/1.jpg", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'MSI PRO B660M-A DDR4':
        charac("MSI PRO B660M-A DDR4")
        ph = open("img/motherboard_img/MSI_PRO_B660M-A_DDR4/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Intel Core i3-12100F OEM':
        charac1('Intel Core i3-12100F OEM')
        ph = open("img/cpu_img/Intel_Core_i3-12100F_OEM/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Intel Core i5-12400F OEM':
        charac1('Intel Core i5-12400F OEM')
        ph = open("img/cpu_img/Intel_Core_i5-12400F_OEM/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Intel Core i5-11400F OEM':
        charac1('Intel Core i5-11400F OEM')
        ph = open("img/cpu_img/Intel_Core_i5-11400F_OEM/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Добавить материнскую плату в сборку':
        if xmw == 0:
            keyboard = types.InlineKeyboardMarkup()
            key_proc = types.InlineKeyboardButton(text='Расчитать подходящий процессор!', callback_data='proc_input')
            keyboard.add(key_proc)
            bot.send_message(message.chat.id,
                             "Супер, Вы молодец!\nДалее нажмите на кнопку ниже, чтобы мы могли подобрать процессоры, подходящий именно для вас!",
                             reply_markup=keyboard)
        else:
            keyboard = types.InlineKeyboardMarkup()
            key_corp = types.InlineKeyboardButton(text='Подобрать подходящие корпуса!', callback_data='corp_input')
            keyboard.add(key_corp)
            bot.send_message(message.chat.id,
                             "Супер, двигаемся дальше!\nДалее нажмите на кнопку ниже, чтобы мы могли подобрать корпуса, подходящие именно для вас!",
                             reply_markup=keyboard)

    # ----------------------------------------------------

    elif message.text == 'Добавить процессор в сборку':
        if xmw == 1:
            keyboard = types.InlineKeyboardMarkup()
            key_proc = types.InlineKeyboardButton(text='Расчитать подходящие материнские платы!',
                                                  callback_data='motherboard_input')
            keyboard.add(key_proc)
            bot.send_message(message.chat.id,
                             "Супер, Вы молодец!\nДалее нажмите на кнопку ниже, чтобы мы могли подобрать материнские платы, подходящие именно для вас!",
                             reply_markup=keyboard)
        else:
            keyboard = types.InlineKeyboardMarkup()
            key_corp = types.InlineKeyboardButton(text='Подобрать подходящие корпуса!', callback_data='corp_input')
            keyboard.add(key_corp)
            bot.send_message(message.chat.id,
                             "Супер, двигаемся дальше!\nДалее нажмите на кнопку ниже, чтобы мы могли подобрать корпуса, подходящие именно для вас!",
                             reply_markup=keyboard)

    # ----------------------------------------------------

    elif message.text == 'Вернуться к выбору материнской платы':
        if motherboardtrue_1 == 0:
            bot.send_message(message.chat.id,
                             "Выберите подходящую материнскую плату!", reply_markup=motherboardtrue)
        else:
            bot.send_message(message.chat.id,
                             "Выберите подходящую материнскую плату!", reply_markup=motherboardtrue_1)

    # ----------------------------------------------------

    elif message.text == 'Вернуться к выбору процессоров':
        if cputrue_1 == 0:
            bot.send_message(message.chat.id,
                             "Выберите подходящий процессор!", reply_markup=cputrue)
        else:
            bot.send_message(message.chat.id,
                             "Выберите подходящий процессор!", reply_markup=cputrue_1)


    # ----------------------------------------------------

    elif message.text == 'AeroCool SI-5200 Window':
        charac2("AeroCool SI-5200 Window")
        ph = open("img/corp_img/AeroCool_SI-5200_Window/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'DEEPCOOL MATREXX 50 MESH 4FS':
        charac2("DEEPCOOL MATREXX 50 MESH 4FS")
        ph = open("img/corp_img/DEEPCOOL_MATREXX_50_MESH_4FS/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Cougar MX330-F':
        charac2("Cougar MX330-F")
        ph = open("img/corp_img/Cougar_MX330-F/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Добавить корпус в сборку':
        keyboard = types.InlineKeyboardMarkup()
        key_video = types.InlineKeyboardButton(text='Расчитать подходящие видеокарты!',
                                               callback_data='videocards_input')
        keyboard.add(key_video)
        bot.send_message(message.chat.id,
                         "Все складывается просто идеально!\nДалее нажмите на кнопку ниже, чтобы мы могли подобрать видокарты!",
                         reply_markup=keyboard)

    # ----------------------------------------------------

    elif message.text == 'Вернуться к выбору корпусов':
        bot.send_message(message.chat.id,
                         "Выберите подходящий корпус!", reply_markup=corptrue)

    # ----------------------------------------------------

    elif message.text == 'ASRock AMD Radeon RX 6500 XT Phantom Gaming D OC':
        charac3("ASRock AMD Radeon RX 6500 XT Phantom Gaming D OC")
        ph = open("img/videocard_img/ASRock_AMD_Radeon_RX_6500_XT_Phantom_Gaming_D_OC/1.jpeg", 'rb')
        bot.send_photo(message.from_user.id, ph)
    # ----------------------------------------------------

    elif message.text == 'Palit GeForce RTX 3050 Dual OC':
        charac3("Palit GeForce RTX 3050 Dual OC")
        ph = open("img/videocard_img/Palit_GeForce_RTX_3050_Dual_OC/1.jpg", 'rb')
        bot.send_photo(message.from_user.id, ph)
    # ----------------------------------------------------

    elif message.text == 'Palit GeForce RTX 3060 Ti DUAL':
        charac3("Palit GeForce RTX 3060 Ti DUAL")
        ph = open("img/videocard_img/Palit_GeForce_RTX_3060_Ti_DUAL/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Вернуться к выбору видеокарт':
        bot.send_message(message.chat.id,
                         "Выберите подходящую видеокарту!", reply_markup=videocardstrue)

    # ----------------------------------------------------

    elif message.text == 'Добавить видеокарту в сборку':
        keyboard = types.InlineKeyboardMarkup()
        key_cool = types.InlineKeyboardButton(text='Расчитать подходящие кулеры!',
                                              callback_data='cool_input')
        keyboard.add(key_cool)
        bot.send_message(message.chat.id,
                         "Вы огромный молодец!\nДалее нажмите на кнопку ниже, чтобы мы могли подобрать кулеры!",
                         reply_markup=keyboard)

    # ----------------------------------------------------

    elif message.text == 'Cooler Master Hyper 212 Black Edition':
        charac4("Cooler Master Hyper 212 Black Edition")
        ph = open("img/cool_img/Cooler_Master_Hyper_212_Black_Edition/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'DEEPCOOL GAMMAXX 400 V2':
        charac4("DEEPCOOL GAMMAXX 400 V2")
        ph = open("img/cool_img/DEEPCOOL_GAMMAXX_400_V2/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'AeroCool Verkho 2 Dual':
        charac4("AeroCool Verkho 2 Dual")
        ph = open("img/cool_img/AeroCool_Verkho_2_Dual/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Вернуться к выбору кулера':
        bot.send_message(message.chat.id,
                         "Выберите подходящий кулер!", reply_markup=coolertrue)

    # ----------------------------------------------------

    elif message.text == 'Добавить кулер в сборку':
        keyboard = types.InlineKeyboardMarkup()
        key_ram = types.InlineKeyboardButton(text='Подобрать подходящую оперативную память (ОЗУ)',
                                             callback_data='ram_input')
        keyboard.add(key_ram)
        bot.send_message(message.chat.id,
                         "Вы огромный молодец!\nДалее нажмите на кнопку ниже, чтобы мы могли подобрать ОЗУ!",
                         reply_markup=keyboard)

    # ---------------------------------------------------

    elif message.text == 'Patriot Viper 4 Blackout':
        charac5("Patriot Viper 4 Blackout")
        ph = open("img/ram_img/Patriot_Viper_4_Blackout/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Goodram Iridium':
        charac5("Goodram Iridium")
        ph = open("img/ram_img/Goodram_Iridium/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Kingston HyperX FURY Black':
        charac5("Kingston HyperX FURY Black")
        ph = open("img/ram_img/Kingston_HyperX_FURY_Black/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Вернуться к выбору ОЗУ':
        bot.send_message(message.chat.id,
                         "Выберите подходящую ОЗУ!", reply_markup=ramtrue)

    # ----------------------------------------------------

    elif message.text == 'Добавить ОЗУ в сборку':
        keyboard = types.InlineKeyboardMarkup()
        key_hdd = types.InlineKeyboardButton(text='Подобрать ЖЕСТКИЙ ДИСК',
                                             callback_data='hdd_input')
        keyboard.add(key_hdd)
        bot.send_message(message.chat.id,
                         "Супер!\nДалее нажмите на кнопку ниже, чтобы мы могли подобрать жесткий диск!",
                         reply_markup=keyboard)

    # ----------------------------------------------------
    elif message.text == 'WD Blue 1 TB':
        charac6("WD Blue 1 TB")
        ph = open("img/hdd_img/WD_Blue_1_TB/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'WD Blue 500 GB':
        charac6("WD Blue 500 GB")
        ph = open("img/hdd_img/WD_Blue_500_GB/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Toshiba P300':
        charac6("Toshiba P300")
        ph = open("img/hdd_img/Toshiba_P300/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Вернуться к выбору ЖЕСТКОГО ДИСКА':
        bot.send_message(message.chat.id,
                         "Выберите подходящий ЖЕСТКИЙ ДИСК!", reply_markup=hddtrue)

    # ----------------------------------------------------

    elif message.text == 'Добавить данный ЖЕСТКИЙ ДИСК в сборку':
        keyboard = types.InlineKeyboardMarkup()
        key_pu = types.InlineKeyboardButton(text='Подобрать БЛОК ПИТАНИЯ',
                                            callback_data='pu_input')
        keyboard.add(key_pu)
        bot.send_message(message.chat.id,
                         "Супер!\nДалее нажмите на кнопку ниже, чтобы мы могли подобрать блок питания!",
                         reply_markup=keyboard)

    # ----------------------------------------------------

    elif message.text == 'Chieftec CORE 700W':
        charac7("Chieftec CORE 700W")
        ph = open("img/pu_img/Chieftec_CORE_700W/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Cougar STX 700W':
        charac7("Cougar STX 700W")
        ph = open("img/pu_img/Cougar_STX_700W/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'AeroCool AERO BRONZE 750W':
        charac7("AeroCool AERO BRONZE 750W")
        ph = open("img/pu_img/AeroCool_AERO_BRONZE_750W/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Cougar GEC 650':
        charac7("Cougar GEC 650")
        ph = open("img/pu_img/Cougar_GEC_650/1.PNG", 'rb')
        bot.send_photo(message.from_user.id, ph)

    # ----------------------------------------------------

    elif message.text == 'Вернуться к выбору Блока питания':
        bot.send_message(message.chat.id,
                         "Выберите подходящий Блок питания!", reply_markup=putrue)

    # ----------------------------------------------------

    elif message.text == 'Добавить данный Блок питания в сборку':
        keyboard = types.InlineKeyboardMarkup()
        key_itog = types.InlineKeyboardButton(text='Итоговая сборка',
                                              callback_data='itog')
        keyboard.add(key_itog)
        keyboard1 = types.InlineKeyboardMarkup()
        key_adddet = types.InlineKeyboardButton(text='Добавить дополнительные детали!',
                                                callback_data='adddet_input')
        keyboard1.add(key_adddet)
        bot.send_message(message.chat.id,
                         "Супер, вы закончили сборку!\nДалее нажмите на кнопку ниже, чтобы посмотреть итоговую сборку!",
                         reply_markup=keyboard)

    # ----------------------------------------------------

    # ----------------------------------------------------

    else:
        bot.reply_to(message, 'Пожалуйста, введите команду /start и следуйте инструкциям!')


# ----------------------ФУНКЦИЯ ВВОДА БЮДЖЕТА------------------------------
def all_mn(message):
    global money
    global motherboard
    global CPU_value
    global corps
    global video_card
    global CPU_cooling
    global RAM_value
    global data_storage
    global power_unit
    if (message.text.isdigit()):
        money = int(message.text)
        motherboard = (8999 / 76043) * money
        CPU_value = (16999 / 76043) * money
        corps = (3099 / 76043) * money
        video_card = (30999 / 76043) * money
        CPU_cooling = (1250 / 76043) * money
        RAM_value = (6199 / 76043) * money
        data_storage = (4499 / 76043) * money
        power_unit = (3999 / 76043) * money
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да!', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет!', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, "Ваш бюджет: " + str(money) + "₽  ?", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id,
                         "Введите бюджет корректно!\nБюджет должен быть введен цифрами и отличен от 0...")

        bot.register_next_step_handler(message, all_mn)

#Бесконечная работа бота, пока он включен
bot.infinity_polling()
