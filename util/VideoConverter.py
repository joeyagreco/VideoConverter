import subprocess


class VideoConverter:

    def __init__(self, oldVideoPath: str, newVideoPath: str, **kwargs):
        self.__oldVideoPath = oldVideoPath
        self.__newVideoPath = newVideoPath
        # log levels for ffmpeg listed here:
        # https://ffmpeg.org/ffmpeg.html#:~:text=loglevel%20is%20a%20string%20or%20a%20number%20containing%20one%20of%20the%20following%20values%3A
        self.__logLevel = kwargs.pop("logLevel", "error")

    def convert(self):
        print(f"CONVERTING {self.__oldVideoPath} -> {self.__newVideoPath} ...")
        subprocess.run(
            f"ffmpeg -i {self.__oldVideoPath} -vcodec h264 -acodec aac {self.__newVideoPath} -loglevel {self.__logLevel}",
            shell=True,
            stdout=subprocess.DEVNULL)
        print("FINISHED CONVERTING")
