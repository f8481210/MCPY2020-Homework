from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while(30):
    x,y,z = mc.player.getTilePos()
    b = mc.getBlock(x,y-1,z)
    if b == 2: #要記得換行
        mc.setBlock(x,y,z,38) #前面要記得縮排
