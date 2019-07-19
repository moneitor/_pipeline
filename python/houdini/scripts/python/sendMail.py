import smtplib as s

def sendMailto (email , password , nodeName):
    mymail = '3d.hernan@gmail.com'
    conn = s.SMTP("smtp.gmail.com" , 587)
    conn.ehlo()
    conn.starttls()
    conn.login(mymail , 'moneitor1053')
    conn.sendmail(mymail , mymail , 'Subject: The render of node, is done. ')

    conn.quit() 


