import os


class VideoConverter:

    def __init__(self, oldVideoPath: str, newVideoPath: str, **kwargs):
        self.__oldVideoPath = oldVideoPath
        self.__newVideoPath = newVideoPath

    def convert(self):
        print(f"CONVERTING {self.__oldVideoPath} -> {self.__newVideoPath} ...")
        os.system(f"ffmpeg -i {self.__oldVideoPath} -vcodec h264 -acodec aac {self.__newVideoPath}")
        print("FINISHED CONVERTING")
