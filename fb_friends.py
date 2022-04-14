#!/usr/bin/python
#-*-encoding:utf-8-*-

from    selenium.webdriver  import  Firefox
from    time        import  sleep
from    re          import  findall
from    os          import  listdir

def cin(msg, x=None):
    while not x:
        x = input(msg)
    return x

def login():
    element('//input[@name="email"]').send_keys(cin('username: '))
    element('//input[@name="pass"]').send_keys(cin('password: '))
    print(f'[ .. ] Login', end='\r', flush=1)
    element('//button[@name="login"]').click()
    sleep(10)
    if  findall(r'type="password"', dr.page_source):
        print('[ NO ]\nInvalid username or password.')
        dr.quit()
        exit()
    print('[ OK ]')

def get_friends():
    print(f'Getting friends...')
    get('friends/center/friends')
    last_length = -1
    new_length  = 0
    c = 1
    while last_length != new_length:
        dr.execute_script(f'window.scrollTo(0, {2000 * c})')
        sleep(5)
        last_length = new_length
        friends     = set(findall(r'class="darkTouch".+?href="/(.+?)"', dr.page_source))
        new_length  = len(friends)
        c += 1
    save(friends)
    return friends

def save(friends):
    files    = listdir()
    count    = len(findall(r'fb_friends_\d*\.txt', ''.join(files)))
    filename = 'fb_friends_{}.txt'
    if  filename.format(count) in files:
        count += 1
    open(filename.format(count), 'w').write('\n'.join(friends))
    print(f'saving {len(friends)} friends on {filename}.')

def get(user=''):
    while 'inf':
        try:
            dr.get(f'https://m.facebook.com/{user}')
            return sleep(5)
        except:
            sleep(5)

def element(exp, by='xpath'):
    for _ in range(14):
        try:
            return dr.find_element(by, exp)
        except:
            sleep(3)

def close():
    try:dr.quit()
    except:pass
    quit()

if  __name__ == '__main__':
    message  = 'hello world'
    dr = Firefox()
    print('Getting Facebook...')
    get()
    login()
    opt = input('''
    Get fb_friends :
    1 - from facebook
    2 - from filename
    > ''').strip()
    
    friends = get_friends() if  opt == '1' else open(input('friends_list: '))
    if  'y' not in input('Send message to all friends (y/n) : ').strip():
        close()
    for friend in friends:
        print(f'[ .. ] Send msg to {friend}', end='\r', flush=1)
        get(friend)
        try:
            element('//a[@class="_56by _54k8 _5c9u _5caa"]').click()
            element('//textarea[@id="composerInput"]').send_keys(message)
            element('//button[@name="send"]').click()
            sleep(5)
        except:pass
    close()
