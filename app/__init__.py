from flask import Flask, render_template, redirect
from .helpers import convert_file_to_dict, save_records
from .forms.form import UploadForm
from .config import Config
from .models import db, Record, LastUpdate
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)



@app.route("/", methods=["GET"])
def index():
    """simple route/app to handle updating data"""
    form = UploadForm()
    data = Record.query.order_by(Record.created_on.desc()).all()

    prev_updates = LastUpdate.query.all()

    if len(prev_updates) >= 2:
        last_date = prev_updates[-2]
        print(last_date)
        new_data = Record.query.filter(Record.created_on >= last_date.last_update).all()
        print(new_data)
        return render_template("index.html", data=data, form=form, new_data=new_data, report_date=str(prev_updates[-1].last_update)[:-8])

    return render_template("index.html", data=data, form=form)


@app.route("/new", methods=["POST"])
def data_submission():
    form = UploadForm()

    if form.validate_on_submit():
 
        data = convert_file_to_dict(form.data['file'])
        saved_records = save_records(data, form.data['date'])

        if saved_records is True:
            return redirect("/")
        else:
            return "<h1>there was an error on file upload</h1>"

    else:
        print(form.errors)
        return render_template("index.html", form=form, errors=form.errors, data=data)
        