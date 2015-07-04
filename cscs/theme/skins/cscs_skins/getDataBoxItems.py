## Script (Python) "getDataBoxItems"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=archive=False
##title=
##
result = []
items = []
user = context.portal_membership.getAuthenticatedMember()
objs = container.databoxes.objectValues()

if archive:
   for obj in objs:    
       state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
       if user.has_permission('View', obj) and state in ['archive']:
          created_date = obj.modified
          date_obj = [created_date, obj]
          items.append(date_obj)
else:
   for obj in objs:    
       state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
       if user.has_permission('View', obj) and state not in ['archive']:
          created_date = obj.modified
          date_obj = [created_date, obj]
          items.append(date_obj)

items.sort()
items.reverse()

result = []
for item in items:
    result.append(item[1])

return result
