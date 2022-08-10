import logging

from .step import Step
from pytube import YouTube
from ...settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        logging.info('videos to download= ', len(yt_set))

        for yt in yt_set:
            if utils.video_file_exists(yt):
                logging.info('found existing filepath')
                continue
            logging.info('downloading', yt.url)
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
        return data
