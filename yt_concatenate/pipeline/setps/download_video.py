from pytube import YouTube

from yt_concatenate.pipeline.setps.step import Step
from yt_concatenate.setting import VIDEOS_DIR

class DownloadVideo(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('video download=', len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'found video existing video file for {url} skipping')
                continue

            print('下載中:', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
            # first 改成 get_highest_resolution()可以下載高畫質影片
        return data

            # yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
            # yt.streams
            # filter(progressive=True, file_extension='mp4')
            # order_by('resolution')
            # desc()
            # first()
            # download()