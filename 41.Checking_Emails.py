import imapclient, pyzmail
connectionObject = imapclient.IMAPClient('imap.gmail.com', ssl=True)#create connection object
print(connectionObject.login('ro************@gmail.com', '*******'))#print the login call to see if it was a success
connectionObject.select_folder('INBOX', readonly=True)#select the inbox folder and put it in read only
UID = connectionObject.search(['SINCE', '07-Jul-2020'])   #this returns Unique IDs of each message
print(UID)#print the UIDs
rawMessage = connectionObject.fetch([1],['BODY[]', 'FLAGS'])#grab the body and the flag data from the message with ID 1
message = pyzmail.PyzMessage.factory(rawMessage[1][b'BODY[]'])#create a pyzemail objecto of the message
print(message.get_subject())#get the message subject
print(message.get_address('from'))#get the senders details
