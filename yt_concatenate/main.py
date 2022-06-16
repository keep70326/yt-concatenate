from yt_concatenate.pipeline.setps.preflight import Preflight
from yt_concatenate.pipeline.setps.get_video_list import GetVideoList
from yt_concatenate.pipeline.setps.initialize_yt import InitizlizeYT
from yt_concatenate.pipeline.setps.download_captions import DownloadCaptions
from yt_concatenate.pipeline.setps.read_caption import ReadCaption
from yt_concatenate.pipeline.setps.search import Search
from yt_concatenate.pipeline.setps.download_video import DownloadVideo
from yt_concatenate.pipeline.setps.postflight import Postflight
from yt_concatenate.pipeline.setps.step import StepException
from yt_concatenate.pipeline.pipeline import Pipeline
from yt_concatenate.utilities import Utils


CHANNEL_ID = 'UCXmfS5whB0JOyDCqtDgcytA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'game',
    }

    stepsList = [
        Preflight(),
        GetVideoList(),
        InitizlizeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideo(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(stepsList)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
