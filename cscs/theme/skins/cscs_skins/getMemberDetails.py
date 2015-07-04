## Script (Python) "getMemberDetails"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=member='karthick'
##title=
##
mo_dict = {}
mo = context.Members[member]

mo_dict['title'] = mo.Title()
mo_dict['short_description'] = mo.getShortDescription()
mo_dict['full_description'] = mo.getFullDescription()

return mo_dict
