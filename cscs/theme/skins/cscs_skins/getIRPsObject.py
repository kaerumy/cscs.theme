## Script (Python) "getIRPsObject"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
user = context.portal_membership.getAuthenticatedMember()
objs = context.irps.objectValues()

for obj in objs:    
    state = container.portal_workflow.getInfoFor(obj, 'review_state', None)
    if user.has_permission('View', obj) and state not in ['archive']:
       return obj.aq_parent
