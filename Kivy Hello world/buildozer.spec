[app]
# (str) Title of your app
title = My Kivy App
# (str) Package name
package.name = mykivyapp
# (str) Package domain (needed for android/ios packaging)
package.domain = org.test
# (str) Your application's version
version = 0.1
# (str) Your application's source code directory
source.dir = .
# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas
# (list) List of directory to exclude (for source.include_exts)
source.exclude_dirs = tests, bin
# (list) List of exclusions using pattern matching
source.exclude_patterns = license,images/*/*.png
# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png  # اگر آیکون دارید، این مسیر را تنظیم کنید
# (str) Presplash of the application
presplash.filename = %(source.dir)s/presplash.png  # اگر presplash دارید

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 30
# (int) Minimum API your APK will support.
android.minapi = 21

# Kivy version to use
android.version = 2.1.0

# Python for android recipe
requirements = python3,kivy