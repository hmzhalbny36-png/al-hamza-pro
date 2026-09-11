[app]

# (str) Title of your application
title = Al-Hamza Pro

# (str) Package name
package.name = alhamzapro

# (str) Package domain (needed for android packaging)
package.domain = org.alhamza

# (str) Source directory where the main file is located
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it empty to exclude nothing)
source.exclude_exts = spec

# (list) List of inclusion/exclusion patterns
source.exclude_patterns = license, images/*.jpg

# (string) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) The Android specific API to use
android.api = 31

# (list) Minimum API your APK will support
android.minapi = 21

# (bool) Indicate whether the application should be full screen or not
fullscreen = 0

# (string) Presign build target (default is debug)
android.presign = True
