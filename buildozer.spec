[app]

# (str) Title of your application
title = Al-Hamza Pro

# (str) Package name
package.name = alhamzapro

# (str) Package domain (needed for android packaging)
package.domain = org.alhamza

# (str) Source directory where the application files are located
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android build tools version to use
android.build_tools_version = 33.0.2

# (str) python-for-android branch to use
p4a.branch = master

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0
