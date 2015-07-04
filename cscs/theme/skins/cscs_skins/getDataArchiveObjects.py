## Script (Python) "getDataArchiveObjects"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=archive_type=None
##title=
##
if not archive_type:
   return []

result = []
items = []
user = context.portal_membership.getAuthenticatedMember()
objs = container.dataarchive[archive_type].objectValues()

for obj in objs:    
    state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
    if user.has_permission('View', obj) and state not in ['archive']:
       if obj.Title():
          title_obj = (obj.Title(), obj)
          items.append(title_obj)

items.sort()

for item in items:
    result.append(item[1])

return result
