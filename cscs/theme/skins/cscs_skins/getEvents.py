## Script (Python) "getEvents"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=year=None, month=None, day=None, archive=False
##title=
##
from DateTime import DateTime
 
user = context.portal_membership.getAuthenticatedMember()
events_folder = context.events_folder.objectValues()
result = []
 
try:
  date = str(year) + '/' + str(month) + '/' + str(day)
  date = DateTime(date).strftime('%Y-%m-%d')
except:
  return
 
for events in events_folder:
   events_id = events.getId()
   objs = events.objectValues()
   for obj in objs:
     state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
     try:
       start_date = DateTime(obj.getStartDate()).strftime('%Y-%m-%d')   
       if archive:
          if start_date == date and state in ['archive'] and user.has_permission('View', obj):
             result.append(obj)
       else:
          if start_date == date and state not in ['archive'] and user.has_permission('View', obj):
             result.append(obj)
     except:
       pass 
return result
