class SemanticVersion:
    def __init__(self, major, minor, patch):
        version = str(major) + str(minor) + str(patch)
        self.version = 'py'+version

    def __eq__(self, other):
        return self.version == other


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    print(SemanticVersion(3, 7, 0) == py370)

    print(SemanticVersion(3, 7, 1) == py370)


if __name__ == '__main__':
    main()