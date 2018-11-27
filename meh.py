#meh.py
from mcpi import minecraft
#from time import sleep
#flower = 38

mc = minecraft.Minecraft.create()
mc.postToChat("BIG MEME")
x, y, z = mc.player.getPos()


#floor
mc.setBlocks(x, y-1, z, x, y-1, z+10, 3)
mc.setBlocks(x, y-1, z, x, y-1, z+10, 3)
mc.setBlocks(x+1, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x+2, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x+3, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x-1, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x-2, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x-3, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x-4, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x-5, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x-6, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x-7, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x-8, y-1, z, x, y-1, z+10, 24)
mc.setBlocks(x-9, y-1, z, x, y-1, z+10, 24)
#flooring1 addon
mc.setBlocks(x-3, y, z+1, x-4, y+1, z+2, 5)#wooden block
#stairs
mc.setBlock(x, y, z+10, 128,2)
mc.setBlock(x+1, y, z+10, 128,1)
mc.setBlock(x-1, y, z+10, 128,2)
mc.setBlock(x-2, y, z+10, 128,2)
#flooring2
mc.setBlock(x+2, y, z+10, 24)
mc.setBlock(x+3, y, z+10, 24)
mc.setBlock(x+4, y, z+10, 24)
mc.setBlock(x+5, y, z+10, 24)
mc.setBlocks(x-3, y, z+10, x-4, y, z+11, 35,12)
mc.setBlocks(x-3, y+1, z+10, x-4, y+1, z+11, 35,12)
mc.setBlocks(x, y, z+11, x-2, y, z+28, 24)
mc.setBlocks(x+1, y, z+11, x+5, y, z+28, 24)
mc.setBlocks(x-3, y, z+11, x-4, y, z+24, 24)
#flooring2 addons
mc.setBlocks(x-1, y+1, z+16, x-1, y+2, z+16, 5)#pilar 1
mc.setBlocks(x-2, y+1, z+18, x-2, y+2, z+18, 5)#pilar 2
mc.setBlocks(x-1, y+1, z+21, x-1, y+2, z+21, 5)#pilar 3
mc.setBlocks(x-1, y+1, z+27, x-1, y+3, z+27, 42)#iron blocks
mc.setBlocks(x, y+1, z+27, x, y+3, z+27, 42)
mc.setBlocks(x-1, y+1, z+26, x-1, y+2, z+26, 42)
mc.setBlock(x, y+1, z+25, 42)
mc.setBlocks(x+2, y+1, z+21, x+3, y+2, z+21, 5)#block in front of door
mc.setBlocks(x+2, y+1, z+20, x+3, y+2, z+20, 5)
mc.setBlocks(x+2, y+1, z+22, x+3, y+2, z+22, 65,3)
mc.setBlocks(x+2, y+1, z+19, x+3, y+2, z+19, 65,2)
mc.setBlocks(x+2, y+1, z+10, x+5, y+1, z+10, 24)#wall
mc.setBlocks(x+5, y+1, z+10, x+5, y+5, z+15, 24)
mc.setBlock(x+5, y+5, z+16, 24)
mc.setBlock(x+5, y+5, z+20, 24)
mc.setBlocks(x+5, y+1, z+21, x+5, y+5, z+28, 24)
mc.setBlocks(x+5, y+1, z+28, x-2, y+5, z+28, 24)
mc.setBlocks(x-2, y+2, z+28, x-2, y+5, z+25, 24)
mc.setBlocks(x-3, y+1, z+24, x-3, y+5, z+24, 24)
mc.setBlocks(x-4, y+1, z+12, x-4, y+1, z+23, 24)
mc.setBlocks(x+5, y+1, z+16, x+5, y+4, z+16, 2)#iron door
mc.setBlocks(x+5, y+5, z+17, x+5, y+5, z+19, 42)
mc.setBlocks(x+5, y+1, z+16, x+5, y+4, z+16, 42)
mc.setBlocks(x+5, y+1, z+20, x+5, y+4, z+20, 42)













#while True:
#	x, y, z = mc.player.getPos()
#	mc.setBlock(x, y, z, flower)
#	sleep(0.1)
