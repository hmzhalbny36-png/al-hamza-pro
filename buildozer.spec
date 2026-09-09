[app]

# (str) Title of your application
title = Al-Hamza Pro

# (str) Package name
package.name = alhamzapro

# (str) Package domain (needed for android packaging)
package.domain = org.alhamza

# (str) Application versioning (THIS WAS MISSING)
version = 1.0

# (str) Source files where the *.py files are located
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of exclusions
source.exclude_exts = spec

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

#
# Android specific
#

# (int) Target Android API, should be as high as possible
android.api = 34

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Enable Android auto-backup (Android API >=23)
android.autopermissions = True
