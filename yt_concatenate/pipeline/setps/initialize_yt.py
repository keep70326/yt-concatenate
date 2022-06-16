from .step import Step
from yt_concatenate.model.yt import YT

class InitizlizeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]
