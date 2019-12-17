from flask import Flask, render_template, request, url_for, redirect
import pysolr
import json
from pyvi import ViTokenizer

import gensim


# from app import app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/content/<id>', methods=['POST', 'GET'])
def show_content(id):
    solr = pysolr.Solr(
        'http://localhost:8983/solr/tktdtt', always_commit=True)

    results = solr.search('id:{}'.format(id))
    print(results.docs[0])
    report_template = render_template(
        'content-result.html', title=results.docs[0]['title'][0],
        url=results.docs[0]['url'][0],
        description=results.docs[0]['description'][0],
        content=results.docs[0]['content'][0],
        id=results.docs[0]['id'])

    return report_template


@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        solr = pysolr.Solr(
            'http://localhost:8983/solr/tktdtt', always_commit=True)

        if 'topic_btn' in request.form:

            topic = request.form['topic_btn']

            key = "topic : " + topic

            results = solr.search(key)
            print(key)
            print(results.docs[0])
        elif 'text-search' in request.form:

            text_search = request.form['text-search']

            # tìm kiếm các bài có chứa 1 từ trong câu nhập vào, nhập vào 1 từ , tìm kiếm trong description
            def searchDescription1(sentence):

                key = "description : " + sentence

                results = solr.search(key)

                return results

            # tat ca cac ket qua la  results
            results = searchDescription1(text_search)

        report_template = render_template(
            'result.html', title=[results.docs[i]['title'][0] for i in range(0, 10)],
            url=[results.docs[i]['url'][0] for i in range(0, 10)],
            description=[results.docs[i]['description'][0]
                         for i in range(0, 10)],
            content=[results.docs[0]['content'][0] for i in range(0, 10)],
            id=[results.docs[0]['id'] for i in range(0, 10)])

        return report_template

    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
