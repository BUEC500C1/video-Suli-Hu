

from flask import Flask, request, render_template, send_file
from multi_thread_worker import MultiThreadWorker
import zipfile
import os

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['userName']
    twtNum = request.form['twtNum']
    processed_text = text
    mtw4 = MultiThreadWorker(2, 10)
    mtw4.add_task(text , twtNum)
    print(processed_text)
    mtw4.start()
    zipFolder = zipfile.ZipFile('videos.zip','w', zipfile.ZIP_DEFLATED)
    for root, directs, files in os.walk('./video'):
        for f in files:
            print(f)
            if str(f) == '.DS_Store':
                continue
            zipFolder.write('./video/' + str(f))
    zipFolder.close()
    print('zip close')
    os.system("rm video/*")
    return send_file('videos.zip', mimetype ='zip', attachment_filename = 'videos.zip', as_attachment=True)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)