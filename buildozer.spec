[app]

# (str) Title of your application
title = Al-Hamza Pro

# (str) Package name
package.name = alhamzapro

# (str) Package domain (needed for android packaging)
package.domain = org.alhamza

# (str) Application versioning
version = 1.0

# (list) Source files to include (let it empty to include all the files)
source.dir = .

# (list) Source files to exclude (let it empty to exclude none)
source.exclude_exts = spec

# (list) List of inclusions
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) List of permissions
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android API version to use for NDK
android.ndk_api = 21

# (str) The format used to package the app for release
android.release_artifact = apk

# (str) The format used to package the app for debug
android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
