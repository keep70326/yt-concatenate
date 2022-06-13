import os
from pprint import  pprint
from .step import Step
from yt_concatenate.setting import CAPTIONS_DIR

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {} # key->檔名, value->字幕
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:

                time_line = False
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        caption = line.strip()
                        captions[caption] = time #使用字典的方式儲存資料，把caption當成key，這樣可以直接撈取不需要多寫if判斷
                        time_line = False
            data[caption_file] = captions

        pprint(data)
        return data




