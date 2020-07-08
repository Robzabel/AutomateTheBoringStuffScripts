import PyPDF2
import os
os.chdir('/home/zabex/Documents/automate_online-materials/')#get to the correct directory of the file
pdfFile = open('meetingminutes.pdf', 'rb')#open the file in read binary mode
reader = PyPDF2.PdfFileReader(pdfFile)#change the file object into a pdf reader object and store ina variable
print(reader.numPages) # print the number of pages in the object
page = reader.getPage(0) #get the data from a page and store it in a variable
print(page.extractText())#return the text off the page.
for page in range(reader.numPages): #create a for loop to grab all the data from the entire PDF
    print(reader.getPage(page).extractText())