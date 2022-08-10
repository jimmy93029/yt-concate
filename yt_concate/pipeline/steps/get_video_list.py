import logging
import os
import urllib.request
import json
from yt_concate.settings import API_KEY
from yt_concate.pipeline.steps.step import Step
from threading import Thread
from time import time


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        logging.info('in get video list')
        self.channel_id = inputs['channel_id']
        self.base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        self.url = base_search_url + f'key={API_KEY}&channelId={self.channel_id}&part=snippet,id&order=date&maxResults=25'
        self.video_links = []
        self.utils = utils

        start_time = time()
        threads = []
        # print('my cpu_count have', os.cpu_count(), 'cores')
        for _ in range(12):
            threads.append(Thread(target=self.request_video_url))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        end_time = time()
        logging.info('threads runs', end_time - start_time, 'seconds')

        logging.info(self.video_links)
        self.write_to_file(self.video_links, utils.get_video_list_filepath(self.channel_id))
        return self.video_links

    def request_video_url(self):
        if self.utils.video_list_file_exists(self.channel_id):
            logging.info('Found exiting video list file for channel id', self.channel_id)
            return self.read_file(self.utils.get_video_list_filepath(self.channel_id))
        while len(self.video_links) <= 500:
            inp = urllib.request.urlopen(self.url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    self.video_links.append(self.base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = self.url + f'&pageToken={next_page_token}'

            except KeyError:
                break

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


