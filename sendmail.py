import sys
import os
import argparse
import smtplib
from email.encoders import encode_base64
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE

SMTP_URL=""
receiver_list=[]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send Report mail")
    parser.add_argument('--subject', nargs=1, metavar='N', help='Email Main Subject', required=True)
    parser.add_argument('--smtpurl', nargs=1, metavar='N', help='Sender', required=True)
    parser.add_argument('--sender', nargs=1, metavar='N', help='Sender', required=True)
    parser.add_argument('--receiver', nargs=1, metavar='N', help='Receiver', required=True)
    parser.add_argument('--context', nargs='+', metavar='N', help='filepath for context', required=True)
    parser.add_argument('--importance', nargs=1, metavar='N', help='Importance level', required=False)
    parser.add_argument('--attachment', nargs=1, metavar='N', help='attachment file path', required=False)
    args = parser.parse_args()

    SMTP_URL=args.smtpurl[0]

    maintext = ""

    for context in args.context :
        print(context)
        f = open(context, 'r')
        maintext += "".join(f.readlines())
        f.close()
    #print(maintext)

    for recv_file in args.receiver :
        f = open(recv_file, 'r')
        for receiver in "".join(f.readlines()).split('\n') :
            receiver_list.append(receiver)
        f.close()
    #print(receiver_list)

    s = smtplib.SMTP(SMTP_URL)

    msg = MIMEMultipart()
    msg['Subject'] = args.subject[0]
    msg['From'] = args.sender[0]
    msg['To'] = COMMASPACE.join(receiver_list)
    if args.importance != None :
        msg['Importance'] = args.importance[0]
    body = MIMEText("".join(maintext), 'html')
    msg.attach(body)

    if args.attachment != None :
        for files in args.attachment :
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(files, "rb").read())
            encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(files))
            msg.attach(part)

    s.sendmail(args.sender[0], receiver_list, msg.as_string())
    s.quit()