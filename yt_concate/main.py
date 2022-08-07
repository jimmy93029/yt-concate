from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYt
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.readcaptions import ReadCaptions
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.utils import Utils

channel_id = 'UCTOoRgpHTjAQPk6Ak70u-pA'
terms = 'taiwan'


def main():
    inputs = {
        'channel_id': channel_id,
        'terms': terms
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYt(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.pipeline(inputs, utils)


if __name__ == '__main__':
    main()
