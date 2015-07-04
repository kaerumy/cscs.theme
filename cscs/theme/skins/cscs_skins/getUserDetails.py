## Script (Python) "getUserDetails"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=user=None, property=None
##title=
##
if property == 'emailid':
   for member in context.acl_users.getUsers():
       userName = member.getUserName()
       if userName == user:
          memberObject = context.portal_membership.getMemberById(userName)
          email = memberObject.getProperty('email', '-')
          return email
elif property == 'fullname':
   for member in context.acl_users.getUsers():
       userName = member.getUserName()
       if userName == user:
          memberObject = context.portal_membership.getMemberById(userName)
          fullname = memberObject.getProperty('fullname', '-')
          if not fullname:
             fullname = user
          return fullname
   return user
