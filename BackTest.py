from flask import (Flask, render_template, request,jsonify,render_template_string)
import requests
import eventlet
import FetchData as fd
from dotenv import load_dotenv
import json
import os
load_dotenv('.env')
app = Flask(__name__)
from flask_cors import CORS
app.config['SECRET_KEY'] = 'secret!'
CORS(app)

@app.route('/')
def hello_world():
    with open('Indicators.json','r') as f:
        Indicators = json.load(f)
        f.close()
    return render_template('home.html',Indicators=Indicators)

@app.route('/send_output/',methods=['GET'])
def send_output():
    name = request.args.get("name")
    print(name)
    output=[]
    output_data=[]
    with open("./Outputs/"+name+'wob.json','r') as f:
        output.append(json.load(f))
        f.close()
    with open("./Outputs/"+name+'wb.json','r') as f:
        output.append(json.load(f))
        f.close()
    name=[name]
    typef=['Without Brokerage','With Brokerage']
    output_data.append({"company_name":name,"Outputs":
    [{"Type":"Without Brokerage","Output":output[0]},{"Type":"With Brokerage","Output":output[1]}]})
    return render_template('output.html',output=output_data)


@app.route('/send_algo', methods=['POST'])
def send_algo():
    x = request.get_json()
    entry_algo = x['entry_algo']
    exit_algo = x['exit_algo']
    stop_loss = x['stop_loss']
    take_profit = x['take_profit']
    quantity = x['quantity']
    start_cash = x['start_cash']
    start_year = x['start_year']
    start_month = x['start_month']
    start_day = x['start_day']
    end_year = x['end_year']
    end_month = x['end_month']
    end_day = x['end_day']
    start_time = x['start_time']
    end_time = x['end_time']
    broker_commission = x['broker_commission']
    company_name = x['stock_name'].split(",")

    output_data=[]
    typef=['Without Brokerage','With Brokerage']
    for name in company_name:
        output=[]
        for i in range(0,2):
            if(i==0):
                open("./Outputs/"+name+'wob.json', 'w').close()
            else:
                open("./Outputs/"+name+'wb.json', 'w').close()
            name = name.strip()
            fd.compute(entry_algo,exit_algo,stop_loss,take_profit,quantity,start_cash,start_year,start_month,start_day,end_year,end_month,end_day,start_time,end_time,str(1.0*i*float(broker_commission)),name)
            if(i==0):
                os.system("python3 ./Scripts/"+name+"wob.py")
                with open("./Outputs/"+name+'wob.json','r') as f:
                    output.append(json.load(f))
                    f.close()
            else:
                os.system("python3 ./Scripts/"+name+"wb.py")
                with open("./Outputs/"+name+'wb.json','r') as f:
                    output.append(json.load(f))
                    f.close()
        output_data.append({"company_name":name,"Outputs":
        [{"Type":"Without Brokerage","Output":output[0]},{"Type":"With Brokerage","Output":output[1]}]})
    # output_data=json.loads(output_data)
    return json.dumps({'success':True,'data':output_data}), 200, {'Content-Type':'application/json'} 



def main():
    app.debug = True
    app.threaded=True
    app.processes=2
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
