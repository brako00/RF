import os
import pandas as pd
import hashlib
import magic
import mimetypes

# specify the directory path where the files are located
dir_path = 'C://Users//A508//brako//lab2//dokazi'

# create an empty list to store the file names
file_names = []
extensions = []
md5s = []
sha1s = []
sha256s = []
magic_numbers = []
extension_matches = []

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
                   'magic_numbers:': magic_numbers, 'extension_matches:': extension_matches})


# print the dataframe
print(df)