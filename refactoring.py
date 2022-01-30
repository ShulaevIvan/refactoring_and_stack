import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail_Client:
    def __init__(self, login, password_):
        self.connect = {'login': login, 'password': password_}

    def send_mail(self, srv, port, recipients, head, subject):
        
        try:
            
            msg = MIMEMultipart()
            msg['From'] = self.connect['login']
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            msg.attach(MIMEText(head))
            auth_smtp = smtplib.SMTP(srv, port)
            auth_smtp.ehlo()
            auth_smtp.starttls()
            auth_smtp.ehlo()
            auth_smtp.login(self.connect['login'], self.connect['password'])
            result = auth_smtp.sendmail(msg['From'], msg['To'], msg.as_string())
            auth_smtp.quit()
            
            return result
        
        except Exception as Err:
            return f'Error sending data: {Err}'

    def receive_mail(self, srv, box, header_=None):
        
        auth_imap = imaplib.IMAP4_SSL(srv)
        
        try:
            
            auth_imap.login(self.connect['login'], self.connect['password'])
            auth_imap.list()
            auth_imap.select(box)
            criterion = '(HEADER Subject "%s")' % header_ if header_ else 'ALL'
            result, data = auth_imap.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = auth_imap.uid('fetch', latest_email_uid.decode('utf-8'), '(RFC822)')
            raw_email = data[0][1]
            take_mail = email.message_from_string(raw_email.decode('utf-8'))
            auth_imap.logout()
            
            return take_mail
        
        except Exception as Err:
            
            return f'Data acquisition error:{Err}'


if __name__ == '__main__':
    gmail = Mail_Client('test9@gmail.com', 'testpass')
    gmail.send_mail(
        'smtp.gmail.com',
        587,
        ['vasya@email.com', 'petya@email.com'],
        'this is test message',
        'test Header'
    )
    gmail.receive_mail('imap.gmail.com', 'inbox')