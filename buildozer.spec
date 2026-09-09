[app]

title = Al-Hamza Pro
package.name = alhamzapro
package.domain = org.alhamza
version = 1.0

source.dir = .
source.exclude_exts = spec
source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy

orientation = portrait

android.api = 33
android.min_api = 24

android.ndk = 25b
android.ndk_api = 24

android.release_artifact = apk
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
