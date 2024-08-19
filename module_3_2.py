def is_email (a): #проверяем правильность email согласно ТЗ
    suffix = ('.com', '.ru', '.net') # допустимые домены

    if not "@" in a:  # проверка на наличие @

        return False
    elif not a.endswith(suffix): #проверяем допустимые домены

        return False

    else:
        return True

def send_email(messege, recipient, sender = "university.help@gmail.com"):
    if not is_email(recipient) or not is_email(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return
    if  recipient == sender :
         print("Нельзя отправить письмо самому себе!")
         return
    if sender == "university.help@gmail.com" :
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

    else :
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")




    #print (messege, recipient, sender)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
