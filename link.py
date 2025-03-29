#import webbrowser

#web = "https://www.cisco.com/"
#webbrowser.open(web)


#import os

#ip = ''

#video_vrl = 'https://www.youtube.com/watch?v=5xel-DBdpl0&t=279s'

#packace_NAME = 'com.google.android.youtube.tv'
#ac = 




import os

# عنوان IP الخاص بالجهاز المستهدف داخل الشبكة
DEVICE_IP = "192.168.178.91"
YOUTUBE_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
PACKAGE_NAME = "com.google.android.youtube"
ACTIVITY_NAME = "com.google.android.youtube.Activity,ShellActivity"



adb_command = f"adb -s {DEVICE_IP}:5555 shell am start -n {PACKAGE_NAME}/{ACTIVITY_NAME} -a android.intent.action.VIEW -d \"{YOUTUBE_URL}\""


os.system(adb_command)
