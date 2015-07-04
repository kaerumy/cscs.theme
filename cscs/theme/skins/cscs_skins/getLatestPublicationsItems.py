## Script (Python) "getLatestPublicationsItems"
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
publications_folder = container.publications_folder.objectValues()

if archive:
   for publications in publications_folder:    
       objs = container.publications_folder[publications.getId()].objectValues()
       for obj in objs:    
         state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
         publication_date = obj.created
         if user.has_permission('View', obj) and state in ['archive']:            
            date_obj = [publication_date, obj]
            items.append(date_obj)
else:
   for publications in publications_folder:    
       objs = container.publications_folder[publications.getId()].objectValues()
       for obj in objs:    
         state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
         publication_date = obj.created
         if user.has_permission('View', obj) and state not in ['archive']:
            date_obj = [publication_date, obj]
            items.append(date_obj)

items.sort()

result = []
for item in items:
    result.append(item[1])

return result[:5]
