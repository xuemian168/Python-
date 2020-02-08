import os,shutil

before = '移动前 尾部不需要/'
after = '移动后目录 尾部不需要/'
n=0
if os.path.exists(after):
    print('处理后目录不存在')
else:
    os.mkdir(after)
if os.path.exists(after+'/vedio'):
    print('视频目录已存在')
else:
    os.mkdir(after+'/vedio')
if os.path.exists(after+'/photo'):
    print('图片目录已存在')
else:
    os.mkdir(after+'/photo')
print('判断目录完成')
for foldername,subfolders,filenames in os.walk(before):
    print(foldername)
    for filename in filenames:
        if '.jpg' in filename or '.JPG' in filename:
            try:
                shutil.copy(foldername + '/' + filename,after+'/photo/'+ str(n+1) + '.jpg')
                n+=1
            except OSError:
                pass
    for filename in filenames:
        if '.mp4' in filename or '.MP4' in filename:
            try:
                shutil.copy2(foldername + '/' + filename, after + '/vedio/' + str(n+1) + '.mp4')
                n+=1
            except:
                pass
        else:
            pass
print('处理完成')