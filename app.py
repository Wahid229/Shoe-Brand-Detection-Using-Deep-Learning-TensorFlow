from tkinter import Image
from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import numpy as np

app = Flask(__name__)
model = load_model('model.h5')




@app.route("/")
def uploadpic():
    return render_template('index.html',query2="")


@app.route("/", methods=['POST'])
def predict():
    query2 = request.form['shoes']
    shoename=request.form['Randomname']
    findshoe_url = query2
    findss_path = tf.keras.utils.get_file(shoename, origin=findshoe_url)
    img = tf.keras.utils.load_img(findss_path, target_size=(224,224))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    final_score=round(100 * np.max(score))
    classname=[np.argmax(score)]
    if classname==[0]:
            Brand="Adidas"
    elif classname==[1]:
            Brand="Balenciaga"
    elif classname==[2]:
            Brand="Nike"
    elif classname==[3]:
            Brand="Puma"
    


   
    return render_template('index.html', output1=Brand, output2=final_score)
    
    
if __name__ == "__main__":
    app.run(debug=True)



