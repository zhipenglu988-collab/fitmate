[app]

# (str) Title of your application
title = FitMate

# (str) Package name
package.name = fitmate

# (str) Package domain (needed for android/ios packaging)
package.domain = com.fitmate

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let the pattern match)
source.include_exts = py,png,jpg,kv,atlas,ttf,txt

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let the pattern match)
#source.exclude_exts = spec

# (list) List of directory to exclude (let the pattern match)
#source.exclude_dirs = tests, bin

# (list) List of additional frameworks to include
#frameworks =

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
#version.regex = __version__ = ['"](.*)['"]
#version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd,plyer,apscheduler

# (str) Custom source folders for requirements
#requirements.source.kivy = ../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/icon.png

# (str) Supported orientation (one of landscape, sensor_landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY, NAME2:ENTRYPOINT2_TO_PY

# OSX specific
#
# (str) Supported OSX version
osx.python_version = 3

# (str) Kivy version to use
osx.kivy_version = 2.2.1

# OSX specific options
#osx.title =
#osx.cfbundleidentifier =

# Android specific
#

# (list) Permissions
android.permissions = INTERNET, RECEIVE_BOOT_COMPLETED, VIBRATE, POST_NOTIFICATIONS, FOREGROUND_SERVICE, WAKE_LOCK

# (int) Android API to use
android.api = 33

# (int) Minimum API
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 21

# (str) Android NDK version to use
#android.ndk = 19c

# (bool) Use Android's private storage for app data
#android.private_storage =

# (bool) Use Gradle instead of ant
android.gradle = true

# (str) Path to android's ant
#android.ant_path =

# (str) Path to android sdk
#android.sdk_path =

# (str) Path to android ndk
#android.ndk_path =

# (str) Path to Android SDK build-tools
#android.sdk_build_tools =

# (list) Android extra Jars to add to the java classpath
#android.add_src =

# (str) Android entry point, default is 'org.kivy.android.PythonActivity'
#android.entrypoint =

# (str) Android app theme, default is '@android:style/Theme.NoTitleBar'
#android.apptheme =

# (str) The Android logcat filter
#android.logcat_filters =

# (bool) Copy the python source code to the APK instead of using symlinks
#android.copy_sources = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (str) Path to the Android NDK
# android.ndk_path =

# (str) Android NDK version
android.ndk = 25b

# (str) Android SDK version
android.sdk = 33

# (str) Android SDK build tools
# android.sdk_build_tools =

# (bool) Use the Gradle build system for Android
#android.use_libpython = 1

# (list) The Android addons to install
#android.addons =

# (str) The Android package name
#android.package_name =

# (str) The Android intent to add
#android.intent =

# (list) The Android services to declare
#android.services =

# (str) The Android service to declare
#android.service =

# (str) The Android service class
#android.service_class =

# (str) The Android service permission
#android.service_permission =

# (str) The Android service process
#android.service_process =

# (str) The Android service type
#android.service_type =

# (str) The Android service export
#android.service_export =

# (str) The Android service meta data
#android.service_meta_data =

# (list) Launch modes for Android activity
#android.launch_modes =

# (bool) The Android service to declare
#android.service_restart =

# (list) The Android service to declare
#android.service_restart_delay =

# (list) The Android service to declare
#android.service_on_start_command =

# (list) The Android services to declare
#android.service_on_bind =

# (list) The Android services to declare
#android.service_on_unbind =

# (list) The Android services to declare
#android.service_on_destroy =

# (list) The Android services to declare
#android.service_on_handle_intent =

# (list) The Android services to declare
#android.service_on_start_command =

# (list) The Android services to declare
#android.service_on_bind =

# (list) The Android services to declare
#android.service_on_unbind =

# (list) The Android services to declare
#android.service_on_destroy =

# (list) The Android services to declare
#android.service_on_handle_intent =

# (list) The Android services to declare
#android.service_on_start_command =

# (list) The Android services to declare
#android.service_on_bind =

# (list) The Android services to declare
#android.service_on_unbind =

# (list) The Android services to declare
#android.service_on_destroy =

# (list) The Android services to declare
#android.service_on_handle_intent =

# (list) The Android services to declare
#android.service_on_start_command =

# (list) The Android services to declare
#android.service_on_bind =

# (list) The Android services to declare
#android.service_on_unbind =

# (list) The Android services to declare
#android.service_on_destroy =

# (list) The Android services to declare
#android.service_on_handle_intent =

# (list) The Android services to declare
#android.service_on_start_command =

# (list) The Android services to declare
#android.service_on_bind =

# (list) The Android services to declare
#android.service_on_unbind =

# (list) The Android services to declare
#android.service_on_destroy =

# (list) The Android services to declare
#android.service_on_handle_intent =

# (list) Android extra jars to add to the classpath
#android.add_src =

# (list) The Android AAR libraries to include
#android.aars =

# (list) The Android JAR libraries to include
#android.jars =

# (list) The Android AIDL imports to include
#android.aidl_imports =

# (list) The Android extra Java/Kotlin source directories
#android.add_src =

# (list) The Android extra resources directories
#android.add_res =

# (list) The Android extra assets directories
#android.add_assets =

# (list) The Android extra Java/Kotlin library jars to add to the classpath
#android.add_jar =

# (list) The Android extra native libraries to add to the libs directory
#android.add_libs =

# (list) The Android extra files to add to the assets directory
#android.add_assets =

# (list) The Android extra Java/Kotlin lint jars to add to the lint directory
#android.add_lint =

# (list) The Android extra Java/Kotlin proguard files
#android.proguard =

# (str) Path to the Android keystore
#android.keystore =

# (str) The Android keystore password
#android.keystore_password =

# (str) The Android key alias
#android.keyalias =

# (str) The Android key password
#android.keypassword =

# (str) The Android AAR library to include
#android.aar =

# (str) The Android JAR library to include
#android.jar =

# (str) The Android AIDL import to include
#android.aidl_import =

# (str) The Android extra Java/Kotlin source directory
#android.add_src =

# (str) The Android extra resources directory
#android.add_res =

# (str) The Android extra assets directory
#android.add_assets =

# (str) The Android extra Java/Kotlin library jar to add to the classpath
#android.add_jar =

# (str) The Android extra native library to add to the libs directory
#android.add_lib =

# (str) The Android extra file to add to the assets directory
#android.add_asset =

# (str) The Android extra Java/Kotlin lint jar to add to the lint directory
#android.add_lint =

# (str) The Android extra Java/Kotlin proguard file
#android.proguard =

# (list) Android Gradle dependencies
android.gradle_dependencies = 'androidx.core:core:1.9.0'

# (list) Android Gradle repositories
#android.gradle_repositories =

# (list) Add a compile options to the generated build.gradle
#android.gradle_options =

# (bool) Enable the AndroidX support
android.use_androidx = True

# (bool) Enable the AndroidX legacy support
#android.use_androidx_legacy =

# (bool) Enable the AndroidX multidex support
#android.multidex = True

# Icons
#icon.filename = icon.png

# Presplash
#presplash.filename = presplash.png

# iOS specific
#

# (str) iOS SDK version
#ios.sdk_version = 13.0

# (str) iOS deployment target
#ios.deployment_target = 11.0

# (str) iOS icon
#ios.icon = ios-icon.png

# (str) iOS presplash
#ios.presplash = ios-presplash.png

# (list) iOS permissions
#ios.permissions =

# (str) iOS plugin
#ios.plugin =

# (list) iOS frameworks
#ios.frameworks =

# (list) iOS source files
#ios.source_files =

# Windows specific
#

# (str) Windows version
#win.version = 10.0

# (bool) Windows build for 32-bit
#win.32bit = False

# (str) Windows icon
#win.icon = win-icon.png

# (str) Windows presplash
#win.presplash = win-presplash.png

# Linux specific
#

# (str) Linux version
#linux.version = 10.0

# (bool) Linux build for 32-bit
#linux.32bit = False

# (str) Linux icon
#linux.icon = linux-icon.png

# (str) Linux presplash
#linux.presplash = linux-presplash.png

# macOS specific
#

# (str) macOS version
#macos.version = 10.9

# (bool) macOS build for 32-bit
#macos.32bit = False

# (str) macOS icon
#macos.icon = macos-icon.png

# (str) macOS presplash
#macos.presplash = macos-presplash.png

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug, 3 = debug info)
log_level = 1

# (int) Number of parallel jobs to use, set to 0 to let buildozer decide
#jobs = 4

# (str) Target to build (android, ios, windows, linux, osx)
target = android

# (str) Path to the build directory
#build_dir = ./build

# (str) Path to the bin directory (generated APKs go here)
#bin_dir = ./bin

# (str) Path to the Android SDK
#android_sdk_path =

# (str) Path to the Android NDK
#android_ndk_path =

# (str) Path to the Android ant
#android_ant_path =

# (str) Path to the Android gradle
#android_gradle_path =

# (bool) Use the Gradle build system for Android
#android.use_gradle = True
