import uiautomator2
import time


def follow_pub(devices_id):
    devices = uiautomator2.connect_usb(devices_id)
    devices(resourceId='com.next.innovation.takatak:id/follow_button').click_exists(5)
    time.sleep(2)
    devices.swipe_ext('up', 1)
    time.sleep(0.5)


if __name__ == '__main__':
    times = 0
    while times < 200:
        follow_pub('711KPPB0781840')
        times += 1
        print(times)