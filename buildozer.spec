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

android.accept_sdk_license = True
android.p4a_whitelist = libjpeg-turbo, libpng, libfreetype
android.ndk = 28c

# تحديد إصدار Python المستخدم داخل Android (لا يزال 3.10)
python.requirements = pip==23.2.1, setuptools==68.0.0, wheel==0.41.0

[buildozer]
log_level = 2
warn_on_root = 1
