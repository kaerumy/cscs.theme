## Script (Python) "createDefaultContentForNewMember"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
username = context.portal_membership.getAuthenticatedMember()
try:
   container.Members.invokeFactory(id=username, type_name='CSCSPeople', title='Title comes here', short_description='Short Description comes here', full_description='Full Description comes here')
   uf = container.Members[username]
   uf.manage_setLocalRoles(username, ['Owner','Reviewer'])
except:
   pass
