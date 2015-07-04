## Script (Python) "getCalendarItems"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cur_date=None
##title=
##
from DateTime import DateTime

result = [] 
user = context.portal_membership.getAuthenticatedMember()
try:
  cur_date = DateTime(cur_date).strftime('%Y/%m/%d')
except:
  return result

announcements = context.portal_catalog.searchResults(portal_type='Announcement')
events = context.portal_catalog.searchResults(portal_type='CSCSEvent')

for obj in announcements:
    obj = obj.getObject()
    try:
      start_date = DateTime(str(obj.getAnnouncementDate())[:10]).strftime('%Y/%m/%d')
      if start_date == cur_date and user.has_permission('View', obj):
         result.append(obj)
    except:
      continue

for obj in events:
    obj = obj.getObject()
    try:
      start_date = DateTime(str(obj.getStartDate())[:10]).strftime('%Y/%m/%d')
      if start_date == cur_date and user.has_permission('View', obj):
         result.append(obj)
    except:
      continue

return result
