## Script (Python) "delete_this_object"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=obj=None
##title=
##
user = context.portal_membership.getAuthenticatedMember()
if user.has_permission('Delete objects', context):
   parent_url = context.aq_parent.absolute_url()
   context.aq_parent.manage_delObjects(obj)
   context.REQUEST['RESPONSE'].redirect(parent_url)

"""
user = context.portal_membership.getAuthenticatedMember()
per = user.has_permission('Delete objects', context)
comment = '?%s' % per
parent_url = context.portal_url() + comment
context.REQUEST['RESPONSE'].redirect(parent_url)
"""
