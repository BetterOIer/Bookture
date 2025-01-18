from CovertPDFtoPNG import covertPDFtoImg
from MergePNG import mergeImgs

name = "Your_PDF_Name"
imgFormat = "jpg"

inFile = f"Your_File_Path\\{name}.pdf"
tempDir = f"Your_File_Path\\{name}temp"
outDir = f"Your_File_Path\\{name}"

confirm = input(f"[Inform] Run Program 1?")
if confirm == "":
    covertPDFtoImg(inFile, tempDir, name, imgFormat, 2)
else:
    print(f"[Error] Program 1 terminated by user!")

confirm = input(f"[Inform] Run Program 2?")
if confirm == "":
    mergeImgs(tempDir, outDir, imgFormat, 5, 8, True, 1, (250, 249, 222))
else:
    print(f"[Error] Program 2 terminated by user!")