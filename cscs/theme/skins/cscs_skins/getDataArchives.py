## Script (Python) "getDataArchives"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=archive=False
##title=
##
result = []
user = context.portal_membership.getAuthenticatedMember()
objs = container.dataarchive.objectValues()

if archive:
   for obj in objs:    
       state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
       if user.has_permission('View', obj) and state in ['archive']:
          result.append(obj)
   return result

else:
   items = []
   for obj in objs:    
       state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
       if user.has_permission('View', obj) and state not in ['archive']:
          title_obj = (obj.Title(), obj)
          items.append(title_obj)
   items.sort()
   for item in items:
       result.append(item[1])

return result
