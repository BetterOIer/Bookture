## 书途同归 Bookture

by Zyx Better_OIer

这是一个可以把`PDF`转化成图片，并把转化完成后图片合并成拼图的`Python`程序

## 用途

### 电子书

若用于转换`.epub`等电子书文件，本程序需搭配`Calibre`食用，推荐配置
![1727705125369](image/example.png)

对于`CovertPDFtoImg.py`，使用
```python
covertPDFtoImg(inDir, outDir, "PDF_name","jpg",2)
```

对于`MergeImg.py`，使用
```python
mergeImgs(inDir, outDir,"jpg",5,8,True,1)
```

~~可以**刚刚好**放进响应~~(Unpdate 25.01.18 现在好像得5x6了，自己试试吧)

### 普通A4文件

对于`CovertPDFtoImg.py`，使用
```python
covertPDFtoImg(inDir, outDir, "PDF_name","jpg",3)
```

对于`MergeImg.py`，使用
```python
mergeImgs(inDir, outDir,"jpg",3,4,True,1)
```

可以**刚刚好**放进响应

### 可选参数

对于`CovertPDFtoImg.py`，
```python
covertPDFtoImg(inDir, outDir, "PDF_name","jpg",2,1,100)
#输入，输出，文件名，格式，放大倍数（谨慎修改），起始页（[1,末页]选填），结束页（[1,末页]选填）
```
对于`MergeImg.py`，
```python
mergeImgs(inDir, outDir,"jpg",5,8,True,1,(255,255,255))
#输入，输出，格式，长，宽，是否划线，编号开始下标，背景颜色（选填）
```
**注意**，背景颜色仅仅指**合成图片的背景色**，如果源PDF文件背景与背景颜色不同，PDF文件背景会覆盖图片背景。你应该在食用该程序前将两者调成一致