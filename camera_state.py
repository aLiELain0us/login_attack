#!/usr/bin/python3
#!/utf/8in/ae_camera
#!/ali/elainous

from    pygame      import  camera,mixer
from    time        import  sleep
from    threading   import  Thread

def alert():
    mixer.init()
    mixer.music.load('alert.wav')   # alert.wav : alert sound
    mixer.music.play()
    sleep(7)                        # alert for 7 seconds
    mixer.quit()

def main():
    camera.init()
    print('scaning cameras...')
    while 'inf':
        for camera_path in camera.list_cameras():
            # camera_path : /dev/video0
            cmr = camera.Camera(camera_path)
            try:
                cmr.start()
                cmr.stop()
            except:
                print('** Alert ** : (camera {} is opend)'.format(camera_path))
                Thread(target=alert).start()
                sleep(1)
        sleep(1)
    camera.quit()

if __name__=='__main__':
    try:
        main()
    except:pass
