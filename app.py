from flask import Flask, jsonify, request,render_template
import pandas as pd

app = Flask(__name__)

# Load the sample dataset
df = pd.read_csv('sample_electric_vehicle_data.csv')

# API endpoint to fetch total miles driven
@app.route('/api/total_miles_driven', methods=['GET'])
def get_total_miles_driven():
    report_type = request.args.get('report_type', default='Total Miles Driven', type=str)
    frequency = request.args.get('frequency', default='Daily', type=str)
    start_date = request.args.get('start_date', type=str)
    end_date = request.args.get('end_date', type=str)
    
    # Filter data based on date range
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    
    # Group data based on frequency
    if frequency == 'Weekly':
        filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
        filtered_df = filtered_df.groupby(pd.Grouper(key='Date', freq='W')).sum()
    elif frequency == 'Monthly':
        filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
        filtered_df = filtered_df.groupby(pd.Grouper(key='Date', freq='M')).sum()
    elif frequency == 'Yearly':
        filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
        filtered_df = filtered_df.groupby(pd.Grouper(key='Date', freq='Y')).sum()
    
    total_miles_driven = int(filtered_df['Miles Driven'].sum())
    return jsonify({'total_miles_driven': total_miles_driven})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
