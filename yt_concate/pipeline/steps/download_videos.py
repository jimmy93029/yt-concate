from .step import Step
from pytube import YouTube
from ...settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('videos to download= ', yt_set)

        for yt in yt_set:
            print('downloading', yt.url)
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)
