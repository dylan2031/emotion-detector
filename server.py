from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_homepage():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_analysis():
    text_to_analyze = request.args.get("textToAnalyze")

    # Get emotion analysis
    analysis_result = emotion_detector(text_to_analyze)

    # Response part 1
    response = "For the given statement, the system response is"

    # Exclude dominant emotion. It is returned seperately.
    for key, value in analysis_result.items():
        if key != "dominant_emotion":
            response += f" '{key}': {value},"

    # Replace the last comma with a period
    response = response.rstrip(",") + "."

    # Add dominant emotion to response (response part 2)
    response += f" The dominant emotion is {analysis_result['dominant_emotion']}."

    return response

if __name__ == "__main__":
    app.run(debug=True)
