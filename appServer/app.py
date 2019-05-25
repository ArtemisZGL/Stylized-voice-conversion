from flask import Flask, request, send_file
import os
import uuid
from segment import Segment
from convertModule import ConvertModule
from flask_cors import CORS
import shutil

app = Flask(__name__)


@app.route('/audios', methods = ['POST'])
def uploadAudio():
    f = request.files["audio"]
    print(f)
    target = request.headers.get("target")
    print(target)

    uuid4 = str(uuid.uuid4())
    filename = uuid4 + '.wav'
    fileLocation = '{}/{}'.format('upload_dir', uuid4)
    os.makedirs(fileLocation)
    filename = os.path.join(fileLocation, filename)
    request.files['audio'].save(filename)

    mySegment = Segment(filename, 'mp3')
    mySegment.beginSegment()
    print("size :" + str(mySegment.getSize()) + "!!!!!")
    cm = ConvertModule(target, fileLocation + '/res/*.wav', mySegment.getSize(), uuid4)
    cm.beginConvert()


    shutil.rmtree(fileLocation + '/res')
    shutil.rmtree(fileLocation + '/chunks')
    return uuid4

@app.route('/audios/<uuid>', methods = ['GET'])
def getAudio(uuid):
    fileLocation = '{}/{}/{}'.format('upload_dir', uuid, uuid + '.wav')
    print(fileLocation)
    ret = send_file(fileLocation)
    
    #os.remove(filename)
    return ret

if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0',port=5000,debug=True)