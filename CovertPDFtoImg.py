""" 
* Le vent se lève, il faut tenter de vivre!
* Author: Better_OIer Zyx
* 起风了，唯有努力生存！
* Blog: http://betteroier.site:1000
* FileStation: http://betteroier.site:1005
* OnlineJudge: http://betteroier.site:8888
"""

"""
* 书图同归
* Bookture
"""

import os

import fitz  # TO INSTALL fitz use : "pip install PyMuPDF"


def covertPDFtoImg(pdfPath, outDir, name, format, enlarge, fromPg=-1,toPg=-1):
    if os.path.exists(pdfPath):
        print(f"[Inform] You are to covert {name}.pdf.")
    else:
        return print("[Error] File does not exist!")
    pdfDoc = fitz.open(pdfPath)
    print(f"[Inform] The file has {pdfDoc.page_count} pages.")
    
    if fromPg==-1:
        fromPg==1
        print("[Inform] The start page is not set. Set to page 1")
    elif fromPg<1 or fromPg>pdfDoc.page_count:
        fromPg=1
        print("[Warning] The start page invalid! Reset to page 1.")
    if toPg==-1:
        toPg=pdfDoc.page_count
        print(f"[Inform] The end page is not set. Set to page {pdfDoc.page_count}")
    elif toPg<1 or fromPg>toPg or toPg>pdfDoc.page_count:
        toPg=pdfDoc.page_count
        print(f"[Warning] The end page invalid! Reset to page {pdfDoc.page_count}.")
    print(f"[Inform] We will convert from page {fromPg} to page {toPg}, {toPg-fromPg+1} pages in total.")
    
    for pg in range(fromPg-1,toPg):
        page = pdfDoc[pg]
        rotate = int(0)
        #谨慎修改，细微的改动可能导致巨大的差异
        zoom_x = enlarge 
        zoom_y = enlarge
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        
        if not os.path.exists(outDir):
            os.makedirs(outDir)
            print("[Warning] The output directory does not exist. A new folder has been created for you automatically!")

        pix.save(f"{outDir}/{name}_{pg+1:04d}.{format}")
        print(f"[Inform] Successfully coverted: {outDir}/{name}_{pg+1:04d}.{format}")
        
    print(f"[Inform] Covert process completed successfully.")

if __name__ == "__main__":
    inDir = 'input_dir'
    outDir = 'output_dir'
    covertPDFtoImg(inDir, outDir, "PDF_name","jpg",3)
    #输入，输出，文件名，格式，放大倍数（谨慎修改），起始页（[1,末页]选填），结束页（[1,末页]选填）

