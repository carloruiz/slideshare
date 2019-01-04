import subprocess as sp
import time

''' 
error: {
    user_id: int,
    filename: str,
    errStr: str,
    timestamp: str
}
    
'''

def gen_err(userid, filename, err_str):
    return {
        "userid": userid,
        "filename": filename,
        "err": err_str,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    }

def upload(filename):
    #thread 1
    #save locally (add salt to filename), convert, upload to aws, 
    try:
        res = sp.run(args=["libreoffice", "--headless", "--convert-to", "pdf", filename], 
            stdout=True, stderr=True, timeout=30)
        if res.returncode != 0:
            err = gen_err(None, filename, res.stderr.decode('utf-8'))
            print(err)
            return
    except sp.TimeoutExpired as e:
        err = gen_err(None, filename, "timeout error")
        print(err)
        return


    #thread 2

if __name__ == "__main__":
    
