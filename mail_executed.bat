@ECHO OFF
ECHO Hello world
set BASE_PATH=%~dp0
pushd %BASE_PATH%
set /p MAIL_TITLE=< %BASE_PATH%settings\��������.txt
set /p SMTP_URL=< %BASE_PATH%settings\�����ּ�.txt
set /p SENDER=< %BASE_PATH%settings\���Ϲ߽���.txt
Python %BASE_PATH%sendmail.py --subject "%MAIL_TITLE%" --smtpurl "%SMTP_URL%" --sender "%SENDER%" --receiver "%BASE_PATH%settings\���ϼ�����.txt" --context "%BASE_PATH%message_header.html" "%BASE_PATH%\settings\message_body.html" "%BASE_PATH%message_footer.html"
PAUSE