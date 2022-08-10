from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYt
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.readcaptions import ReadCaptions
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_videos import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.utils import Utils
import sys
import getopt


def main():
    inputs = {
        'channel_name': 'CNN10',
        'channel_id': 'UCTOoRgpHTjAQPk6Ak70u-pA',
        'terms': 'taiwan'
    }

    short_opts = 'hc:t:'
    long_opts = 'help channel_id= terms'.split()
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print('ytconcate.py -c <channel_id> -t <terms>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('ytconcate.py -c <channel_id> -t <terms>')
            sys.exit()
        elif opt in ("-c", "--channel_id"):
            inputs['channel_id'] = arg
        elif opt in ("-t", "--terms"):
            inputs['terms'] = arg
    print('channel_id is :', inputs['channel_id'])
    print('terms is :', inputs['terms'])

    steps = [
        Preflight(),
        # GetVideoList(),
        # InitializeYt(),
        # DownloadCaptions(),
        # ReadCaptions(),
        # Search(),
        # DownloadVideos(),
        # EditVideo(),
        # Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.pipeline(inputs, utils)


if __name__ == '__main__':
    main()
