import module
import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

a=api.dataset_download_files('carlmcbrideellis/llm-7-prompt-training-dataset')
# os.system("unzip -v C:/Users/gksxo/Desktop/2023학년도 2학기/오픈소스-조겨리 교수님/기말프로젝트/llm-7-prompt-training-dataset.zip")

import zipfile

zip_path = 'C:/Users/gksxo/Desktop/2023학년도 2학기/오픈소스-조겨리 교수님/기말프로젝트/llm-7-prompt-training-dataset.zip'  # 압축 파일 경로
extract_path = 'C:/Users/gksxo/Desktop/2023학년도 2학기/오픈소스-조겨리 교수님/기말프로젝트'  # 압축 해제 경로

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
