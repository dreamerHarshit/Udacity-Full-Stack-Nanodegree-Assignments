import webapp2
import cgi

rot13_form="""
<form method="post">
<br>
<div align=left>
<font size="5"><b>ROT13 Homework:</b></font>
<br>
<input type="text" name="textarea">
<button>Add</button>
</form>"""

class Rot13(webapp2.RequestHandler):
	def escape_html(self, s):
		return cgi.escape(s, quote = True)

	def trans(self, str_in):
		i = 0
		listtt = list(str_in)

		for x in listtt:
			x = ord(x)
			if x>=65 and x<=77:
				listtt[i] = x+13
			elif x>=78 and x<=90:
				listtt[i] = x-13
			elif x>=97 and x<=109:
				listtt[i] = x+13
			elif x>=110 and x<=122:
				listtt[i] = x-13
			else :
				listtt[i] = x
			i=i+1

		i=0
		for x in listtt:
			x = chr(x)
			listtt[i] = x
			i = i + 1
		str_in = ''.join(listtt)

		return str_in


	def write_form(self, f=""):
		self.response.out.write(rot13_form % {"fill": f})

	def get(self):
		self.write_form()

	def post(self):
		text_trans = self.request.get('text')

		if text_trans:
			text_trans = self.trans(text_trans)
			text_trans = self.escape_html(text_trans)
			self.write_form(text_trans)

		else:
			self.response.out.write("Please input the text")

