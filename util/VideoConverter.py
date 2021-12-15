import os
import subprocess

from parsers.PathParser import PathParser


class VideoConverter:

    def __init__(self, oldVideoPath: str, newVideoPath: str, **kwargs):
        # note that the paths here include the file name at the end
        self.__oldVideoPath = oldVideoPath
        self.__newVideoPath = newVideoPath
        # log levels for ffmpeg listed here:
        # https://ffmpeg.org/ffmpeg.html#:~:text=loglevel%20is%20a%20string%20or%20a%20number%20containing%20one%20of%20the%20following%20values%3A
        self.__logLevel = kwargs.pop("logLevel", "error")

    def convert(self):
        print(
            f"CONVERTING '{PathParser.getFileNameFromPath(self.__oldVideoPath)}' FROM '{PathParser.getFileExtensionFromPath(self.__oldVideoPath)}' -> '{PathParser.getFileExtensionFromPath(self.__newVideoPath)}'")
        self.__createNewDirectoryIfNonExistent()
        if os.path.exists(self.__newVideoPath):
            print("CONVERTED FILE EXISTS! SKIPPING CONVERSION.")
        else:
            subprocess.run(
                f"""ffmpeg -i "{self.__oldVideoPath}" -vcodec h264 -acodec aac "{self.__newVideoPath}" -loglevel {self.__logLevel}""",
                shell=True,
                stdout=subprocess.DEVNULL)
            print("FINISHED CONVERTING")

    def __createNewDirectoryIfNonExistent(self):
        # creates the directory in self.__oldVideoPath if it doesn't already exist
        newDirectory = PathParser.getPathWithoutFileName(self.__newVideoPath)
        if not os.path.exists(newDirectory):
            # Create a new directory because it does not exist
            os.makedirs(newDirectory)
