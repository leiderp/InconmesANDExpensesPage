from flask import Flask, url_for,redirect, render_template, request
from aplicacion.forms import singupForm, loginForm,regIncomes,regExpenses,verFechas
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user,logout_user,login_required,current_user
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from flask_caching  import Cache
from datetime import date
import json


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="index"
cache = Cache(config={'CACHE_TYPE': 'null'})
cache.init_app(app)
cache.clear()

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
@app.route("/login", methods=["GET","POST"])
@app.route("/registro", methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index():
    from aplicacion.models import Users as us
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    formLogin = loginForm(request.form)
    formSingup = singupForm(request.form)
    if (request.method == "POST" and formLogin.validate_on_submit()):
        email = formLogin.usernameLg.data
        passw = formLogin.passwordLg.data
        user = us.query.filter_by(username=email).first()
        if user is not None:
            if check_password_hash(user.password,passw):
                login_user(user)
                return redirect(url_for('dashboard'))
        formLogin.usernameLg.errors.append("Usuario o contraseña incorrectos")
        return render_template('index.html',form1=formLogin, form2=formSingup)
    elif request.method=="POST" and formSingup.validate_on_submit():
        name = formSingup.name.data
        email = formSingup.username.data
        passw = formSingup.password.data
        is_singup = us.query.filter_by(username=email).first()
        if is_singup is None:
            user = us(name=name,username=email,password=generate_password_hash(passw))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        formSingup.username.errors.append("Usuario ya fue registrado, por favor inicie sesión")
        return render_template('index.html',form1=formLogin, form2=formSingup)
    else:
        return render_template('index.html',form1=formLogin, form2=formSingup)
    #return redirect(url_for('return_string'))
    
    
@login_manager.user_loader
def load_user(user_id):
    from aplicacion.models  import Users as us
    return us.query.get(int(user_id))


@app.route('/dashboard',methods=["GET","POST"])
@login_required
def dashboard():
    from aplicacion.models import Incomes
    from aplicacion.models import Expenses
    form5 = verFechas()
    if request.method=="POST" and form5.validate_on_submit():
        dateNow = form5.dateNow.data
        incomes = Incomes.query.filter_by(userId=current_user.id).filter_by(date=dateNow).all()
        expenses = Expenses.query.filter_by(userId = current_user.id).filter_by(date=dateNow).all()
        dataincomes={}
        dataincomes['income']=[]
        for incoms in incomes:
            dataincomes['income'].append({
                'desc':incoms.description,
                'amount':incoms.amount
            })
        dataexpenses={}
        dataexpenses['expense']=[]
        for expens in expenses:
            dataexpenses['expense'].append({
                'desc':expens.description,
                'amount':expens.amount
            })    
        with open(app.root_path+"/static/img/income"+str(current_user.id)+".json",'w') as file:
            json.dump(dataincomes, file, indent=4)
        
        with open(app.root_path+"/static/img/expense"+str(current_user.id)+".json",'w') as file:
            json.dump(dataexpenses, file, indent=4)
        return render_template('dashboard.html',incomes=incomes,expenses=expenses,user=current_user.name,activ=0,usid=current_user.id,form5=form5)
    incomes = Incomes.query.filter_by(userId=current_user.id).filter_by(date=date.today()).all()#Incomes.query.all()
    expenses = Expenses.query.filter_by(userId = current_user.id).filter_by(date=date.today()).all()
    dataincomes={}
    dataincomes['income']=[]
    for incoms in incomes:
        dataincomes['income'].append({
            'desc':incoms.description,
            'amount':incoms.amount
        })
    dataexpenses={}
    dataexpenses['expense']=[]
    for expens in expenses:
        dataexpenses['expense'].append({
            'desc':expens.description,
            'amount':expens.amount
        })    
    with open(app.root_path+"/static/img/income"+str(current_user.id)+".json",'w') as file:
        json.dump(dataincomes, file, indent=4)
    
    with open(app.root_path+"/static/img/expense"+str(current_user.id)+".json",'w') as file:
        json.dump(dataexpenses, file, indent=4)
    return render_template('dashboard.html',incomes=incomes,expenses=expenses,user=current_user.name,activ=0,usid=current_user.id,form5=form5)


@app.route('/dashboard/incomes',methods=["GET","POST"])
@login_required
def dashboard_incomes():
    form3 = regIncomes()
    if (request.method == "POST" and form3.validate_on_submit()):
        from aplicacion.models import Incomes
        dateInc=form3.dateIncome.data
        descInc = form3.descrip.data
        amountInc = form3.amount.data
        userid= current_user.id
        income = Incomes(date=dateInc,description=descInc,amount=amountInc,userId=userid)
        db.session.add(income)
        db.session.commit()
        return redirect(url_for('dashboard'))
    else:
        return render_template('addIncomes.html',form3=form3,activ=1)

@app.route('/dashboard/expenses',methods=["GET","POST"])
@login_required
def dashboard_expenses(activ=3):
    form4 = regExpenses(request.form)
    if(request.method == "POST" and form4.validate_on_submit()):
        from aplicacion.models import Expenses
        dateExp=form4.dateEx.data
        descExp = form4.descripEx.data
        amountExp = form4.amountEx.data
        userid= current_user.id
        expense=Expenses(date=dateExp,description=descExp,amount=amountExp,userId=userid)
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('addExpenses.html',form4=form4,activ=2)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
#if __name__== "__main__":
#    app.run(debug=True)
    