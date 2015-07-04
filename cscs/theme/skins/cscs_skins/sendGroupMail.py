## Script (Python) "sendGroupMail"
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

from_addr = request.get('email', '')
sub = request.get('subject', '')

fullname = request.get('fullname', '')
email = request.get('email', '')
contact = request.get('contact', '')
message = request.get('message', '')
groups = request.get('groups', [])

to_list = []
for group in groups:
    users = container.getGroupUsers(gid = group)
    if users:
       for user in users:
           try:
              mail_id = container.portal_membership.getMemberById(str(user)).getProperty('email', None)
              if mail_id:
                 to_list.append(mail_id)
           except:
              pass

if not fullname:
   print "Please enter the full name"
   return printed
if not email:
   print "Please enter the email id"
   return printed
if not contact:
   print "Please enter the contact number"
   return printed
if not message:
   print "Please enter the message"
   return printed
if len(to_list) == 0:
   print "No Groups has been selected or No users under the selected group. Please re-select the group name(s)"
   return printed

err_list = []
sent_list = []

#from_addr = fullname + '<' + from_addr + '>'

for to_addr in to_list:
    msg = """
    From: %s
    To: %s
     %s

    Full Name - %s
    Email - %s
    Contact Number - %s
    Message - %s""" % (from_addr, to_addr, sub, fullname, email, contact, message)

    try:
      container.MailHost.send(msg, to_addr, from_addr, sub)
      sent_list.append(to_addr)
    except:      
      err_list.append(to_addr)

if len(sent_list) > 0:
   print "<b>Mail has been sent to following members succesfully</b>"
   for item in sent_list:
       print '<br/>', item

if len(err_list) > 0:
   print "<b>There was some problem in sending mail to following members. Please try again later.</b><br/>"
   for item in err_list:
       print '<br/>', item

return printed
