from flask import request, render_template
from . import main
from .. import db

@main.route('/',methods = ['GET', 'POST'])
def Index():
    if request.method == 'POST':
        kwords = request.form['kwords']
        ch = request.form['optradio']
        if len(kwords)==0:
            return render_template('index.html', data=[],tip='Keywords is Null.')
        elif ch=='uscities':
            kws=kwords.split(',')
            if len(kws)<2:
                return render_template('index.html', data=[], tip='Input Format is error,example:city,state')
            else:
                city= '%'+kws[0]+'%'
                state=kws[1]
                sql = 'select concat(lat,",",lng),population,density,ranking,name from uscities_data a left join businesses_data b on a.city=b.city and a.state=b.state where a.city like "%s" and a.state="%s" order by b.stars desc limit 20;' %(city,state)
                dataitems = db.session.execute(sql).fetchall()
                print(dataitems)
                return render_template('index.html',data=dataitems,table='uscities')
        elif ch=='businesses':
            sql = 'select name,address,city,state,stars,review_count,category from businesses_data where name like "%s";' %('%'+kwords+'%')
            dataitems = db.session.execute(sql).fetchall()
            print(dataitems)
            return render_template('index.html', data=dataitems,table='businesses')
    else:
        return render_template('index.html',table='uscities')


