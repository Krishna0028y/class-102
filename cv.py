from os import access
import cv2;
import time;
import random;
import dropbox;

start_time = time.time()

def take_snapshot():
    no = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        img_name ="img"+str(no)+"png"
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite("NewPicture1.jpg",frame)
        result = False
    return img_name
    print("snapshot taken")


    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

def upload_files(img_name):
    access_token = 'sl.BJIjrQYcA_qY7n87W6kMQJtcFX-2IMi2IQ2FfaXyBzO16mLGlgbLyGrz_vWNjLd6Q4UO7jC2NpiWoX9UymLbrxTrQX62I0vIO3hvUFV_nOgxz0cjfWuviNS_9PCwJMUXwAJGAd0'
    file = img_name
    file_from = file
    file_to ="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_files(name)


main()                                                                            
