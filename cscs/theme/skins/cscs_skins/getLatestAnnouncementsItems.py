## Script (Python) "getLatestAnnouncementsItems"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
result = []
items = []
old_items = []
user = context.portal_membership.getAuthenticatedMember()
now = DateTime().strftime('%Y-%m-%d %H:%M')

announcements = context.portal_catalog.searchResults(portal_type='Announcement')

for obj in announcements:
    obj = obj.getObject()
    try:
      announcement_date = obj.getAnnouncementDate()
      if user.has_permission('View', obj):
         if announcement_date >= now:            
            date_obj = [announcement_date, obj]
            items.append(date_obj)
         else:
            date_obj = [announcement_date, obj]
            old_items.append(date_obj)
    except:
      continue

old_items.sort()
old_items.reverse()
items.sort()
items.extend(old_items)

for item in items:
    result.append(item[1])

return result[:5]
