import subprocess
from datetime import datetime

# =================================================
# Device 設定
# =================================================
DEVICE_ID = "emulator-5554"

# =================================================
# 根據你的清單過濾出的 App 對照表
# =================================================
APP_PACKAGE_MAP = {
    # 原有目標
    "Test APK": "com.viewsonic.testapk",
    # 你要求加入的系統/Google App
    "Calendar": "com.google.android.calendar",
    "Camera": "com.android.camera2",
    "Chrome": "com.android.chrome",
    "Clock": "com.google.android.deskclock",
    "Contacts": "com.google.android.contacts",
    "Drive": "com.google.android.apps.docs",
    "Files": "com.google.android.documentsui",
    "Gmail": "com.google.android.gm",
    "Google": "com.google.android.googlequicksearchbox",
    "Maps": "com.google.android.apps.maps",
    "Messages": "com.google.android.apps.messaging",
    "Phone": "com.android.phone",
    "Photos": "com.google.android.apps.photos",
    "Play Store": "com.android.vending",
    "Settings": "com.android.settings",
    "YouTube": "com.google.android.youtube",
    "YT Music": "com.google.android.apps.youtube.music",
    # 註：清單中未見 T-Mobile 相關包名，可能該模擬器環境未內建
}

# ANSI 顏色設定
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def run_command(command):
    try:
        return subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True, timeout=5
        ).strip()
    except:
        return ""


def get_version(package):
    # 在 Mac/Linux 環境下執行 shell 指令抓取版本
    cmd = f'adb -s {DEVICE_ID} shell "dumpsys package {package} | grep versionName"'
    output = run_command(cmd)
    for line in output.splitlines():
        if "versionName=" in line:
            return line.split("=")[-1].strip()
    return "N/A (未安裝)"


def main():
    print(f"\n🔍 正在掃描設備 {CYAN}{DEVICE_ID}{RESET} 的 App 版本資訊...\n")
    print(f"{'App Name':<15} | {'Package ID':<40} | {'Version'}")
    print("-" * 75)

    for app_name, package in APP_PACKAGE_MAP.items():
        version = get_version(package)

        # 顏色標記：找不到用紅色，找到用綠色
        v_color = RED if "N/A" in version else GREEN

        print(f"{app_name:<15} | {package:<40} | {v_color}{version}{RESET}")

    print("\n✅ 掃描完成。")


if __name__ == "__main__":
    main()
