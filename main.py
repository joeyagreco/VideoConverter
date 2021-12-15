import os

from parsers.PathParser import PathParser
from util.EnvironmentReader import EnvironmentReader
from util.VideoConverter import VideoConverter

if __name__ == "__main__":
    oldDir = EnvironmentReader.get("DIRECTORY_TO_CONVERT_FROM")
    newDir = EnvironmentReader.get("DIRECTORY_TO_CONVERT_TO")
    oldExt = EnvironmentReader.get("OLD_EXTENSION")
    newExt = EnvironmentReader.get("NEW_EXTENSION")

    # convert all files in old directory
    for file in os.listdir(oldDir):
        # check if this file is the type we want to convert
        if PathParser.isFile(file) \
                and PathParser.getFileExtensionFromPath(file).lower() == PathParser.cleanExtension(oldExt).lower():
            # convert
            vc = VideoConverter(f"{oldDir}\\{file}",
                                f"{newDir}\\{PathParser.removeFileExtensionFromPath(file)}.{PathParser.cleanExtension(newExt)}")
            vc.convert()
