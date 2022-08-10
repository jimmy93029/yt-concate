import os
from yt_concate.settings import DOWNLOADS_DIR, VIDEOS_DIR, CAPTIONS_DIR, OUTPUT_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def create_dirs():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    @staticmethod
    def get_video_list_filepath(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def caption_file_exists(yt):
        filepath = yt.get_caption_filepath()
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    @staticmethod
    def video_file_exists(yt):
        filepath = yt.get_video_filepath()
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    @staticmethod
    def get_output_filepath(channel_name, terms):
        file_name = channel_name + '_' + terms
        return os.path.join(OUTPUT_DIR, file_name + '.mp4')

# #logger
# FORMAT = '%(asctime)s: %(name)s: %(message)s'
# logging.basicConfig(format=FORMAT)
#
# logger_file = logging.getLogger(__name__)
# filehandler = logging.FileHandler(filename=DOWNLOADS_DIR + 'logger')
# logger_file.addHandler(filehandler)
#
# stream_handler = logging.StreamHandler()
# ogger_output = logging.getLogger(__name__)
# logger_output.addHandler(stream_handler)
# stream_handler.setLevel(level='DEBUG')
# logger_output.setLevel(level='DEBUG')