## Script (Python) "getPublicationsItems"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=archive=False, publications_id=None
##title=
##
result = []
user = context.portal_membership.getAuthenticatedMember()
publications_folder = container.publications_folder.objectValues()

if publications_id:
         current_folder = context.getId()
         objs = container.publications_folder[current_folder].objectValues()
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

for publications in publications_folder:
    publications_id = publications.getId()
    objs = container.publications_folder[publications_id].objectValues()
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
