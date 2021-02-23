#!/usr/bin/python3
#!/utf/8in/systems.py

from os import system

def check(val,rng):
    var1 , var2 =  (val+'.').split('.')[:2]
    if  [ _ for _ in val if _ not in rng ]:
        quit('Err !!!')
    return var1,var2

def bin_to(val,md,_from=2,rng='0.1'):
    var1, var2  = check(val,rng) ; total = '' ; dt = {8:3,16:4}
    Hx={
    	'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15',
     'a':'10','b':'11','c':'12','d':'13','e':'14','f':'15'
     }
    if md in dt:
        _ =  dt[md]
        var1 = '0'*(_-len(var1)%_)+var1 if len(var1)%_ != 0 else var1
        var2 = var2+'0'*(_-len(var2)%_) if len(var2)%_ != 0 else var2
        _8   = {
        	'000':'0', '001':'1','010':'2', '011':'3', '100':'4', '101':'5', '110':'6', '111':'7'}
        _16  = {
        	'0000':'0', '0001':'1','0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7',
        '1000':'8', '1001':'9','1010':'A', '1011':'B', '1100':'C', '1101':'D', '1110':'E', '1111':'F'
        }
        for var in (var1,var2):
            count  =0 ;  new =''
            while  count < len(var): new += locals()['_'+str(md)][var[count:count+_]] ; count += _
            total  +=    new+'.'
        cut = 1    if    var2   else 2 ;return (total[:-1*cut])
    else:
        c = 0 ; _ = 1
        for var in   (var1[::-1],var2):
            cc  = 0  ;new = 0
            while    cc  < len(var):
                v = Hx[var[cc]] if var[cc] in Hx else var[cc]
                new  +=  int(v)*(_from**(_*(c+cc))) ; cc += 1 
            total    +=  str(new)[:]+'.' ;  c += 1 ; _ = -1
        return total.replace('.0.','.')[:-1]

def dec_to(val,md):
    var1,var2 = check(val,'0.123456789')
    new1 , new2 = '' if var1 != '0' else '0' ,  '' if var2 != '0' else '0'
    dt = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    while 1:
        if int(var1) == 0 :   break
        _  = str(int(var1)%md)
        new1 += dt[_] if ( _ in dt )  else _                    ;  var1 = int(var1)/md
    old = float('0.'+var2)*md
    while 1:
        n  , var2 = str(float('0.'+var2)*md).split('.');  new2 += dt[n] if (n in dt) else n
        if float('0.'+var2)*md == old or len(new2) == 16        :  break
    for i,j in enumerate(new2[::-1]):
        if j != '0'    :new2=new2[::-1][i:];break
    total  = new1[::-1]+'.'+new2[::-1] if new2 != '0' else new1[::-1] ;  return total

def h_o_to(val,md,bs=16,rng='0.123456789ABCDEFabcdef'):
    var1,var2 = check(val,rng)
    _dec = bin_to(val,10,bs,rng) # bs=8 : oct_to_dec , bs=16 : hex_to_dec .
    if md==10:return _dec
    else:     return dec_to(_dec,md)

def main():
    system('clear') ; _ = '0.1234567'
    dt = {  'ia':8 , 'ib':2 , 'ic':2 , 'id':2,
            'ja':10, 'jb':10, 'jc':8 , 'jd':8,
            'ka':16, 'kb':16, 'kc':16, 'kd':10 }
    print(''':: Conversion between counting systems (binary,octal,decimal & hexadecimal). ::
    ___________________________________________
   |\__p||   a    |   b    |   c     |   d     |
   |n__\||-_-_-_-_|-_-_-_-_|-_-_-_-_-|-_-_-_-_-|
   |    ||        |        |         |         |
   | i  || 2 -> 8 | 8 -> 2 | 10 -> 2 | 16 -> 2 |
   |____||________|________|_________|_________|
   |    ||        |        |         |         |
   | j  || 2 -> 10| 8 -> 10| 10 -> 8 | 16 -> 8 |
   |____||________|________|_________|_________|
   |    ||        |        |         |         |
   | k  || 2 -> 16| 8 -> 16| 10 -> 16| 16 -> 10|
   |____||________|________|_________|_________|

    Ex: [np=pn:?], (jd=dj:16->8), (ka:2->16), (bj:8->10)''')

    while 1:
        ch = input('\nmode: ')
        if not (ch in dt or ch[::-1] in dt)  :return
        try:    md =  dt[ch]
        except: md =  dt[ch[::-1]]
        if     'a' in ch:
            print('\033[7m',bin_to(input('[2_to_' +str(md)+'] (2: ' ),md)    ,'\033[0m')
        elif   'b' in ch:
            print('\033[7m',h_o_to(input('[8_to_' +str(md)+'] (8: ' ),md,8,_),'\033[0m')
        elif   'c' in ch:
            print('\033[7m',dec_to(input('[10_to_'+str(md)+'] (10: '),md)    ,'\033[0m')
        elif   'd' in ch :
            print('\033[7m',h_o_to(input('[16_to_'+str(md)+'] (16: '),md)    ,'\033[0m')

if __name__ == '__main__':main()

#
# By: __aLi_eLainous__ ;
#
