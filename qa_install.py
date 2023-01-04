import zipfile
import gdown
import shutil
import os.path

def setup(url, zip_file):

    gdown.download(url, zip_file, quiet=False)

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('.')

    # delete file
    folder = '__MACOSX'

    try:
        if os.path.isdir(folder) :
            shutil.rmtree(folder)

        if os.path.isfile(zip_file) :
            os.remove(zip_file)

    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

if __name__ == "__main__":
    # total 5m 5sec [28sec(133Mb) + 2min 38sec(658Mb) + 1min 59sec(466Mb)]
    app = {"Rooting_apk.zip":"1lD_1Os0zLCqK-rxJk6bN9C1aa3MOxTpT", "RemoteControler_apk.zip":"1AR1d8QVmm1N5_PJbyrX57n09snzzdDhd", "PalleralCloner_apk.zip":"1xw-B_5MJvgOJzEsmSsZZP4WuaSB8-gGw"}
    base_url = 'https://drive.google.com/uc?id='

    for zip_file, id in app.items() :
        url = base_url + id
        setup(url, zip_file)