from yt_concatenate.pipeline.setps.get_video_list import GetVideoList
from yt_concatenate.pipeline.setps.step import StepException

from yt_concatenate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCXmfS5whB0JOyDCqtDgcytA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    stepsList = [
        GetVideoList(),
    ]

    p = Pipeline(stepsList)
    p.run(inputs)


if __name__ == '__main__':
    main()
