import requests,os
#pass an argument to the requests.get() method
print(os.getcwd())
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(response.status_code) # the txt file is stored in the response variable
print(len(response.text))# we can see the file is stored in the variable by counting the characters in it
print(response.text[:500])# this prints a slice of the first characters
response.raise_for_status()#this checks the http status to see if the dl was successful

#this next line of cosde shows the 404 error in the output because we used the raise for status method on a non exitstant web page
"""badResponse = requests.get('https://automatetheboringstuff.com/soijfefposahj')
badResponse.raise_for_status()"""

playFile = open('RomeoAndJuliet.txt','wb')
for chunk in response.iter_content(1000000):
    playFile.write(chunk)
playFile.close()