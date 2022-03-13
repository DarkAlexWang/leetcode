from enum import Enum

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    EXTRALARGE = 4

class Package:
    count = 0
    def __init__(self, package_size):
        Package.count += 1
        self.package_id = Package.count
        self.package_size = package_size

    def get_package_size(self):
        return self.package_size

class PackageFactory:
    @staticmethod
    def create(package_size):
        if not isinstance(package_size, Size):
            raise ValueError(package_size)
        return Package(package_size)

class Locker:
    count = 0
    def __init__(self, locker_size):
        Locker.count += 1
        self.locker_id = Locker.count
        self.locker_size = locker_size
        self.vacancy_status = True

    def set_vacancy_status(self, new_status):
        self.vacancy_status = new_status

    def get_vacancy_status(self):
        return self.vacancy_status

    def get_locker_size(self):
        return self.locker_size

    def get_locker_id(self):
        return self.locker_id


class LockerFactory:
    @staticmethod
    def create(locker_size):
        if not isinstance(locker_size, Size):
            raise ValueError(locker_size)
        return Locker(locker_size)


class LockerManager:
    def __init__(self, lockers = []):
        self.lockers = lockers
        self.locker_map = {}

    def get_lockers(self):
        return self.lockers


    def add_lockers(self, new_lockers):
        if any(not isinstance(l, Locker) for l in new_lockers):
            raise ValueError(new_lockers)
        self.lockers.extend(new_lockers)

    @staticmethod
    def match_sizes(locker, package):
        locker_size = locker.get_locker_size().value
        package_size = package.get_package_size().value
        return locker_size >= package_size

    def occupy_locker(self, package):
        if not isinstance(package, Package):
            raise ValueError(package)
        for locker in self.get_lockers():
            if locker.get_vacancy_status():
                match = LockerManager.match_sizes(locker, package)
                if not match: continue
                locker_id = locker.get_locker_id()
                self.locker_map[locker_id] = package
                locker.set_vacancy_status(False)
                return (locker_id, True)
        return (-1, False)

    def extract_package_from_locker(self, locker_id):
        for locker in self.get_lockers():
            if locker_id in self.locker_map and locker_id == locker.get_locker_id():
                locker.set_vacancy_status(True)
                stored_package = self.locker_map[locker_id]
                return stored_package
        return None

small_locker = LockerFactory.create(Size.SMALL)
medium_locker = LockerFactory.create(Size.MEDIUM)
large_locker = LockerFactory.create(Size.LARGE)


lm = LockerManager()
lm.add_lockers([small_locker, medium_locker, large_locker])

p1 = PackageFactory.create(Size.LARGE)
p2 = PackageFactory.create(Size.LARGE)
p3 = PackageFactory.create(Size.LARGE)
p4 = PackageFactory.create(Size.LARGE)

print(lm.extract_package_from_locker(large_locker.get_locker_id()))
#None

packages = [p1, p2, p3, p4]
for i,p in enumerate(packages):
    print(i, lm.occupy_locker(p))
    """
    (0, (3, True))
    (1, (-1, False))
    (2, (-1, False))
    (3, (-1, False))
    """

print(lm.extract_package_from_locker(large_locker.get_locker_id()))
#<__main__.Package instance at 0x7f067d3e1280>
