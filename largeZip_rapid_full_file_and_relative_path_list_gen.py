import zipfile
import os
from datetime import datetime


with zipfile.ZipFile('bck_2025_08_22.zip', 'r') as zip_ref:
    for info in zip_ref.infolist():
        print(f"{info.filename}; {os.path.basename(info.filename)}; {os.path.dirname(info.filename)}/; {info.file_size}; {info.is_dir()}; {datetime(*info.date_time).strftime('%Y-%m-%d %H:%M:%S')}")
