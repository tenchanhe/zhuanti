import pyaudio
import wave
import whisper


chunk = 1024                     # 記錄聲音的樣本區塊大小
# 樣本格式，可使用 paFloat32、paInt32、paInt24、paInt16、paInt8、paUInt8、paCustomFormat
sample_format = pyaudio.paInt16
channels = 2                     # 聲道數量
# 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
fs = 44100
seconds = 5                      # 錄音秒數
filename = "oxxostudio.wav"      # 錄音檔名

p = pyaudio.PyAudio()            # 建立 pyaudio 物件

print("start record...")

# 開啟錄音串流
stream = p.open(format=sample_format, channels=channels,
                rate=fs, frames_per_buffer=chunk, input=True)

frames = []                      # 建立聲音串列

for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)          # 將聲音記錄到串列中

stream.stop_stream()             # 停止錄音
stream.close()                   # 關閉串流
p.terminate()

print('end record...')

wf = wave.open(filename, 'wb')   # 開啟聲音記錄檔
wf.setnchannels(channels)        # 設定聲道
wf.setsampwidth(p.get_sample_size(sample_format))  # 設定格式
wf.setframerate(fs)              # 設定取樣頻率
wf.writeframes(b''.join(frames))  # 存檔
wf.close()


model = whisper.load_model("base")
result = model.transcribe("oxxostudio.wav")
print(result["text"])
