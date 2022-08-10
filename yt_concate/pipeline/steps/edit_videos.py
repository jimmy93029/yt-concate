import logging

from moviepy.video.compositing.concatenate import concatenate_videoclips
from .step import Step
from moviepy.editor import VideoFileClip


class EditVideo(Step):
    def process(self, data, inputs, utils):
        logging.info('in edit videos')
        founds = data
        clips = []
        for found in founds:
            [time_start, time_end] = found.time.replace(',', '.').split('-->')
            video = VideoFileClip(found.yt.video_filepath).subclip(time_start, time_end)
            clips.append(video)
        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_name'], inputs['terms'])
        final_clip.write_videofile(output_filepath)
