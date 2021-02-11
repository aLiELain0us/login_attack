#!/usr/bin/python3
#!/utf/8in/netstat

from    os      import  system, popen
from    sys     import  argv
from    time    import  sleep, time
from    psutil  import  net_connections, WINDOWS
from    socket  import  socket, gethostname, gethostbyname, gethostbyaddr, getservbyport

def tab(var,length=0):
    return str(var).rjust(int(length)) if str(var).isdigit() or var=='.' else str(var).ljust(int(length))

def info(ip,port):
    try:    host = gethostbyaddr(ip)
    except: host = '.....',''
    try:    serv = getservbyport(port)
    except: serv = '..'
    return  host[0],serv

def main():
    monitored_ports = argv[1:]
    t0=0
    while 'inf':
        system('cls' if WINDOWS else 'clear')
        print('\033[33m',end='')
        print(tab('PID',5),tab('LIP',17),tab('LHOST',25),tab('LPORT/SERV',19),tab('RIP',17),tab('RHOST',50),tab('RPORT/SERV',19),tab('STATUS',12))
        print('\033[36m',end='')
        print(tab('====='),tab('='*17,17),tab('='*25,25),tab('='*19,19),tab('='*17,17),tab('='*50,50),tab('='*19,19),tab('='*6,12))
        print('\033[0m',end='')
        for conn in net_connections():

            lip,lport = conn.laddr
            status = conn.status
            pid= '.' if conn.pid!='None' else conn.pid
            rip,rport = ('...','.') if not conn.raddr else conn.raddr
            lhost,lserv = info(lip,lport)
            rhost,rserv = info(rip,rport)
            
            if str(rport) in monitored_ports and int(time()-t0)>=180:
                # ------------------------------------------------
                popen('python3 attacker.py '+rip+' '+str(rport)) #----------- run attacker.py
                popen('python3 alert.py')                        #----------- run alert.py .
                # ------------------------------------------------
                t0=time()
            print(tab(pid,5)+' '+tab(lip,17)+' '+tab(lhost,25)+' '+tab(lport,5)+' '+tab(lserv,13)+' '+tab(rip,17)+' '+tab(rhost,50)+' '+tab(rport,5)+' '+tab(rserv,13)+' '+tab(status,12))
        sleep(2)

if __name__=='__main__':
    try:main()
    except Exception as e:print(e);pass

