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
