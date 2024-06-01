from flask import Flask, request, render_template

app = Flask(__name__)

# Store temperature and humidity data
temperature = None
humidity = None

# Update temperature and humidity data
@app.route('/update', methods=['POST'])
def update_data():
    global temperature, humidity
    data = request.get_json()
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    return 'Data updated successfully'

# Serve HTML page with temperature and humidity data
@app.route('/')
def index():
    return render_template('index.html', temperature=temperature, humidity=humidity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)