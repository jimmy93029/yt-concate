import logging

from .step import Step


class ReadCaptions(Step):
    def process(self, data, inputs, utils):
        logging.info('in read captions')
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue
            captions = {}
            with open(yt.caption_filepath, 'r', encoding='utf-8') as file:
                time_line = False
                caption = None
                time = None
                for line in file:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        caption = line.strip()
                        captions[caption] = time
                        time_line = False
            yt.captions = captions
        return data



