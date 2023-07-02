
import re
import datetime


log_path = "C:\\Users\\A508\\brako\\lab3\\setupapi.dev.log"
pattern = r'^>>>  \[Device Install.*#(Disk&Ven_[A-Za-z0-9]+)&(Prod_([\w\s\S]+?))&(Rev_([\w\s\S]+?))#([\w\s\S]+?)#.*\]'
usb_devices_list = []

# Read the contents of the setupapi.dev.log file
with open(log_path, "r") as log_file:
     # Store information about each USB device in a dictionary
     for line in log_file:
     # Find all USB device installation events and extract information about each device
        match = re.match(pattern, line)
        if(match):
            # for i in range(0,7):
            #     print(match.group(i))
            #     print("end")
            vendor_id = match.group(1)
            product_id = match.group(2)
            serial_number = match.group(6)
            instance_id = product_id + serial_number
            line = next(log_file)
            event_line = line.split("t")
            event_time = event_line[3]
            usb_devices = {
            "device_vendor_id": vendor_id,
            "device_product_id": product_id,
            "device_instance_id": instance_id,
            "device_serial_number": serial_number,
            "event_time": event_time
            }
            usb_devices_list.append(usb_devices)
for device in usb_devices_list:
    print(device)


import os
import pandas as pd
import hashlib
import magic
import mimetypes
import time

# specify the directory path where the files are located
dir_path = 'E:\\'

# create an empty list to store the file names
file_names = []
extensions = []
md5s = []
sha1s = []
sha256s = []
magic_numbers = []
extension_matches = []
creation_times = []
modification_times = []
access_times = []

magic_object = magic.Magic(mime=True)



# iterate through all files in the directory
for file in os.listdir(dir_path):
    # check if the file is a regular file (i.e., not a directory)
    if os.path.isfile(os.path.join(dir_path, file)):
        # if so, add the file name to the list
        tuple, extension = os.path.splitext(file)
        file_names.append(file)
        extensions.append(extension)

        with open(os.path.join(dir_path, file), 'rb') as f:
            data = f.read()
            md5 = hashlib.md5(data).hexdigest()
            sha1 = hashlib.sha1(data).hexdigest()
            sha256 = hashlib.sha256(data).hexdigest()
            md5s.append(md5)
            sha1s.append(sha1)
            sha256s.append(sha256)
            ctime = time.ctime(os.path.getctime(os.path.join(dir_path, file)))
            mtime = time.ctime(os.path.getmtime(os.path.join(dir_path, file)))
            atime = time.ctime(os.path.getatime(os.path.join(dir_path, file)))
            creation_times.append(ctime)
            modification_times.append(mtime)
            access_times.append(atime)


        mo = magic_object.from_file(os.path.join(dir_path, file))
        magic_numbers.append(mo)

        
        # check if the magic number contains the file extension
        if extension.lower() == '':
            extension_matches.append(False)
        elif mimetypes.guess_type('test'+extension.lower())[0] in mo.lower():
            extension_matches.append(True)
        else:
            extension_matches.append(False)

# create a Pandas dataframe with the file names
df = pd.DataFrame({'file_name': file_names, 'extension_names': extensions
                   , 'md5s': md5s, 'sha1s': sha1s, 'sha256s': sha256s,
                   'magic_numbers:': magic_numbers, 'extension_matches:': extension_matches,
                   'creation_times': creation_times, 'modification_times': modification_times,
                   'access_times': access_times})


# print the dataframe
print(df.head())
