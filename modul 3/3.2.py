# комментарии не читайте!!! все для обучения на pythontutor.com

def send_email(message, recipient, sender="university.help@gmail.com"):
    # Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net"
    if '@' not in recipient or '@' not in sender:
        print(f' Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')

    if '.com' not in recipient or '.com' not in sender:
        print(2)
    if  '.ru' not in recipient or '.ru' not in sender:
        print(3)
    if '.net' not in recipient or '.net' not in sender:
        print(f' Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    if sender == recipient:
        print(f' Нельзя отправить письмо самому себе!')
    # Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    if sender == 'university.help@gmail.com':
        ## Если же отправитель по умолчанию - university.help@gmail.com, то вывести
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        # else:
        #     print(2)

        # В противном случае вывести сообщение:
    # else:
    #     print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info_gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher_mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
