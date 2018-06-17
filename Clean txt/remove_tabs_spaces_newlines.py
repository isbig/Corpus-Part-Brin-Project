import re
import os
import glob

dir_path = os.path.dirname(os.path.realpath(__file__))

for filename in glob.glob(os.path.join(dir_path, '*.txt')):
    print(filename)
    a = os.path.splitext(os.path.basename(filename))[0]
    with open(filename, "r", encoding='utf-8') as f1:                 
        with open(dir_path+"/"+a+"_cut.txt", "w", encoding='utf-8') as f2:
            for line in f1:
                m = re.sub('\s+',' ', line)
                f2.write(m)
        f1.close()
        f2.close()
        
#found how to remove spaces tabs newlines at https://stackoverflow.com/questions/10711116/strip-spaces-tabs-newlines-python
#found How to get the filename without the extension from a path in Python? on https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python
