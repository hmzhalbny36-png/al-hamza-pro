[app]

title = Al-Hamza Pro
package.name = alhamzapro
package.domain = org.test
version = 0.1
version.code = 1

requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# icon.filename = icon.png

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.minapi = 21
android.sdk = 33
android.gradle_dependencies = ''

# لا تحدد مسار SDK هنا، بل اعتمد على متغير البيئة ANDROID_HOME الذي سيضبطه إجراء setup-android
# android.sdk_path = 

android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
