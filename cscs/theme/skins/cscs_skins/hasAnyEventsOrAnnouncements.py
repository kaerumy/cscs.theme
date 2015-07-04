## Script (Python) "hasAnyEventsOrAnnouncements"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=year=None, month=None, day=None
##title=
##
from DateTime import DateTime

user = context.portal_membership.getAuthenticatedMember()
 
days = []
try:
     cur_date = str(year) + '/' + str(month) + '/' + str(day)
     cur_date = DateTime(cur_date).strftime('%Y-%m')
except:
     pass

events = context.portal_catalog.searchResults(portal_type='CSCSEvent')
for obj in events:
    obj = obj.getObject()
    try:
        get_start_date = str(obj.getStartDate())
        start_date = DateTime(get_start_date[:10]).strftime('%Y-%m')
        if start_date == cur_date and user.has_permission('View', obj):
           daynumber = int(get_start_date[8:10])
           if daynumber not in days:
              days.append(daynumber)
    except:
        continue
    
announcements = context.portal_catalog.searchResults(portal_type='Announcement')
for obj in announcements:
    obj = obj.getObject()
    try:
        get_announcement_date = str(obj.getAnnouncementDate())
        announcement_date = DateTime(get_announcement_date[:10]).strftime('%Y-%m')
        if announcement_date == cur_date and user.has_permission('View', obj):
           daynumber = int(get_announcement_date[8:10])
           if daynumber not in days:
              days.append(daynumber)
    except:
        continue

days.sort()
return days
