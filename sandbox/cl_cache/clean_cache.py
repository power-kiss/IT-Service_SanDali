import os
import shutil
import logging

logging.basicConfig(filename='cache_cleaning_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def exception_folder(name_folder):
    return not any(keyword in name_folder.lower() for keyword in ['профиль_пользователя', 'conf'])


def clean_cache(cache_path):
    for root, dirs, files in os.walk(cache_path, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if exception_folder(dir_name):
                logging.info(f'Folder deleted: {dir_path}')
                shutil.rmtree(dir_path)

    logging.info('Cache cleared successfully')

cache_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', '1C', '1cv8')
clean_cache(cache_path)

cache_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', '1C', '1cv8')
clean_cache(cache_path)