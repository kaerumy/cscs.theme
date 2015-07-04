## Script (Python) "getAdminEmailId"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
admin_id = 'karthicksundaram@hotmail.com'
'''
for obj in context.others.objectValues():
    if obj.getId() == 'admin_email_id':
       admin_id = obj.short_description
'''
print admin_id
return printed
