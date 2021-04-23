from app.api_1_0 import api
from flask import current_app,jsonify,url_for,redirect,send_from_directory,request,render_template
from werkzeug.utils import secure_filename
from app.models.rollingdata import InnocationCenter
import os
import uuid
from app.utils.filedeal import allowed_file
from app import db
from app.viewmodels.rollingdata import InnovationCenterTableView


#查看上传的文件
@api.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],
                               filename)

#返回文件路径
@api.route('/entityimage/<entityname>')
def entity_image(entityname):
    dataquery=InnocationCenter.query.filter_by(name=entityname).first()
    imagename=dataquery.image_url
    if imagename is None:
        return ''
    else:
        url=url_for('api_1_0.uploaded_file',filename=imagename)
        return url

#上传图片
@api.route('/image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        print(request.files)
        file = request.files.get('file')
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = uuid.uuid4().hex+'_'+secure_filename(file.filename)
            Uploadfolder = current_app.config['UPLOAD_FOLDER']
            filestore = os.path.join('app', Uploadfolder, filename)
            file.save(filestore)
            # resp = jsonify({'message': 'File successfully uploaded','filename':filename})
            # resp.status_code = 201
            return filename

    return '''<!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@api.route('/entities/',defaults={'page':1},methods=['GET', 'POST'])
@api.route('/entities/<int:page>/',methods=['GET', 'POST'])
def entitiescheck(page):
    # pagination = Member.query.paginate(page, per_page=30, error_out=False)
    # members=pagination.items
    # return render_template('memberslist.html', pagination=pagination, members=members)
    pagination = InnocationCenter.query.paginate(page, per_page=50)
    view=InnovationCenterTableView(pagination.items)
    # citems = pagination.items


    # if request.method == 'POST':
    #
    #     elif request.form.get('submit'):
    #         company=request.form.get('company')
    #         # branch = request.form.get('branch')
    #         text = request.form.get('text')
    #         searchcom = "%{}%".format(text)
    #         confirmsts =  request.form.get('confirm')
    #         if confirmsts=='all' and company!='all':
    #             pagination = Member.query.filter(Member.company==company,or_(Member.name.like(searchcom),Member.branch.like(searchcom))).paginate(page, per_page=10)
    #             members = pagination.items
    #             # return render_template('memberslist.html', members=members, pagination=pagination)
    #         elif confirmsts!='all' and company=='all':
    #             pagination = Member.query.filter(Member.confirmed == confirmsts,
    #                                              or_(Member.name.like(searchcom),
    #                                                  Member.branch.like(
    #                                                      searchcom))).paginate(page,
    #                                                                            per_page=10)
    #             members = pagination.items
    #             # return render_template('memberslist.html', members=members, pagination=pagination)
    #         elif confirmsts=='all' and company=='all':
    #             pagination = Member.query.paginate(page, per_page=10)
    #             members = pagination.items
    #         else:
    #             pagination = Member.query.filter(Member.company == company,Member.confirmed==confirmsts, or_(Member.name.like(searchcom),
    #                                                                             Member.branch.like(
    #                                                                                 searchcom))).paginate(page,
    #                                                                                                       per_page=10)
    #             members = pagination.items
    #         return render_template('memberslist.html', members=members, pagination=pagination)
    #
    #     elif request.form.get('clear'):
    #         return redirect(url_for('api_1_0.membercheck', page=page))
    return render_template('datamanage.html', citems=view.items,pagination=pagination)

