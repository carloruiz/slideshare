import subprocess as sp
import time
import tempfile
from pdf2image import convert_from_path
from logic.models import Slide_id, Slide

BUCKET = 'https://s3.console.aws.amazon.com/s3/buckets/slide-share-thumbs'
WORK_DIR = os.getcwd()

def gen_err(userid, filename, err_str):
    return {
        "userid": userid,
        "filename": filename,
        "err": err_str,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    }

def run_subprocess(args, exception=Exception, timeout=30):
    try:
        res = sp.run(args=args, stdout=True, stderr=True, timeout=timeout)
        if res.returncode != 0:
            err = gen_err(userid, filename, res.stderr.decode('utf-8'))
            print(err)
            return 1
    except exception as e:
        err = gen_err(userid, filename, str(e))
        print(err)
        return 1
    
    return 0


def upload(userid, filename):
    
    #thread 0
    new_id = Slide_id()
    new_id.save()
    resourceid = new_id.id

    #thread 1
    #save locally, convert, upload to aws, 

    flag = 0
    idx = filename.rfind('.')
    name, ext = filename[:idx], filename[idx:]

    with tempfile.TemporaryDirectory() as path:
        args = 'libreoffice --headless --convert-to pdf %s --outdir %s' % (name+ext, path.name)
        flag = run_subprocess(args=args.split(), exception=sp.TimeoutExpired, timeout=20)
       
        if not flag:
            args = "pdftoppm -jpeg %s %s" % (name+'.pdf', path.name) 
            flag = run_subprocess(args=args.split(), timeout=20)

        os.remove(path+'/'+name+'.pdf')
        for f in os.listdir('.'):
            os.rename(f, '0'*(7-len(new_name[1:]))+new_name[1:])
        
        if not flag:
            args = 'aws s3 cp --recursive --quiet . s3://slide-share-thumbs/{}/{}/'.format(
                userid, resourceid)

        #aws s3 cp $PWD/01.jpg s3://slide-share-thumbs/1/6/011.jpg
        #delete pdf
 
         

    #thread 2


    # after join
    # while keyExists error gen resource id, try to insert row to db
    #

if __name__ == "__main__":
   upload('3', 'python.pptx') 
