## Script (Python) "getGroupUsers"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=gid=None
##title=
##
for obj in context.portal_groups.listGroups():
    if obj.getId() == gid:
       return obj.getGroupMembers()
