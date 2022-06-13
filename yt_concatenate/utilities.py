import os.path

from yt_concatenate.setting import DOWNLOADS_DIR
from yt_concatenate.setting import CAPTIONS_DIR
from yt_concatenate.setting import VIDEOS_DIR



class Utils:
    def __init__(self):
        pass

    @staticmethod
    def get_video_id_from_url(videoLink):
        return videoLink.split('watch?v=')[1]

    def get_caption_filepath(self, videoLink):
        return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(videoLink) + '.txt')

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    def caption_file_exist(self, videoLink):
        path = self.get_caption_filepath(videoLink)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0