# smartphonebrainscanner2-craft-blueprints
Craft blueprints and documentation to build windows installers for smartphonebrainscanner apps using craft

# Usage

### Step 1
Fetch the sources and make sure you can build them with for example QtCreator

### Step 2
Set up Craft as described on
https://community.kde.org/Craft

Optionally set it up to use the QtSDK rather than building own Qt.

### Step 3
Add the blueprints repository to craft

```
craft --add-blueprint-repository https://github.com/...../smartphonebrainscanner2-craft-blueprints.git
```

### Step 4
Prepare Craft for creating the package

```
craft --install-deps sbs2-eegviewer
```

### Step 5
Build, install and package sbs2 from the sources you checked out in step 1.

```
craft --src-dir C:\SOMEPATH\smartphonebrainscanner2-DataCollector\ --compile --install --package sbs2
```

NOTES:
Due to the way the SmartphoneBrainScanner sources are setup with different repositories, and external code, step 4 and 5 are needed as
separate steps. For other setups, a blueprint can be written that is handling those in one.
