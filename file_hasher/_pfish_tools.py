__author__ = 'girish'

import argparse
import os
import logging
import time
import hashlib
import csv
log = logging.getLogger('main._pfish')

global gl_args
global gl_hashType

def ValidateDirectory(theDir):
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError("Directory does not exist")
    else:
        return theDir
def ValidateDirectoryWritable(theDir):
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError("Directory does not exist")
    if os.access(theDir,os.W_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError("Directory is not writable")



def parse_command_line():
    parser= argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('--md5',help='specifies MD5 algorithm',action='store_true')
    group.add_argument('--sha256', help='specifies SHA256 algorithm', action='store_true')
    group.add_argument('--sha512', help='specifies SHA512 algorithm', action='store_true')
    parser.add_argument('-d','--dirpath',type=ValidateDirectory,required=True,help="specify the root path for hashing")
    parser.add_argument('-r','--reportpath',type=ValidateDirectoryWritable,required=True,help="specify the path for reports and logs will be written")
    global gl_args
    global gl_hashType
    gl_args = parser.parse_args()
    if gl_args.md5:
        gl_hashType='MD5'
    elif gl_args.sha256:
        gl_hashType='SHA256'
    elif gl_args.sha512:
        gl_hashType='SHA512'
    else:
        gl_hashType='unknown'


def Walk_path():
    processCount = 0
    errorCount = 0
    oCSV =CSVWriter(gl_args.reportpath+'\\fileSystemReport1.csv',gl_hashType)
    for root,dirs,files in os.walk(gl_args.dirpath):
        for file in files:
            fname = os.path.join(root,file)
            result =HashFile(fname,file,oCSV)
            if result == True:
                processCount+=1
            else:
                errorCount += 1


class CSVWriter:
    def __init__(self,filename,hashtype):
        """

        :param filename:
        :param hashtype:
        """
        try:

            self.csvfile = open(filename,'w')
            self.writer = csv.writer(self.csvfile,delimiter=",",quoting=csv.QUOTE_ALL)
            self.writer.writerow(('File','Path','Size','Modified Time','Access Time','Created Time','hashType','Owner','Group','Mode'))
        except :
            log.error("CSV store failed for "+filename)
    def writeCSVrow(self,simplename,theFile,fileSize,modifiedTIme,accessTime,createdTime,hashValue,ownerID,groupID,mode):
        """
        method takes in the required
        :param simplename:
        :param theFile:
        :param fileSize:
        :param modifiedTIme:
        :param accessTime:
        :param createdTime:
        :param hashValue:
        :param ownerID:
        :param groupID:
        :param mode:
        """
        self.writer.writerow((simplename,theFile,fileSize,modifiedTIme,accessTime,createdTime,hashValue,ownerID,groupID,mode))

    def close(self):
        self.csvfile.close()



def HashFile(theFile,simplename,o_result):
    if os.path.exists(theFile):
        if os.path.isfile(theFile):
            try:
                f=open(theFile,'rb')
            except IOError:
                log.warning("open failed :"+theFile)
                return
            else:
                try:
                    rd = f.read()
                except IOError:
                    f.close()
                    log.warning("read failed:"+theFile)
                    return

                else:
                    theFileStats=os.stat(theFile)
                    (mode,ino,dev,nlink,uid,gid,size,atime,mtime,ctime)=os.stat(theFile)
                    log.info("Processing File: "+theFile)
                    fileSize = str(size)
                    modifiedTIme= time.ctime(mtime)
                    accessTime = time.ctime(atime)
                    createdTime = time.ctime(ctime)
                    ownerID = str(uid)
                    groupID = str(gid)
                    fileMode = bin(mode)

                    if gl_args.md5:
                        hashout = hashlib.md5()
                        hashout.update(rd)
                        hexmd5 = hashout.hexdigest()
                        hashValue = hexmd5.upper()
                    elif gl_args.sha256:
                        hashout = hashlib.sha256()
                        hashout.update(rd)
                        hexsha256 = hashout.hexdigest()
                        hashValue = hexsha256.upper()
                    elif gl_args.sha512:
                        hashout = hashlib.sha512()
                        hashout.update(rd)
                        hexsha512 = hashout.hexdigest()
                        hashValue = hexsha512.upper()
                    else:
                        log.error("hash not Selected")

                    f.close()
                    o_result.writeCSVrow(simplename,theFile,fileSize,modifiedTIme,accessTime,createdTime,hashValue,ownerID,groupID,mode)
                    return True

        else:
            log.warning("cannot read the file :"+theFile)
            return False
    else:
        log.warning("not a file"+theFile)
        return False















