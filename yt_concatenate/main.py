from yt_concatenate.pipeline.setps.get_video_list import GetVideoList
from yt_concatenate.pipeline.setps.download_captions import DownloadCaptions
from yt_concatenate.pipeline.setps.step import StepException
from yt_concatenate.pipeline.setps.preflight import Preflight
from yt_concatenate.pipeline.setps.postflight import Postflight
from yt_concatenate.utilities import Utils


from yt_concatenate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCXmfS5whB0JOyDCqtDgcytA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    stepsList = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(stepsList)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
