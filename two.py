from flask import Flask, redirect, url_for, request, render_template
import os

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
	fo = open("kickstart.cfg", "ab+")
	if request.method == 'POST':
	###Display Configuration 
		fo.write("\n# Use graphical install\ngraphical")
		check_value = request.form.to_dict('display-checkbox')
		check_or_uncheck = check_value['display-checkbox']
		if check_or_uncheck =='check':
			print "check"
			first_boot = check_value['first-boot']
			if first_boot == 'Enabled':
				print "enable"
				fo.write("\n# Run the Setup Agent on first boot\nfirstboot --enable")
			elif first_boot == 'Disabled':
				print "disable"
                               	fo.write("\nfirstboot --disable")
			elif first_boot == 'Reconfigure':
				print "reconfigure"
                                fo.write("\n# Run the Setup Agent on first boot\nfirstboot --reconfig")
		elif check_or_uncheck == 'uncheck':
			print "uncheck"	
			fo.write("\n# Run the Setup Agent on first boot\nfirstboot --reconfig\n# Do not configure the X Window System\nskipx")
	return render_template('index.html')
	fo.close()

if __name__ == '__main__':
   app.run(debug = True)

