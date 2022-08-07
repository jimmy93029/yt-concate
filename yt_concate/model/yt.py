import os
from yt_concate.settings import CAPTIONS_DIR, VIDEOS_DIR


class Yt:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_filepath()
        self.captions = None

    @staticmethod
    def get_video_id_from_url(url):
        video_id = url.split('watch?')[-1]
        return video_id

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.id + 'txt')  # 應該是' .txt' 要加上點

    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')

    def __str__(self):
        return self.url

    def __repr__(self):
        content = ';'.join([
            'url: ' + str(self.url),
            'caption: ' + str(self.caption_filepath)
        ])
        return '<Found(', content, ')>'
