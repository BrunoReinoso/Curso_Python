class Log():
    def escreve(msg, status):
        if status == 0:
            cod = 'ERROR: '
        elif status == 1:
            cod = 'INFO: '
        else:
            with open('log.txt', 'a+') as file:
                file.write('INVALID')
                file.write('/n')
            return

        with open('log.txt', 'a+') as file:
            file.write(cod + msg)
            file.write('\n')