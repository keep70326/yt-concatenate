from .step import Step


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue

            captions = {}

            with open(yt.caption_filepath, 'r') as f:
                time_line = False
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        caption = line.strip()
                        captions[caption] = time #使用字典的方式儲存資料，把caption當成key，時間當value，這樣可以直接撈取不需要多寫if判斷
                        time_line = False
            yt.captions = captions

        return data




