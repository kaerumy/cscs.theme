## Script (Python) "getAnnouncementsItems"
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
announcements_folder = container.announcements_folder.objectValues()

for announcements in announcements_folder:
    announcements_id = announcements.getId()
    objs = container.announcements_folder[announcements_id].objectValues()
    if archive:
       for obj in objs:    
           state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
           if user.has_permission('View', obj) and state in ['archive']:
              result.append(obj)
    else:
        for obj in objs:    
            state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
            if user.has_permission('View', obj) and state not in ['archive']:
               result.append(obj)
return result
