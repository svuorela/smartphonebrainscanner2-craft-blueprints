# -*- coding: utf-8 -*-
import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.description = "SmartphoneBrainScanner DataCollector"
        self.displayName = "SmartphoneBrainScanner DataCollector"
        self.svnTargets['master'] = 'git://anongit.kde.org/|master'
        self.defaultTarget = 'master'

    def setDependencies(self):
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = "default"


from Package.Qt5CorePackageBase import *


class Package(Qt5CorePackageBase):
    def __init__(self, **args):
        Qt5CorePackageBase.__init__(self)

    def createPackage(self):
        self.defines["shortcuts"] = [{"name" : self.subinfo.displayName, "target":"bin//sbs2-DataCollector"}]
        self.defines["icon"] = os.path.join(os.path.join(self.sourceDir(), "datacollector.ico"))
        self.defines["company"] = "DTU"
        self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist.txt'))

        return TypePackager.createPackage(self)
