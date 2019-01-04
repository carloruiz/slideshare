import subprocess as sp
import time
import tempfile
from pdf2image import convert_from_path


def gen_err(userid, filename, err_str):
    return {
        "userid": userid,
        "filename": filename,
        "err": err_str,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    }

def upload(userid, filename):
    #thread 1
    #save locally (add salt to filename), convert, upload to aws, 
    try:
        res = sp.run(args=["libreoffice", "--headless", "--convert-to", "pdf", filename], 
            stdout=True, stderr=True, timeout=30)
        if res.returncode != 0:
            err = gen_err(userid, filename, res.stderr.decode('utf-8'))
            print(err)
            return
    except sp.TimeoutExpired as e:
        err = gen_err(userid, filename, "timeout error")
        print(err)
        return

    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path('/slideshare/python.pdf', output_folder=path)
    
    if not images:
        err = gen_err(userid, filename, "pdf2image error")
        print(err)
        return

    for img in images:
        

    #thread 2

if __name__ == "__main__":
    
