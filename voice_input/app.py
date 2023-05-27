from flask import Flask, request, render_template
import wave
import whisper

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/save_sound', methods=['POST'])
def save_sound_route():
    sound = request.files['sound']
    sound.save("sound.wav")
    return "录音已保存"

@app.route('/convert_audio')
def convert_audio():
    # 在这里进行音频转文本的处理，假设已经将转换后的文本保存在变量 text 中
    model = whisper.load_model("base")
    result = model.transcribe("sound.wav")
    text = result["text"]
    return text


# def save_sound(data):
#     print('before change...')
#     with wave.open("sound.wav", "wb") as f:
#         f.setnchannels(1)  # 设置声道数为1
#         f.setsampwidth(2)  # 设置采样宽度为2字节
#         f.setframerate(44100)  # 设置采样率为44100Hz
#         f.writeframes(data)
#     change()

# def change():
#     print('changing...')
#     model = whisper.load_model("base")
#     result = model.transcribe("sound.wav")
#     print(result["text"])
#     print('ok??')


if __name__ == '__main__':
    app.run(debug=True)
    print('hi')
