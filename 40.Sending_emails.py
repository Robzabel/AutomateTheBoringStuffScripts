import smtplib
connectionObject = smtplib.SMTP('smtp.gmail.com', 587) #create a connection object to the smtp server
print(type(connectionObject)) #see that the the connection object belongs to the SMTP class
connectionObject.ehlo() #this is the function that starts the connection
connectionObject.starttls() # start the tls protocol for password encryption
connectionObject.login('**********@gmail.com', '**********')#login to the gmail server
connectionObject.sendmail('***********@gmail.com','*********@gmail.com', 'subject: test1\n\nThis is the third test')
"""in the line above is how you need to send the email, source address first then destination then headers and message
 the source email is not important becasue modern servers take it from the log in but it needs to be there or the 
 other parts are out of argumental position"""
connectionObject.quit() #this will disconnect from the mail server
