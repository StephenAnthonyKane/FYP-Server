import datetime

class FileLogger:
    def Error(self, error):
        errorLog = open('/home/skane/www/ErrorLog.txt','a+')
        time = datetime.datetime.now()
        errorMessage = '[' + time.strftime("%X") + ']' + str(error) + '\n'
        errorLog.write(errorMessage)
        errorLog.close()

    def Info(self, message):
        infolog = open('/home/skane/www/InfoLog.txt','a+')
        time = datetime.datetime.now()
        logMessage = '[' + time.strftime("%X") + ']' + str(message) + '\n'
        #print(logMessage)
        infolog.write(logMessage)
        infolog.close()