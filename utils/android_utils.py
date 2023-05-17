import subprocess


def get_device_uuid() -> str:
    devices = subprocess.run(
        ["adb", "devices"], capture_output=True, text=True
    ).stdout
    try:
        return devices.split()[4]
    except IndexError:
        raise Exception("No active devices")


def get_device_udid():
    output = subprocess.check_output(["adb", "devices"]).decode().split('\n')
    device = output[1].split("\t")[0]

    return device


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_device_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
