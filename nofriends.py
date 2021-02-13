#!/usr/bin/python3
#!/utf/8in/noFriend
#!/ali/elainous

from    selenium.webdriver  import  Firefox,firefox
from    getpass             import  getpass
from    time                import  sleep
from    re                  import  findall

class Fb(Firefox):
    'login to fb account , getting friends_list & delet it'
    def  __init__(self):
        self.opt = 'none'
        opt = firefox.options.Options()
        #opt.set_headless()                                                             # remove "#" to head window of browser
        Firefox.__init__(self)                                                          # start firefox_driver

    def login(self):
        print('Getting facebook...'.ljust(50),end=': ',flush=1)
        while 'inf':
            try:
                self.get('https://m.facebook.com/login/?ref=dbl&amp;fl&amp;refid=9')                                      # open facebook
                print('Done') ; break
            except:pass
        try:                                                                        # try to login 
            self.find_element_by_name('email').send_keys( input('\t<username> : ')) # write username
            self.find_element_by_name('pass').send_keys(getpass('\t<password> : ')) # write password
            print('Sending Data...')
            self.find_element_by_name('login').click()                              # submit ...
            sleep(5)
            print('Getting friends...')
            self.get('http://m.facebook.com/friends/center/friends')
            assert 'facebook.com/friends/center/friends' in self.current_url        # check if  data are correct                                                         
        except:
            print('Error :  username or password is incorrect !!?')                  # data are not correct
            self.close() ; exit()

    def friends(self):
        # Get friends list (10 by 10)
        while 'inf':
            users_name = findall('<a class="darkTouch" href="/(.+?)">',self.page_source)
            if  not users_name:
                print(' :: All friends are removed ::')
                break
            for username in users_name:
                # with    id : http://m.facebook.com/profile.php?id=100022716066422
                # without id : http://m.facebook.com/profeso.ali
                if  'id=' not in username:
                    self.get('http://m.facebook.com/'+username)
                    # get id from here (profile picture)
                    # photo.php?fbid=837369957030199&id=100022716066422&set=a.104580083642527&source=11
                    friend_id = findall('href="/photo.php\?fbid=\d+.....id=(\d+)' , self.page_source)[0]
                else:
                    friend_id = findall('id=(\d+)',username)[0]
                self.remove(friend_id)
            self.get('http://m.facebook.com/friends/center/friends')

    def remove(self,friend_id):
        while 'inf':
            try:
                self.get('http://m.facebook.com/removefriend.php?friend_id={}'.format(friend_id))
                # <a class="_4kk6" href="/rida.mihouk.09">Rida Chikamaro</a>
                friend_username,friend_name = findall('class="_4kk6" href="/(.+?)">(.+?)</a>',self.page_source)[0]
                if  self.opt == 'none':
                    self.opt = input('\n\t[ + ] Are you sure you want to remove all you friends [Y/N] ?')
                    if  'y' in self.opt.lower():
                        self.opt = 'true'
                    else:
                        print('Exiting the process...')
                        return self.close()
                print('[ ?? ] : Removing {} '.format(friend_name.ljust(24)),end='\r')
                self.find_element_by_name('confirm').click()
                
                sleep(2)
                print('[ OK ]') ; break
            except Exception as err:
                print('[ NO ]')
                print('err : ',err)

def main():
    try:
        fb = Fb()
        fb.login()
        fb.friends()
        print('Exiting...')
        fb.close()
    except:pass

#####################################################
#                                                   #
#   Script for delet all your facebook friends.     #
#                                                   #
#   by :   aLi_eLainous                             #
#                                                   #
#####################################################

if  __name__ == '__main__':
    main()
