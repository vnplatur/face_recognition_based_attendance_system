import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "dymmy27@gmail.com"
APP_PASSWORD = "wnkncgxdhyfparuh"


print("Mail Start")
msg = EmailMessage()
msg['Subject'] = "Student Face Attendance Using Image Processing"
msg['From'] = SENDER_EMAIL
msg['To'] = "workdaily23@gmail.com"
msg.set_content('Todays Student Face Attendance Xls sheet is attached Please find attachment')

with open('D:/face attendance with database/attendace_sheet.xlsx', 'rb') as f:
        file_data = f.read()
msg.add_attachment(file_data, maintype="application", subtype="vnd.ms-excel", filename='D:/face attendance with database/attendace_sheet.xlsx')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        print("Mail send successfully")
