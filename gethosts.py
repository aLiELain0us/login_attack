#!/usr/bin/python3
#!/utf/8in/gethosts
#!/ali/elainous

from    threading   import  Thread
from    socket      import  socket
from    time        import  sleep
from    sys         import  argv

def is_open(ip):
    s = socket()
    s.settimeout(3)
    try:
        print('? ',ip, end='\r', flush='y')
        s.connect((ip, 80))
        return not print(ip+' '*10)
    except Exception as err:
        # ConnectionRefusedError: 111, e.g: ip exist but port not open 
        return not print(ip+' '*10) if  err.args[0] == 111 else None
    s.close()

def is_ip(gateway):
    try:
        lst = list(map(lambda d:(0<=int(d)<=255), gateway.split('.')))
        return gateway if (all(lst) and len(lst) == 4) else ''
    except:
        s = socket()
        try:
            s.connect((gateway,80))
            ip = s.getpeername()[0]
            s.close()
            return ip
        except:
            return s.close()

def main():
    gateway = argv[1] if  len(argv) > 1 else input('NetGateway: ')
    gateway = is_ip(gateway.strip())
    if  not gateway:
        return print('GatewayError: the ip is not correct.')
    i = '.'.join(gateway.split('.')[:-1])
    for p in range(1,256):
        ip = '{}.{}'.format(i,p)
        Thread(target=is_open, args=(ip,)).start()
        sleep(.1)

if  __name__ == '__main__':
    main()
