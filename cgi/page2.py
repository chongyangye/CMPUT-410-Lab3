#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
val1 = form.getvalue('name')
val2 = form.getvalue('family')
if val1 !=None and val2 !=None:
    print "Content-type:text/html"
    print
    print "My name is: %s<br/> The family is in %s" %(val1,val2)



print """

<form method = "post" action ="page1.py">
<textarea name ="birthday" cols ="40" rows ="5">
birthday...
</textarea>
<br/>
<textarea name ="hobby" cols ="40" rows ="5">
main hobby...
</textarea>
<br/>
<input type="submit" value ="Submit">
</form>"""