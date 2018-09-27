from flask import *
from pymongo import MongoClient
import codecs
from model import Image as ModelImage
from PIL import Image

app = Flask(__name__)

import mlab
mlab.connect()

client = MongoClient("mongodb://admin:admin123@ds163382.mlab.com:63382/flaskgrid")
db = client.flaskgrid

@app.route("/", methods=['GET','POST'])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    else:
        image = request.files['image']
        
        new_img = ModelImage(data = image)
        new_img.save()
        return redirect("collection")

@app.route("/collection/")
def collection():
    images = ModelImage.objects.all()
    image_datas = []
    #Get chunks collection
    chunks_col = db['images.chunks']
    for image in images:
        data_id = image.data._id
        chunks = chunks_col.find({ "files_id": data_id})
        image_bytes = ""
        for chunk in chunks:
            base64_data = codecs.encode(chunk["data"], "base64")
            image_bytes += base64_data.decode('utf-8')

        image_datas.append(image_bytes)
    return render_template("detail.html", images = image_datas)

if __name__ == '__main__':
  app.run(debug=True)
 