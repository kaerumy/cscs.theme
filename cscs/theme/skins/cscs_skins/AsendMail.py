## Script (Python) "AsendMail"
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

to_addr = 'karthicksundaram@hotmail.com'
fullname = 'Full Name'
from_addr = 'karthicksundaram@hotmail.com'
contact = '+919845669779'
message = 'Message flows here ...'
sub = 'Subject Flows Here ...'

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
