import smtplib, ssl

port = 465  # For SSL
password = 'mwoudrdcyaqdygcc'
from_user = 'sultanovboburbek9998@gmail.com'
to_user = 'alishermakhsetov@gmail.com'

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(from_user, password)
    server.sendmail(from_user, to_user, 'Ne xavar!')
    # TODO: Send email here
