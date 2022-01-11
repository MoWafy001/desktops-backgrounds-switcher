import ctypes, os
vda = ctypes.WinDLL(os.getcwd()+"\\VirtualDesktopAccessor.dll")
#####
def currentDesktop():
    return vda.GetCurrentDesktopNumber()
def setWallpaper(n):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+"\\"+str(n)+".jpg" , 0)
#####
pd = -1
cd = -2
while True:
    cd = currentDesktop()
    if pd != cd:
        pd = cd
        setWallpaper(cd)
