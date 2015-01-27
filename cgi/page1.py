#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
val1 = form.getvalue('birthday')
val2 = form.getvalue('hobby')
if val1 !=None or val2 !=None:
    print "Content-type:text/html"
    print
    print "The birthday is here: %s<br/> The hobby is %s" %(val1,val2)
else:
    print "Content-type: text/html"



print """

<form method = "post" action ="page2.py">
<textarea name ="name" cols ="40" rows ="5">
Name
</textarea>
<br/>
<textarea name ="family" cols ="40" rows ="5">
Family
</textarea>
<br/>
<input type="submit" value ="Submit">
</form>"""