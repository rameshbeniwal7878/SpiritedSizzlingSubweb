from flask import Flask, render_template
app = Flask(__name__)

LANGUAGE =[
  {
  'id': 1,
    'title' : 'Python',
     'type' : 'very easy then other language'
   },

  
   {
    'id': 2,
  'title' : 'Java',
  'type' : 'some harder but strong'
   },
  
  {
    'id' : 3,
    'title' : 'C++',
    'type' : 'tuff but same as java'
  }
 ]

@app.route("/")
def hello_world():
  return render_template('home.html', language=LANGUAGE, )

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
