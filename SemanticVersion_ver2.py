class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

        version = str(major) + str(minor) + str(patch)
        self.version = 'py'+version

    def __eq__(self, other):
        return self.version == other

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    print('3.7.0' == str(py370))


if __name__ == '__main__':
    main()