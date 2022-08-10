from dotenv import load_dotenv
import os
import logging

load_dotenv()
API_KEY = os.getenv('API_KEY')

DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
OUTPUT_DIR = 'output'

#logger
FORMAT = '%(asctime)s: %(name)s: %(message)s'
logging.basicConfig(format=FORMAT)

logger_file = logging.getLogger(__name__)
filehandler = logging.FileHandler(filename='logger')
logger_file.addHandler(filehandler)

stream_handler = logging.StreamHandler()
logger_output = logging.getLogger(__name__)
stream_handler.setLevel(level='DEBUG')
logger_output.addHandler(stream_handler)
logger_output.setLevel(level='DEBUG')