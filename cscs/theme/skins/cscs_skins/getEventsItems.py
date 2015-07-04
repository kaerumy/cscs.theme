## Script (Python) "getEventsItems"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=events_name=None, archive=False
##title=
##
if not events_name:
   return result

result = []
user = context.portal_membership.getAuthenticatedMember()
events_folder = container.events_folder.get(events_name).objectValues()

if archive:
   for obj in events_folder:
       state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
       if user.has_permission('View', obj) and state in ['archive']:
          result.append(obj)
else:
   items = []
   for obj in events_folder:
       state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
       if user.has_permission('View', obj) and state not in ['archive']:
          title_obj = (obj.Title(), obj)
          items.append(title_obj)
   items.sort()
   for item in items:
       result.append(item[1])

return result
