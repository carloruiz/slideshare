from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.db.utils import IntegrityError
from logic.models import Slide_id, Slide

import subprocess as sp
import os
import tempfile
from datetime import datetime
from random import randint
from threading import Lock, Thread


FILE_BUCKET = 'https://s3.amazonaws.com/slide-sharing-platform'
THUMB_BUCKET = 'https://s3.amazonaws.com/slide-share-thumbs' 



def gen_err(userid, filename, err_str):
    return {
        "userid": userid,
        "filename": filename,
        "err": err_str,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    }

def run_subprocess(args, userid, filename, exception=Exception, timeout=30):
    try:
        res = sp.run(args=args, stderr=sp.PIPE, timeout=timeout)
        if res.returncode != 0:
            err = gen_err(userid, filename, res.stderr.decode('utf-8'))
            print(err)
            return 1
    except exception as e:
        err = gen_err(userid, filename, str(e))
        print(err)
        return 1
    
    return 0

def strfmt_bytes(size):
    # MacOS displays different file size in teriminal vs finder
    # I chose to display finder size.. To get 'real' size use 
    # power = 1024
    power = 1000
    n = 0
    Dic_powerN = {0 : '', 1: 'K', 2: 'M', 3: 'G'}
    while size > power:
        size /=  power
        n += 1
    return str(round(size)) + ' ' + Dic_powerN[n]+'B'




new_id = None
filesize = None
new_id = None
lock = Lock()

def thread1():
    # TODO upload method with less collisions
    # lock is only used so other thread sleeps
    lock.acquire()
    while True:
        try:
            new_id = Slide_id(randint(1,10e5))
            new_id.save()
        except IntegrityError as e:
            continue
        break
    resourceid = new_id.id
    lock.release()

    # upload file to aws
    filesize = strfmt_bytes(os.path.getsize(filename))

def thread2():
    with tempfile.TemporaryDirectory() as path:
        args = 'libreoffice --headless --convert-to pdf %s --outdir %s' % (name+ext, path)
        flag = run_subprocess(args.split(), userid, 
            filename, exception=sp.TimeoutExpired, timeout=20)
            
        if not flag:
            args = "pdftoppm -jpeg %s %s/" % (path+'/'+name+'.pdf', path) 
            flag = run_subprocess(args.split(), userid, filename, timeout=20)
       
        os.remove(path+'/'+name+'.pdf')
        for f in os.listdir(path):
            os.rename(path+'/'+f, path+'/'+'0'*(7-len(f[1:]))+f[1:])
        
        
        if not flag:
            args = 'aws s3 cp --recursive --quiet {} s3://slide-share-thumbs/{}/{}/'.format(
                path, userid, resourceid)
            flag = run_subprocess(args.split(), userid, filename, timeout=20)



def upload(userid, filename, resource_name, description):
    #base thread
    #save file locally

    #thread 0

    #thread 1
    #save locally, convert, upload to aws, 

    flag = 0
    idx = filename.rfind('.')
    name, ext = filename[:idx], filename[idx:]

       

    # after join
    
    new = Slide(**{
        "id": new_id,
        "name": resource_name,
        "size": filesize,
        "url": '%s/%s/%s' % (FILE_BUCKET,userid, resourceid),
        "thumbnail": '%s/%s/%s' % (THUMB_BUCKET, userid, resourceid),
        "user_id": userid,
        "description": description,
        "last_mod": datetime.now(tz=timezone.utc)
    })

    try:
        new.save()
    except Exception as e:
        err = gen_err(userid, filename, str(e))
        print(err)
        return


def index(request):
   return upload('3', 'python.pptx', 'Python Lecture 1', "Python presentation for the masses")

