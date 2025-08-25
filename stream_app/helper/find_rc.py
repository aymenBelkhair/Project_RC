import os
import re
import sys

def find_files_with_exact_rc(directory):
    matches = []
    pattern = re.compile(r'(?<![a-zA-Z])RC(?![a-zA-Z])|(Reglement|règlement).*consultation', re.IGNORECASE)  # Regular expression pattern
              
    for root, dirnames, filenames in os.walk(directory):
#         print(root,dirnames,filenames)
        for filename in filenames:
            if pattern.search(filename) and (filename.lower().endswith('.pdf') or filename.lower().endswith('.doc') or filename.lower().endswith('.docx')):
                matches.append(os.path.join(root, filename))

    return matches
        

def RC(path):
    try:
        directory_path = path
    except IndexError:
        print('Please provide a directory path as an argument.')
       

    try:
        files_with_exact_rc = find_files_with_exact_rc(directory_path)
        if not files_with_exact_rc:
            raise FileNotFoundError("RC file doesn't exist in the specified directory.We can't find them, make shure that you had one on yhis directory")
        
        nom_fichier = files_with_exact_rc[0].split('/')[-1].split('.')[0]
        print(f"Found RC file at : {files_with_exact_rc[0]}")
	

    except FileNotFoundError as e:
        print(e)

    return files_with_exact_rc[0],nom_fichier

if __name__ == "__main__":
    	main()
