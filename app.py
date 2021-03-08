from flask import Flask

app = Flask("myapp")

@app.route("/")
def home():
    print(" This is print fn...")
    return("""
		<body bgcolor=aqua >
	    	<h1>  <marquee>  Welcome in Python Programming world - Full Stack Development using Flask training by Vimal Sir .. </marquee> </h1>
		</body>

	 """)
