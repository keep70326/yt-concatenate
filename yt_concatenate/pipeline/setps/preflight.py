from yt_concatenate.pipeline.setps.step import Step

class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in Preflight')
        utils.create_dirs()