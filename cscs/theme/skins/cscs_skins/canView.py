## Script (Python) "canView"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=member='karthick'
##title=
##
user = context.portal_membership.getAuthenticatedMember()

try:
  if user.has_permission('View', context.Members[member]):
     return True
except:
  pass

return False
