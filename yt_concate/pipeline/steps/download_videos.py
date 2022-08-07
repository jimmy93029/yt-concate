from .step import Step
from pytube import YouTube
from ...settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('videos to download= ', len(yt_set))

        for yt in yt_set:
            if utils.video_file_exists(yt):
                print('found existing filepath')
                continue
            print('downloading', yt.url)
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
        return data
