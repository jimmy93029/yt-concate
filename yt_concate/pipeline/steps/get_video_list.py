import urllib.request
import json
from yt_concate.settings import API_KEY
from yt_concate.pipeline.steps.step import Step


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        print('in get video list')
        channel_id = inputs['channel_id']

        if utils.video_list_file_exists(channel_id=channel_id):
            print('Found exiting video list file for channel id', channel_id)
            return self.read_file(utils.get_video_list_filepath(channel_id))

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        url = base_search_url + f'key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

        video_links = []
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = url + f'&pageToken={next_page_token}'

            except KeyError:
                break
        print(video_links)
        self.write_to_file(video_links, utils.get_video_list_filepath(channel_id))
        return video_links

    def write_to_file(self, video_links, filepath):
        with open(filepath, 'w') as file:
            for url in video_links:
                file.write(url + '\n')

    def read_file(self, filepath):
        video_links = []
        with open(filepath, 'r') as file:
            for url in file:
                video_links.append(url.strip())
            return video_links
