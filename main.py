import json
import subprocess
import time

with open('contacts.json') as json_file:
    contacts = json.load(json_file)

subprocess.run(['adb', 'shell', 'am', 'force-stop', 'com.android.contacts'])

i=0
for contact in contacts:
    print(i)
    i+=1
    # subprocess.run(['adb', 'shell', 'am', 'force-stop', 'com.android.contacts'])
    time.sleep(1)
    name = contact['name']
    name = name.replace(" ",  "_")
    name += "_RVU_neural_nexus"
    number = contact['number']
    # subprocess.run(['adb', 'shell', 'am', 'start', '-a',
    # 'android.intent.action.INSERT', '-t',
    # 'vnd.android.cursor.dir/contact', '-e',
    # 'name', name, '-e', 'phone', number])

    email = contact['email']
    subprocess.run(['adb', 'shell', 'am', 'start',
                    '-a','android.intent.action.INSERT',
                    '-t','vnd.android.cursor.dir/contact',
                    '-e','name', name, '-e', 'phone', number, '-e', 'email', email])
    time.sleep(1)
    # subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_MENU'])  # Open the options menu
    # subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_DPAD_DOWN'])  # Navigate to the "Save" option
    subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENTER'])  # Select the "Save" option
    subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_BACK'])  # Go back to the main Contacts screen
    subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENTER'])  # Select the "Save" option
    subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENTER'])  # Select the "Save" option
    subprocess.run(['adb', 'shell', 'input', 'keyevent','KEYCODE_BACK'])  # Go back to the contact creation screen for the next contact
    subprocess.run(['adb', 'shell', 'input', 'keyevent','KEYCODE_BACK'])  # Go back to the contact creation screen for the next contact
    subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENTER'])  # Select the "Save" option
    subprocess.run(['adb', 'shell', 'input', 'keyevent',
                    'KEYCODE_BACK'])  # Go back to the contact creation screen for the next contact
    subprocess.run(['adb', 'shell', 'input', 'keyevent',
                    'KEYCODE_BACK'])  # Go back to the contact creation screen for the next contact
    time.sleep(1)
