import os

# def linkFilesInDirs (rootDir, outputFile):
#     if os.path.isdir(rootDir):
#         for dirName in os.listdir(rootDir):
#             nameStr = rootDir + '/' + dirName
#             if os.path.isdir(nameStr):
#                 for fileName in os.listdir(rootDir + '/' + dirName):
#                     subnameStr = rootDir + '/' + dirName + '/' + fileName
#                     linkFilesInDirs(subnameStr, 'fileList.txt')
#     else:
#         if rootDir[-2:] == '.m' or rootDir[-2:] == '.h' or rootDir[-3:] == '.mm':
#             with open(outputFile, 'a') as f:
#                 f.writelines(rootDir + '\n')
# linkFilesInDirs('/Users/xinshui/andy_prj/iOS/Coding-iOS', 'fileList.txt')

lineNumber = 0
file = open("fileList.txt")
for line in file.xreadlines():

    codef = open(line.strip())
    for codeLine in codef.xreadlines():
        codeLine = codeLine.strip('\n')
        if codeLine.lstrip()[:2] == '//' or\
                        codeLine.lstrip()[:2] == '/*' or\
                        codeLine.lstrip()[:2] == '#p' or\
                        codeLine.lstrip()[:1] == '*' or\
                        codeLine.lstrip() == '':
            pass
        else:
            # print(codeLine,)
            lineNumber += 1
    codef.close()
file.close()
print(lineNumber)
