import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#create a buggy factorial programme
logging.disable(logging.CRITICAL)
logging.debug('start of program')
def factorial (n):
    logging.debug('start of factorial(%s)' % (n))
    total = 1
    for i in range (1,n + 1):
        total *=i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return(total)

print(factorial(5))
logging.debug('end of program')

#to send loggs to a file instead
logging.basicConfig(filename='/home/zabex/Documents/Logging_debug_messages.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
