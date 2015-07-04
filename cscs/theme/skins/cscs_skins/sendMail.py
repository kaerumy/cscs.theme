## Script (Python) "sendMail"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

to_addr = context.getAdminEmailId()
fullname = request.get('fullname', '')
from_addr = request.get('email', '')
contact = request.get('contact', '')
message = request.get('message', '')
sub = request.get('subject', '')

msg = """
From: %s
To: %s
Subject: %s

FullName - %s
Contact - %s
%s
""" % (from_addr, to_addr, sub, fullname, contact, message)

try:
  container.MailHost.send(msg, to_addr, from_addr, sub)
  print "Your mail has been send successfully to %s" % to_addr
except:
  print "There was some problem in sending mail. Please try again later."
  print msg, to_addr, from_addr, sub

return printed
