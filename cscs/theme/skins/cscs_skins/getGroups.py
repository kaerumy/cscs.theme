## Script (Python) "getGroups"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
objs = context.portal_groups.listGroups()
g_list = []

for obj in objs:
    g_id = obj.getId()
    g_title = obj.getGroupName()
    id_title = (g_id, g_title)
    g_list.append(id_title)

return g_list
