from util.EnvironmentReader import EnvironmentReader
from util.VideoConverter import VideoConverter

if __name__ == "__main__":
    oldDir = EnvironmentReader.get("DIRECTORY_TO_CONVERT_FROM")
    newDir = EnvironmentReader.get("DIRECTORY_TO_CONVERT_TO")

    # convert all files in old directory
    # for file in os.listdir(oldDir):
    #     print(file)

    vc = VideoConverter("H:\\Desktop-HDD\\test\\old.mov", "H:\\Desktop-HDD\\test\\new\\new.mp4")
    vc.convert()
