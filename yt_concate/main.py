from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.utils import Utils

channel_id = 'UCTOoRgpHTjAQPk6Ak70u-pA'


def main():
    inputs = {
        'channel_id': channel_id
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight()
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.pipeline(inputs, utils)


if __name__ == '__main__':
    main()
