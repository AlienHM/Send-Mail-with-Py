import getpass                                                                                             
import smtplib                                                                        
HOST = 'smtp.gmail.com'                                                                                  
PORT = 465

username = 'moltenhair.az@gmail.com'
password = 'uddgkhwehpmhzkaz'

server = smtplib.SMTP_SSL(HOST, PORT)

server.login(username, password)
send_to = input('Send mail to : ').replace(' ', '').split(',')
subject = input('Subject :')
text = input('Write your message :')
message = 'Subject: {}\n\n{}'.format(subject, text)


try:
    server.sendmail(
    	username,       
    	send_to,
    	message,
    )
    print("Mail successfully sent !")
except:
    print("Mail could not sent !")
    
server.quit()