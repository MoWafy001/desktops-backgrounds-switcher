import ctypes, os
vda = ctypes.WinDLL(os.getcwd()+"\\VirtualDesktopAccessor.dll")
ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+"\\bb.jpg" , 0)
#####
def currentDesktop():
    return vda.GetCurrentDesktopNumber()
def setWallpaper(n):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+"\\"+str(n)+".jpg" , 0)
#####
pd = -1
cd = -1
while True:
    cd = currentDesktop()
    if pd != cd:
        pd = cd
        setWallpaper(cd)