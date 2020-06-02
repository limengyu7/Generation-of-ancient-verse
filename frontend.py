# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:24:10 2020

@author: 王晶
"""
from flask import Flask,render_template,request

print('------------------------------ok')
app = Flask(__name__)
@app.route('/frontend',methods=['GET','POST'])
def frontend():
    if request.method == 'POST':
        recv_data = request.form.get('kw')
        if recv_data:
            print(recv_data['value'])
        else:
            print("---输入为空----")
        output = '床头明月光，疑是地上霜'
    return render_template('frontend.html',useroutput=output);
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',#任何ip都可以访问
            port=7777,#端口
            debug=True,
            use_reloader=False
            )
