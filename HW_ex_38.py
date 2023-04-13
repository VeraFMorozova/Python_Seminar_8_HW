# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

def writing_person():
    lastname = input("фамилия : ")
    name = input("имя : ")
    surname = input("отчество : ")
    tel = input("телефон : ")
    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(f"{lastname} {name} {surname} {tel}\n")
    data.close()


def search():
    lookfor = input("кого ищем? ")
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)
            else:
                print("Поиск не дал результатов")
                                   
             
def print_phonebook():
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            print(line)


def load():
    new_phonebook = input("введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
                    data_1.write("\n")

def delete_data():
   data_str = input("Введите запись, которую необходимо удалить: ")
   with open("phonebook.txt", "r", encoding="utf-8") as data:
        lines=data.readlines()
        with open("phonebook.txt", "w", encoding="utf-8") as data_1:
            for line in lines:
                if data_str not in line:
                    data_1.write(line)
                else:
                    print(line)
                    ask = input("Удалить выбранную строку(да/нет) : ")
                    while ask not in ("да", "нет"):
                        print("Введен некорректный ответ")
                        ask = input("Удалить выбранную строку(да/нет) : ")
                    if ask == "нет":
                        data_1.write(line)

def change_data():
   data_str = input("Введите запись, которую необходимо изменить: ")
   with open("phonebook.txt", "r", encoding="utf-8") as data:
        lines=data.readlines()
        with open("phonebook.txt", "w", encoding="utf-8") as data_1:
            for line in lines:
                if data_str not in line:
                    data_1.write(line)
                else:
                    ask = int(input("Какие данные хотите изменить(1 - фамилия, 2 - имя, 3 - отчество, 4 - телефон) : "))
                    while ask not in (1,2,3,4):
                        print("Введен некорректный ответ")
                        ask = int(input("Какие данные хотите изменить(1 - фамилия, 2 - имя, 3 - отчество, 4 - телефон) : "))
                    new_data=input("Введите новые данные : ")
                    line_list=line.split()
                    line_list[int(ask)-1]=new_data
                    data_1.write("\t".join(line_list)+"\n")
                    
print ("""1 - добавление,
2 - поиск,
3 - вывод на экран,
4 - импорт в файл,
5 - удаление записи,
6 - изменение записи
""")
ask = int(input( ))
if ask ==1:
    writing_person()
elif ask ==2:
    search()
elif ask ==3:
    print_phonebook()
elif ask ==4: 
    load()
elif ask ==5: 
    delete_data()
elif ask ==6:
    change_data()
else:
    print("Нет такой команды")    