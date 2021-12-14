class VideoConverter:

    def __init__(self, oldVideoPath: str, newVideoPath: str, newMediaType: str, **kwargs):
        self.__oldVideoPath = oldVideoPath
        self.__newVideoPath = newVideoPath
        self.__newMediaType = newMediaType

