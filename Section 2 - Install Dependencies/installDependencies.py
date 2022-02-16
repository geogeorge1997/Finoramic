import subprocess
import sys
import pkg_resources
import threading
import multiprocessing

# from datetime import datetime

'''
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
'''    

# Function which is used to install the package in the arg
def install(package,lock):
    try:
        #lock.acquire() 
        #print(package, 'Installation started')
        #lock.release()
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        # To Check the package got installed or not
        dist = pkg_resources.get_distribution(package)
    except Exception as e:
        # If there is any error, the uninstalled package will be appended to failedPackages List
        #lock.acquire() 
        #print(package, 'Installation failed')
        #lock.release()
        failedPackages.append(package)

# Reading the file
file = open('file.json','r')
fileData =file.readlines()
# The Input JSON data found in Problem Statement had some errors,
# so I am doing some process to get the required dependencies
fileProcess=fileData[0].replace('{','')
fileProcess=fileProcess.replace('}','')
fileProcess=fileProcess.replace('Dependencies = ','')
fileProcess=fileProcess.replace(' ','')

# mylist will contain all the dependencies to be installed
mylist=fileProcess.split(',')
mylist.remove('')
mylist.remove('\n')

'''
mylist = ['beautifulsoup4==4.4.1', 'boto==2.48.0', 'bz2file==0.98', 'certifi==2017.7.27.1',
         'chardet==3.0.4', 'gensim==2.3.0', 'html5lib==0.999', 'idna==2.5', 'nltk==3.2.4',
         'numpy==1.13.1', 'pexpect==4.0.1', 'pip==9.0.1','ptyprocess==0.5', 'pyxdg==0.25',
         'reportlab==3.3.0', 'requests==2.18.3', 'scipy==0.19.1', 'setuptools==20.7.0',
         'six==1.10.0', 'smart-open==1.5.3', 'textblob==0.12.0', 'twitter==1.17.1', 'urllib3==1.22']
'''

failedPackages=[]
all_processes = []
numThread = 5

# Calling the install function to install all the dependencies
lock = threading.Lock()

for i in mylist:
    try:
        # To check whether the the package is already installed or not
        dist = pkg_resources.get_distribution(i)     
    except:
        # If package is not installed previously, it will call the install function to install the required package
        while(True):
            if(threading.active_count()<=numThread):
                process = threading.Thread( target=install, args=(i,lock,) )
                process.start()
                all_processes.append(process)
                break

while(True):
    if(threading.active_count()==2):
        break
    
# The condition to be used to display the result
if(len(failedPackages) ==0):
    print('success')
else:
    for i in failedPackages:
        print(i,len(failedPackages))

'''
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
''' 
