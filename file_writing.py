from csv import reader, DictReader
from os.path import exists


def creating():
    file = 'phone.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия,Имя,Номер\n')


def writing_csv(info):
    file = 'phone.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]}\n')


def reading_csv(file):
    with open(file, encoding='utf-8') as data:
        res = list(DictReader(data))
    return res


def get_info():
    info = []
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    info.append(last_name)
    info.append(first_name)
    phone_number = ''
    flag = False
    while not flag:
        try:
            phone_number = input("Введите номер: ")
            if len(phone_number) != 11:
                print("В номере должно быть 11 цифр")
            else:
                phone_number = int(phone_number)
                flag = True

        except:
            print("В номере должны быть только цифры")

    info.append(phone_number)
    return info


def record_info():
    info = get_info()
    writing_csv(info)


def view():
    print(reading_csv('phone.csv'))


def delete_contact():
    file = 'phone.csv'
    with open(file, "r", encoding="utf8") as data:
        tel_book = data.read()
        print(tel_book)
        index_delete_data = int(input("Введите номер строки для удаления: "))
        tel_book_lines = tel_book.split("\n")
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        print(f"Удалена запись: {del_tel_book_lines}\n")
        with open(file, "w", encoding="utf8") as data:
            data.write("\n".join(tel_book_lines))


def change_contact():
    file = 'phone.csv'
    with open(file, "r", encoding="utf8") as data:
        tel_book = data.read()
        print(tel_book)
        index_delete_data = int(input("Введите номер строки для редактирования: "))
        tel_book_lines = tel_book.split("\n")
        edit_tel_book_lines = tel_book_lines[index_delete_data]
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        phone_number = ''
        flag = False
        while not flag:
            try:
                phone_number = input("Введите номер: ")
                # phone_number = '12345678911'
                if len(phone_number) != 11:
                    print("В номере должно быть 11 цифр")
                else:
                    phone_number = int(phone_number)
                    flag = True

            except:
                print("В номере должны быть только цифры")
        edited_line = (f'{last_name},{first_name},{phone_number}\n')
        tel_book_lines[index_delete_data] = edited_line
        print(f"Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n")
        with open(file, "w", encoding="utf8") as data:
            data.write("\n".join(tel_book_lines))


def main():
    while True:
        step = input("Введите действие: ")
        if step == 'q':
            break
        elif step == 'w':
            path = 'phone.csv'
            flag = exists(path)
            if not flag:
                creating()
                record_info()
            else:
                record_info()

        elif step == 'r':
            view()
        elif step == 'x':
            delete_contact()
        elif step == 'y':
            change_contact()


main()
