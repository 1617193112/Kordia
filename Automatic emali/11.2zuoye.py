import smtplib
import email.mime.multipart
import email.mime.text
for num in range(1,10):
     msg = email.mime.multipart.MIMEMultipart()
     msg['from'] = 'krs1711@163.com'
     msg['to'] = '765758646@qq.com'
     msg['subject'] = 'Lazy'
     content = "So lazy"
     txt = email.mime.text.MIMEText(content)
     msg.attach(txt)
     smtp = smtplib
     smtp = smtplib.SMTP()
     smtp.connect('smtp.163.com', '25')
     smtp.login('krs1711@163.com', 'qaz1470')
     smtp.sendmail('krs1711@163.com', '765758646@qq.com', str(msg))
     smtp.quit()
import  time
start_job = True
while start_job:
    time.sleep(60)