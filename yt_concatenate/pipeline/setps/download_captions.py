from pytube import YouTube

from yt_concatenate.pipeline.setps.step import Step
from yt_concatenate.pipeline.setps.step import StepException



class DownloadCaptions(Step):
    def process(self, data, inputs, utils):

        for videoLink in data:
            print('downloading caption for', videoLink)
            if utils.caption_file_exist(videoLink):
                print("已存在字幕檔")
                continue


            try:
                source = YouTube(videoLink)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('Error when downloading caption for', videoLink)
                continue
            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_filepath(videoLink), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

