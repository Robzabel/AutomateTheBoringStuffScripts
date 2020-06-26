import re
#This code looks for the names of the secret agents
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave Agent Bob the secret documents.'))
Video Paused at 1:45