#
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
long = int(input("請輸入長度："))  #長
width = int(input("請輸入寬度："))  #寬
length = int(input("請輸入高度："))  #高
blockid = int(input("請輸入方塊id：")) 
air = 0

mc.setBlocks(x,y,z,x+long,y+length,
             z+width,blockid) #外圍
mc.setBlocks(x+1,y+1,z+1,x+long-1,
             y+length-1,z+width-1,air) #裡面填滿空氣
mc.setBlocks(x,y+1,z+1,x,y+2,z+1,air) #門

mc.setBlocks(x,y+length,z,x+long,y+length,
             z+width,169) #天花板
mc.setBlocks(x+1,y+length/2,z+1,x+long-1,y+length/2,
             z+width-1,169) #中間
mc.setBlocks(x+2,y+length/2,z+2,x+long-2,y+length/2,
             z+width-2,0) #中間挖空

