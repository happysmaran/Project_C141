from flask import Flask, jsonify, request
import csv

all_articles=[]
with open("shared_data.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]

liked_articles=[]
disliked_articles=[]

app=Flask(__name__)
@app.route("/")

def index():
    return jsonify({
        "data":data,
        "message":"success"
        })

app=Flask(__name__)
@app.route("/get-article")

def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
        })

@app.route("/liked-article", methods=["POST"])

def like():
    article=all_articles[0]
    all_articles=all_movies[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
        }), 201

@app.route("/disliked-article", methods=["POST"])

def dislike():
    article=all_articles[0]
    all_articles=all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        "status":"success"
        }), 201

if __name__ == "__main__":
  app.run()
