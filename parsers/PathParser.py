class PathParser:
    __slashes = ["/", "\\"]

    @classmethod
    def __removeSlashesFromString(cls, s: str) -> str:
        for slash in cls.__slashes:
            s = s.replace(slash, "")
        return s

    @classmethod
    def __removeSlashesFromEndOfString(cls, s: str) -> str:
        for i, char in enumerate(reversed(s)):
            if char not in cls.__slashes:
                return s[:-i]

    @classmethod
    def getFileNameFromPath(cls, path: str) -> str:
        """
        'some/path/myFile.txt' -> 'myFile.txt'
        'invalidString' -> None
        """
        fileName = None
        tmpFileName = ""
        for char in reversed(path):
            tmpFileName += char
            if char in cls.__slashes:
                fileName = tmpFileName[::-1]
                break
        return cls.__removeSlashesFromString(fileName)

    @classmethod
    def getPathWithoutFileName(cls, path: str) -> str:
        """
        'some/path/myFile.txt' -> 'some/path'
        'invalidString' -> None
        """
        fileName = None
        for i, char in enumerate(reversed(path)):
            if char in cls.__slashes:
                fileName = path[:-i]
                # remove any trailing slashes
                break
        return cls.__removeSlashesFromEndOfString(fileName)

    @classmethod
    def getFileExtensionFromPath(cls, path: str) -> str:
        """
        'some/path/myFile.txt' -> 'txt'
        'invalidString' -> None
        """
        extension = None
        tmpSections = path.split(".")
        if len(tmpSections) > 1:
            extension = tmpSections[-1]
        return extension

    @classmethod
    def cleanExtension(cls, s: str) -> str:
        """
        '.mp4' -> 'mp4'
        'mp4' -> 'mp4'
        """
        return s.replace(".", "")

    @classmethod
    def isFile(cls, s: str) -> bool:
        """
        'myFile.mp4' -> True
        'test/myFile.mp4' -> True
        'test' -> False
        """
        return s.count(".") > 0

    @classmethod
    def removeFileExtensionFromPath(cls, path: str) -> str:
        """
        'some/path/myFile.txt' -> 'some/path/myFile'
        'some/path' -> 'some/path'
        """
        return path.split(".")[0]
