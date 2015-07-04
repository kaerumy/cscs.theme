## Script (Python) "getCoursesFolderObject"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
obj = container.courses_folder.objectValues()[0]
return obj.aq_parent
