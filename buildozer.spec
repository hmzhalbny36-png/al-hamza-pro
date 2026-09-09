name: Build Android APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: 1. سحب الكود
      uses: actions/checkout@v4

    - name: 2. إعداد Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: 3. تثبيت متطلبات النظام
      run: |
        sudo apt update
        sudo apt install -y \
          git zip unzip openjdk-17-jdk \
          autoconf libtool pkg-config zlib1g-dev \
          libncurses5-dev libncursesw5-dev libtinfo5 \
          cmake libffi-dev libssl-dev
        # تعيين Java 17 كلغة افتراضية
        sudo update-alternatives --set java /usr/lib/jvm/java-17-openjdk-amd64/bin/java

    - name: 4. تثبيت Buildozer
      run: |
        pip install --upgrade pip
        pip install buildozer cython

    # ===== الطريقة اليدوية المضبوطة (تنجح دائماً) =====
    - name: 5. تثبيت Android SDK وقبول التراخيص يدوياً
      run: |
        # تحديد المسار الثابت لـ SDK
        export ANDROID_HOME="$HOME/.buildozer/android/platform/android-sdk"
        mkdir -p "$ANDROID_HOME"
        
        # تحميل أحدث أدوات سطر الأوامر (رابط رسمي من Google)
        wget -q https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O /tmp/cmdline-tools.zip
        unzip -q /tmp/cmdline-tools.zip -d /tmp/
        mkdir -p "$ANDROID_HOME/cmdline-tools"
        mv /tmp/cmdline-tools "$ANDROID_HOME/cmdline-tools/latest"
        
        # إضافة الـ SDK إلى مسار التنفيذ
        echo "$ANDROID_HOME/cmdline-tools/latest/bin" >> $GITHUB_PATH
        echo "ANDROID_HOME=$ANDROID_HOME" >> $GITHUB_ENV
        
        # قبول جميع التراخيص بدون تدخل (هذا يحل مشكلتك الأساسية)
        yes | "$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" --licenses > /dev/null 2>&1
        
        # تثبيت Build-Tools 37 و Platform المطلوبة
        "$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" "build-tools;37.0.0" "platforms;android-33"
    # =====================================================

    - name: 6. بناء ملف APK
      run: |
        # تأكد من وجود ملف buildozer.spec في مجلد المشروع
        if [ ! -f "buildozer.spec" ]; then
          echo "❌ ملف buildozer.spec غير موجود! قم بإنشائه أولاً."
          exit 1
        fi
        # إجبار Buildozer على استخدام SDK الذي ثبتناه
        export ANDROID_HOME="$HOME/.buildozer/android/platform/android-sdk"
        buildozer android debug

    - name: 7. رفع ملف APK الناتج
      uses: actions/upload-artifact@v4
      with:
        name: app-debug
        path: bin/*.apk
