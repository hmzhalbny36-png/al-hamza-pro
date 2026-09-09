[app]

# اسم التطبيق الذي سيظهر داخل الهاتف
title = My Application

# اسم الحزمة (يجب أن يكون فريداً)
package.name = myapp
package.domain = org.test

# إصدار التطبيق
version = 0.1
version.code = 1

# المتطلبات (مكتبات بايثون التي تحتاجها)
requirements = python3,kivy

# نوع التطبيق (بما أن لديك main.py فهو بيسي)
orientation = portrait
fullscreen = 0

# الأيقونة (اختياري، اتركها فارغة أو ضع مسار صورة)
# icon.filename = icon.png

# إذنات الأندرويد المطلوبة
android.permissions = INTERNET

# الحد الأدنى لإصدار الأندرويد (API 21 = أندرويد 5.0)
android.minapi = 21
android.sdk = 33

# استخدم Gradle (أفضل للتوافق)
android.gradle_dependencies = ''

# لا تغير أي شيء تحت هذا السطر
[buildozer]
log_level = 2
warn_on_root = 1
