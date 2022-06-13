from yt_concatenate.pipeline.setps.step import Step

class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')
