from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user
from jobplus.forms import CompanyProfileForm
from jobplus.decorators import company_required
from jobplus.models import Company



company = Blueprint("company", __name__, url_prefix="/company")



@company.route("/")
def index():

    return render_template("company/index.html")



@company.route("/admin")
@company_required
def admin():
    return redirect(url_for("company.profile"))



#更新企业信息
@company.route("/admin/profile", methods=['GET', 'POST'])
@company_required
def profile():

    form = CompanyProfileForm(obj=current_user.company)
    if form.validate_on_submit():
        form.update_company(current_user.company)
        return redirect(url_for("company.profile"))
    else:
        return render_template("company/profile.html", form=form)



@company.route("/<company_id>")
def detail(company_id):
    company = Company.query.get_or_404(company_id)
    return render_template("company/company_detail.html", company=company)


        
