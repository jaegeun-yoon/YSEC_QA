import zipfile


# download
url = 'https://drive.google.com/file/d/1lD_1Os0zLCqK-rxJk6bN9C1aa3MOxTpT/view?usp=share_link'



# unpacking
path_to_zip_file = '/Users/' + os.getenv('USER') + '/Downloads/Rooting_apk.zip' # 압축파일 경로
directory_to_extract_to = '/Users/' + os.getenv('USER') + '/dev/Rooting_apk' # 압축 풀고 저장할 경로

with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)