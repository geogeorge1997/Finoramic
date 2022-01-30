import subprocess
import sys
import pkg_resources

# Function which will install all the packages inside the list
def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        # To Check the package got installed or not
        dist = pkg_resources.get_distribution(package)
    except:
        # If there is any error, the uninstalled package will be appended to failedPackages List
        failedPackages.append(package)

# Reading the file
file = open('file.json','r')
fileData =file.readlines()
# The Input JSON data found in Problem Statement had some errors,
# so I am doing some process to get the required dependencies
#
fileProcess=fileData[0].replace('{','')
fileProcess=fileProcess.replace('}','')
fileProcess=fileProcess.replace('Dependencies = ','')
fileProcess=fileProcess.replace(' ','')

# mylist will contain all the dependencies to be installed
mylist=fileProcess.split(',')
mylist.remove('')
mylist.remove('\n')

failedPackages=[]

# Calling the install function to install all the dependencies
for i in mylist:
    try:
        # To check whether the the package is already installed or not
        dist = pkg_resources.get_distribution(i)
    except:
        # If package is not installed previously, it will call the install function to install the required package
        install(i)

# The condition to be used to display the result
if(len(failedPackages) ==0):
    print('success')
else:
    for i in failedPackages:
        print(i)


