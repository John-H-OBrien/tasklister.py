#!/usr/bin/python

# import pyPdf
import os
import smtplib



def merge_pdfs():
    #Searches directory for PDFs and combines them
    startDir = "/~/code/python"
    os.chdir(startDir)

    fileList = os.listdir(startDir)
    output = pyPdf.PdfFileWriter()

    for item in fileList:
        if os.path.splitext(item)[1].upper() == ".PDF":
            pdfDocument = os.path.join(startDir,item)
            input1 = pyPdf.PdfFileReader(file(pdfDocument, "rb"))
        for page in range(input1.getNumPages()):
            output.addPage(input1.getPage(page))

    outputStream = file("TLTestCombined.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

# This is an email utilitiy grabbed from the internet.
# I need to pull in information from pipe_utils on email process for our network.

import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
def send_mail(send_from , send_to, subject, text, files=[], server="localhost"):
    assert type(send_to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()



# This secion was heavily influenced by Brandon. 
# He explained a lot of really good concepts and designs to me.

import glob
import os
# Find the last modified dir.


 
def find_latest_dir(base):
    result = None
    if os.path.exists(base): 
        all_files = glob.glob(os.path.join(base, '*'))
        dirs = []
        for tmp in all_files:
            if os.path.isdir(tmp):
                dirs.append(tmp)

        if dirs:
            # Using a lambda (function created on the fly)
            # to get me the modified time. Reversing it to get the latest dir
            sorted_dirs = sorted(dirs, key=lambda x: os.stat(x).st_mtime, reverse=True)

            result = sorted_dirs[0]

    return result

latest_dir = find_latest_dir('P:\comm_PA\Task Lists\August\') 
print latest_dir
print "test"





