import zipfile
import os
from datetime import datetime


with zipfile.ZipFile('file.zip', 'r') as zip_ref:
    for info in zip_ref.infolist():
        print(f"{info.filename}; {info.file_size}; {info.is_dir()}; ")


