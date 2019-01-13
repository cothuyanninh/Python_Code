import smtplib
import config

SUBJECT = open('subject.txt', 'r', encoding ='utf-8').read()[1:]
TEXT = open('data.txt', 'r', encoding ='utf-8').read()[1:]
TO = open('input.txt', 'r', encoding ='utf-8').readlines()

# SUBJECT = r"Thông báo toàn thể sinh viên trong trường"
# TEXT = r"Đây là tin nhắn test"
# TO =["hanquocso01@gmail.com","hanquocso02@gmail.com","cothuyanninh@gmail.com"]
# print(SUBJECT)
# print(TEXT)
# print(TO)
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(config.USERNAME, config.PASSWORD)
BODY = '\r\n'.join(['To: %s' % TO,'From: %s' % config.USERNAME,'Subject: %s' % SUBJECT,'', TEXT])
smtpObj.sendmail(config.USERNAME, TO, BODY.encode("utf8"))
smtpObj.quit()
