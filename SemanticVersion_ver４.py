class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

        self.version = f'py{str(major)}.{str(minor)}.{str(patch)}'

    def patch_version_up(self):
        return f'py{str(self.major)}.{str(self.minor)}.{str(self.patch +1)}'

    def minor_version_up(self):
        return f'py{str(self.major )}.{str(self.minor + 1)}.0'

    def __eq__(self, other):
        return self.version == other

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py380 = py370.minor_version_up()
    print(SemanticVersion(3, 8, 0) == py380)


if __name__ == '__main__':
    main()