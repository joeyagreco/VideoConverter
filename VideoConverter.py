import subprocess


class VideoConverter:

    def __init__(self, oldVideoPath: str, newVideoPath: str, **kwargs):
        self.__oldVideoPath = oldVideoPath
        self.__newVideoPath = newVideoPath
        # log levels for ffmpeg listed here: https://superuser.com/questions/326629/how-can-i-make-ffmpeg-be-quieter-less-verbose#:~:text=Here%20you%20have%20loglevels%20from%20the%20source%20code%20(FFmpeg%20version%200.10.2.git)
        self.__logLevel = kwargs.pop("logLevel", "error")

    def convert(self):
        print(f"CONVERTING {self.__oldVideoPath} -> {self.__newVideoPath} ...")
        subprocess.run(
            f"ffmpeg -i {self.__oldVideoPath} -vcodec h264 -acodec aac {self.__newVideoPath} -loglevel {self.__logLevel}",
            shell=True,
            stdout=subprocess.DEVNULL)
        print("FINISHED CONVERTING")
