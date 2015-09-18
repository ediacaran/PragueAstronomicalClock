all:	build deploy

build:
	buildozer android debug

deploy:
	adb install bin/PragueAstronomicalClock-0.0.1-debug.apk

uninstall:
	adb shell am start -a android.intent.action.DELETE -d package:org.test.astronomicalclock

