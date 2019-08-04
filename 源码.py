import time

# 原理是先将需要发送的文本放到剪贴板中，然后将剪贴板内容发送到qq窗口
# 之后模拟按键发送enter键发送消息

import win32gui
import win32con
import win32clipboard as w


def send(to_who, msg):
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    # 将消息写到剪贴板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()
    # 获取qq窗口句柄
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


count = 0

err = 0

show = False

while True:
    isShow = input('是否显示好友名称（y/n）:')
    if isShow == 'n':
        err = 0
    elif isShow == 'y':
        err = 2
    else:
        err = 1
    if err == 1:
        print('输入错误！将默认不显示')
        show = False
        break
    elif err == 2:
        show = True
        break
    else:
        show = False
        break



while True:
    man = 'Python'
    count += 1
    send(man,'test')
    if show == True:
        print('[INFO] 已发'+count.__str__()+'条消息给'+man)

    else:
        print('[INFO] 已发' + count.__str__() + '条消息给' + (len(man))*'*')
    time.sleep(1)
    if count >= 5:
        exit(233)