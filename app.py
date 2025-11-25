from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get the text input from the form
    user_text = request.form.get('user_text', '')
    
    # You can use different images based on the text
    # For this example, we'll use a static image
    image_url = "/static/images/sample.jpg"  # Make sure this image exists
    
    return render_template('result.html', 
                         user_text=user_text, 
                         image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)