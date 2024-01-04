import zipfile
import os

def extract_file(path_to_file):
    with zipfile.ZipFile(path_to_file, 'r') as zip_ref:
        #create folder with same name as unzipped folder
        os.mkdir(os.path.splitext(path_to_file)[0])
        zip_ref.extractall(os.path.splitext(path_to_file)[0])

def zip_file(path_to_file):
    with zipfile.ZipFile(''+os.path.splitext(path_to_file)[0] + '.zip', 'w', zipfile.ZIP_DEFLATED) as ziph:
    # ziph is zipfile handle
        for root, dirs, files in os.walk(path_to_file):
            for file in files:
                ziph.write(os.path.join(root, file), 
                           os.path.relpath(os.path.join(root, file), 
                                           os.path.join(path_to_file, '..')))

if __name__ == "__main__":
    print("Type 1 to extract or 2 to zip file: ")
    action = input()
    print("Type path of file: ")
    path = input()
    if action == '1':
        extract_file(path)
    if action == '2':
        zip_file(path)
    