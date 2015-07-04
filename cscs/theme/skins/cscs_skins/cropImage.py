## Script (Python) "cropImage"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=img=None
##title=
##
try:
   if img:
     img_list = str(img).split(' ')
     img_height = int(img_list[-3].replace('"', '').replace('=', '').replace('height', ''))
     img_width = int(img_list[-2].replace('"', '').replace('=', '').replace('width', ''))
     if img_width >= img_height:
        height = 100*(img_height/float(img_width))
        width = 100
     else:
        width = 100*(img_width/float(img_height))
        height = 100
     img_list[-3] = 'height="%d"' % height
     img_list[-2] = 'width="%d"' % width
     return ' '.join(img_list)
except:
   img
