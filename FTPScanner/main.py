import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+] ' +str(hostname) + ' FTP Anonymous Login DADDY IS BABY!! ')
        return True
    except Exception:
        print('\n [-] ' +str(hostname) + 'FTP Anonymous Login FAILED Sorry DADDY.')
        return False 
    

if __name__ == '__main__':
    anonLogin('90.130.70.73')