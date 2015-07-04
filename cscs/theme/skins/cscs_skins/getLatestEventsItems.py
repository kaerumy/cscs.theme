## Script (Python) "getLatestEventsItems"
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

events = context.portal_catalog.searchResults(portal_type='CSCSEvent')

for obj in events:
    obj = obj.getObject()
    try:
      event_date = obj.getStartDate()
      if user.has_permission('View', obj):
         if event_date >= now:            
            date_obj = [event_date, obj]
            items.append(date_obj)
         else:
            date_obj = [event_date, obj]
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
