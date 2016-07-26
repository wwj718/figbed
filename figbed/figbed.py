# coding=utf-8

import os
import sys
import time
import math
import random
import string
import operator
import commands
from PIL import Image
from hashlib import md5
import uuid
from qiniu import Auth, put_file, etag
import yaml
from os.path import expanduser,join
from shutil import copyfile



home = expanduser("~")
with open(os.path.join(home,".qiniu.yml")) as f:
    config = yaml.load(f)
    ak = config["AK"]
    sk = config["SK"]
    domain = config["YOUR_DOAMIN"] # http://oav6fgfj1.bkt.clouddn.com
    bucket = config["YOUR_BUCKET"]
    saveas = config.get("PATH_SAVEAS","/tmp")

pngpaste = '/usr/local/bin/pngpaste' # 不同操作系统，可能路径不同

if len(sys.argv) == 2:
    pngpaste = sys.argv[1]

q = Auth(ak, sk)

# check pngpaste is exists
re = os.system(pngpaste)
if re == 127:
    print 'command:%s' % pngpaste, 'not exists'
    sys.exit(1)


def image_similar(image1, image2):
    temp1 = Image.open(image1)
    temp2 = Image.open(image2)
    h1 = temp1.histogram()
    h2 = temp2.histogram()
    rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    print 'two image similar is:', rms
    return rms


def upload_file(upload_file_name, temp):
    # upload_file_name就是文件名
    # 复制到 saveas目录下
    #  先保存到固定文件夹,纳入git管理：saveas
    #key = md5(str(time.time())+''.join(random.sample(string.letters, 12))).hexdigest()
    # key 请求用户输入
    print u"请输入图片名: ",
    pic_name = raw_input()
    uuid_6 = uuid.uuid4().get_hex()[:8] #保证唯一性
    key = pic_name+"_"+uuid_6+".png"
    copyfile(upload_file_name,join(saveas,key))
    mime_type = 'image/png'
    token = q.upload_token(bucket, key)
    ret, info = put_file(token, key, upload_file_name, mime_type=mime_type, check_crc=True)
    print 'upload qiniu result:', info
    assert ret['key'] == key
    assert ret['hash'] == etag(upload_file_name)
    os.rename(upload_file_name, upload_file_name+'.old')
    return domain+'/'+key

file_name = 'test.png' #临时存在当前文件夹下

# todo截图之后，要求用户输入名字
# todo截图之后，默认保证到某个目录，允许创建子目录

def main():
    while True:
        time.sleep(1)
        print u'正在等待截图..................'
        status, output = commands.getstatusoutput(pngpaste+' '+file_name)
        if output.find('No image data found on the clipboard') > 0:
            continue
        if status == 0:
            if os.path.exists(file_name+'.old'):
                if image_similar(file_name+'.old', file_name) > 0:
                    url = upload_file(file_name, None)
                    os.system('echo "'+url+'"|/usr/bin/pbcopy')
            else:
                url = upload_file(file_name, None)
                os.system('echo "'+url+'"|/usr/bin/pbcopy')
