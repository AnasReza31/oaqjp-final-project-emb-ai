"""Flask application for Emotion Detection."""


from flask import Flask, request, render_template
from emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Handle emotion detection requests."""
    text_to_analyze = request.args.get("textToAnalyze")
	
	# Handle blank input BEFORE processing
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    # Handle blank response
    if response is None or response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    output = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
