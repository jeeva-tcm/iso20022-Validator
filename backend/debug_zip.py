import zipfile
import os

zip_path = r'c:\Users\HP\Desktop\iso20022 Validator\backend\xsds\pacs.zip'
out_file = r'c:\Users\HP\Desktop\iso20022 Validator\backend\zip_contents.txt'
with open(out_file, 'w') as f:
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zf:
            for name in zf.namelist():
                f.write(name + '\n')
    else:
        f.write("ZIP not found")
