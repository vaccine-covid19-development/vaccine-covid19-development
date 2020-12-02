from flask import Flask
app = Flask(__name__)

@app.route('/all_employees')
def all_employees():
    return get_info_all_employes()
    
@app.route('/history')
def get_history():
    return get_history()
 
@app.route('/statuses')
def get_statuses():
    return get_statuses()

@app.route('/give_privileges')
def give_privileges():
    # here we want to get the current mail (i.e. ?mail=some-value)
    user = request.args.get('mail')
    update_privileges(user)
    
   

    
#  Running on http://cpxcyberchallenge.com/Covid19/server/
  
