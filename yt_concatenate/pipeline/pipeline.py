from .setps.step import StepException

class Pipeline:
    def __init__(self, stepsList):
        self.stepsList = stepsList

    def run(self, inputs, utils):
        data = None
        for step in self.stepsList:
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:
                print('Exception happend :', e)
                break