from client import AudioSpeechEmotionSentimentAnalyzerClient

def main():
    client = AudioSpeechEmotionSentimentAnalyzerClient()
    res = client.analyze_audio_emotion("https://cdn.example.com/audio_01.wav", 16000)
    print(f"Detected Emotion: {res['detected_emotion']} (Score: {res['confidence_score']})")

if __name__ == "__main__":
    main()
