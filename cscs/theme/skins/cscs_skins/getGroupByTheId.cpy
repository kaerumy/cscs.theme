## Controller Python Script "getGroupByTheId"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=groupname=None
##title=
##
return container.portal_groups.getGroupById(groupname)
