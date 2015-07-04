## Script (Python) "getAnnouncements"
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
announcements_folder = context.announcements_folder.objectValues()
result = []
 
try:
  date = str(year) + '/' + str(month) + '/' + str(day)
  date = DateTime(date).strftime('%Y-%m-%d')
except:
  return
 
for announcements in announcements_folder:
    announcements_id = announcements.getId()
    objs = context.announcements_folder[announcements_id].objectValues()
    for obj in objs:  
      try:
        state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
        start_date = DateTime(obj.getAnnouncementDate()).strftime('%Y-%m-%d')   
        if archive:
           if start_date == date and state in ['archive'] and user.has_permission('View', obj):
              result.append(obj)
        else:
           if start_date == date and state not in ['archive'] and user.has_permission('View', obj):
              result.append(obj)
      except:
        pass
 
return result
