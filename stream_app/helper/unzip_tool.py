import os
import zipfile

def uzip(path):
        path_to_data = path

        if not zipfile.is_zipfile(f"RC/tests/file_to_test/{path_to_data}"):
                    raise FileNotFoundError("Please upload a zip file noting else")
        else :
                
            
            file_name = path_to_data.split("/")[-1].split('.')[0]
            with zipfile.ZipFile(f"RC/tests/file_to_test/{path_to_data}", 'r') as zip_ref:
                zip_ref.extractall(f"RC/tests/file_to_test/unziped/{file_name}")

            
            current_file = os.listdir(f"RC/tests/file_to_test/unziped/{file_name}")

            new_path = f"RC/tests/file_to_test/unziped/{file_name}"
            for fi in current_file :
                if os.path.isdir(f"{new_path}/{fi}") :#file_name/nouveoux dossier
                    list_all_dir = os.listdir(f"{new_path}/{fi}")
                    for contenu in list_all_dir:
                        file_name2 = contenu.split(".zip")[0]
                        if contenu.endswith(".zip"):
                            with zipfile.ZipFile(f"{new_path}/{fi}/{contenu}", 'r') as zip_ref:
                                zip_ref.extractall(f"{new_path}/{file_name2}")
                elif fi.endswith(".zip"):
                            file_name3 = fi.split(".zip")[0]
                            with zipfile.ZipFile(f"{new_path}/{fi}", 'r') as zip_ref:
                                zip_ref.extractall(f"{new_path}/{file_name3}") 

        print('file unziped')
        return f"/home/aymen/SEF/RC/tests/file_to_test/unziped/{file_name}"

def main():
      uzip()


if __name__ == "__main__":
    main()
