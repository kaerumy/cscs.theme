## Script (Python) "addItem"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=allowed_types=None, item=None, list=None
##title=
##
type_dict = {'CSCSEvent' : 'Event', 
             'CSCSEvents' : 'Events', 
             'IRP' : 'Research Program'}

user = context.portal_membership.getAuthenticatedMember()

if not user.has_permission('Add CSCSItem', context):
   return

if item:
   for ctype in allowed_types:
       cid = ctype[0]
       ctitle = ctype[1]
       if ctitle == item:
          url = "createObject?type_name=" + cid
          print "<a class='right_head' href='folder_contents'>Contents</a><span class='right_head'>&nbsp;&nbsp|&nbsp;&nbsp</span>"
          if ctitle in type_dict.keys():
             ctitle = type_dict[ctype[0]]
          print "<a class='right_head' href='" + url + "'>Add ", ctitle, "</a>"

if list:
   print "<a class='right_head' href='folder_contents'>Contents</a><span class='right_head'>&nbsp;&nbsp|&nbsp;&nbsp</span>"
   for ctype in allowed_types:
       cid = ctype[0]
       ctitle = ctype[1]
       if ctitle in list:
          url = "createObject?type_name=" + cid
          if ctitle in type_dict.keys():
             ctitle = type_dict[ctype[0]]
          print "<a class='right_head' href='" + url + "'>Add " + ctitle + "</a>&nbsp;&nbsp|&nbsp;&nbsp"

return printed
