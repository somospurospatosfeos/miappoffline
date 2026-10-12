[app]
title = Mi App
package.name = miapp
package.domain = com.oscar.miapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 1

# SOLO ARM64 para que no demore 2 horas
[app:android]
android.archs = arm64-v8a
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2
p4a.branch = master
