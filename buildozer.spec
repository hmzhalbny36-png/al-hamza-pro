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

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.minapi = 21
android.sdk = 33
android.gradle_dependencies = ''

android.accept_sdk_license = True

# --- الإعدادات المحسّنة لتجنب تعليق البناء ---
# تجميع معمارية واحدة فقط (لتخفيف الحمل على الذاكرة)
android.arch = armeabi-v7a
# استخدام إصدار NDK أخف
android.ndk = 27c
# استبدال الإعداد القديم (p4a_whitelist) بالجديد
android.whitelist = libjpeg-turbo, libpng, libfreetype

# --- ملاحظة: تم حذف سطر python.requirements لتجنب التعارض ---

[buildozer]
log_level = 2
warn_on_root = 1
