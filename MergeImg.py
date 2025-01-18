""" 
* Le vent se lève, il faut tenter de vivre!
* Author: Better_OIer Zyx
* 起风了，唯有努力生存！
* Blog: http://betteroier.site:1000
* DicStation: http://betteroier.site:1005
* OnlineJudge: http://betteroier.site:8888
"""

"""
* 书图同归
* Bookture
"""

import os
from PIL import Image, ImageDraw
from math import ceil

def mergeImgs(inDir, outDir, format, pgRow, pgCol=-1, drawFlag=True, imgCnt=1, bgColor=(255, 255, 255)):
    
    """
    This is the merge function, 
    please make sure that the input directory ONLY contains image Dics
    """
    
    # Prompts validity checking
    if not os.path.exists(inDir):
        return print("[Error] Directory does not exist!")
    if not os.path.exists(outDir):
        os.makedirs(outDir)
        print("[Warning] The output directory does not exist. A new folder has been created for you automatically!")
    if pgCol==-1: pgCol=2147483647
    
    # Initializing parameters
    Dics=sorted(os.listdir(inDir))
    imgs=[];n=len(Dics);maxX=0;maxY=0;pgCnt=0;perImg=pgRow*pgCol
    print(f"[Inform] You are to merge {n} Dics: {Dics}.")
    for Dic in Dics:
        imgs.append(Image.open(os.path.join(inDir,Dic)))
        maxX=max(maxX,imgs[-1].width)
        maxY=max(maxY,imgs[-1].height)
    if maxX==0 or maxY==0:
        return print("[Error] Failed to acquire image data!")
    
    # Merge Loop
    while pgCnt<n:  # This layer processes each merged image
        # Boundary detection
        if pgCnt+perImg<=n:
            newImg=Image.new("RGB",(maxX*pgRow,maxY*pgCol),bgColor)
            thsiImgCnt=perImg;xLimit=pgRow;yLimit=pgCol
        elif pgCnt+pgRow<=n:
            newImg=Image.new("RGB",(maxX*pgRow,maxY*ceil((n-pgCnt)/pgRow)),bgColor)
            thsiImgCnt=n-pgCnt;xLimit=pgRow;yLimit=ceil((n-pgCnt)/pgRow)
        else:
            newImg=Image.new("RGB",(maxX*(n-pgCnt),maxY),bgColor)
            thsiImgCnt=n-pgCnt;xLimit=n-pgCnt;yLimit=1
        
        # Paste each image
        cnt=0;j=0
        while cnt<thsiImgCnt:   # This layer processes each row
            for i in range(xLimit):     # This layer processes each column
                if cnt>=thsiImgCnt: break
                newImg.paste(imgs[pgCnt],(maxX*i,maxY*j))
                pgCnt+=1;cnt+=1
            j+=1
        
        # Draw lines
        if drawFlag:
            draw=ImageDraw.Draw(newImg)
            black=(0, 0, 0)
            grey=(128,128,128)
            for i in range(1,xLimit):
                stPoint = (maxX*i-1, 0)
                edPoint = (maxX*i-1,maxY*yLimit)
                draw.line((stPoint,edPoint), fill=grey, width=2)
            for i in range(1,yLimit):
                stPoint = (0, maxY*i-1)
                edPoint = (maxX*xLimit,maxY*i-1)
                draw.line((stPoint,edPoint), fill=black, width=2)
            
        # Save merged images
        newImg.save(os.path.join(outDir,f"{imgCnt:03d}.{format}"))
        print(f"[Inform] Successfully exported {imgCnt:03d}.{format}! rect:{newImg.width}x{newImg.height}, {thsiImgCnt} images merged. Left {n-pgCnt} images.")
        imgCnt+=1
        
    print(f"[Inform] Merge process completed successfully.")
 
if __name__ == "__main__":
    inDir = "input_dir"
    outDir = "output_dir"
    mergeImgs(inDir, outDir,"jpg",1,1,True,1,(255,255,255))
    #输入，输出，格式，长，宽，是否划线，编号开始下标，背景颜色（选填）
