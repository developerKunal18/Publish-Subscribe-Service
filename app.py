from flask import Flask, request, jsonify

app = Flask(__name__)

# Topics and subscribers
topics = {
    "orders": [],
    "payments": [],
    "notifications": []
}


# ---------- Subscribe ----------
@app.route(
    "/subscribe",
    methods=["POST"]
)
def subscribe():

    data = request.get_json()

    topic = data["topic"]
    subscriber = data["subscriber"]

    if topic not in topics:

        topics[topic] = []

    topics[topic].append(
        subscriber
    )

    return jsonify({
        "message":
        "Subscribed successfully"
    })


# ---------- Publish ----------
@app.route(
    "/publish",
    methods=["POST"]
)
def publish():

    data = request.get_json()

    topic = data["topic"]
    event = data["event"]

    subscribers = topics.get(
        topic,
        []
    )

    return jsonify({
        "topic": topic,
        "event": event,
        "delivered_to": subscribers
    })


# ---------- View Topics ----------
@app.route("/topics")
def get_topics():

    return jsonify(
        topics
    )


# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status":
        "healthy"
    })


if __name__ == "__main__":

    app.run(
        debug=True
    )
