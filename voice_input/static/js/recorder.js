const recordBtn = document.querySelector(".record-btn");
const player = document.querySelector(".audio-player");

if (navigator.mediaDevices.getUserMedia) {
  var chunks = [];
  const constraints = { audio: true };
  navigator.mediaDevices.getUserMedia(constraints).then(
    stream => {
      console.log("授权成功！");

      const mediaRecorder = new MediaRecorder(stream);

      recordBtn.onclick = () => {
        if (mediaRecorder.state === "recording") {
          mediaRecorder.stop();
          recordBtn.textContent = "record";
          console.log("录音结束");
        } else {
          mediaRecorder.start();
          console.log("录音中...");
          recordBtn.textContent = "stop";
        }
        console.log("录音器状态：", mediaRecorder.state);
      };

      mediaRecorder.ondataavailable = e => {
        chunks.push(e.data);
      };

      mediaRecorder.onstop = e => {
        var blob = new Blob(chunks, { type: "audio/ogg; codecs=opus" });
        chunks = [];
        var audioURL = window.URL.createObjectURL(blob);
        player.src = audioURL;

          // 将录音数据发送到服务器保存
          var formData = new FormData();
          formData.append("sound", blob, "sound.wav");
          fetch("/save_sound", {
            method: "POST",
            body: formData
          })
          .then(response => {
            console.log("录音已保存到服务器");
          })
          .catch(error => {
            console.error("保存录音时出错：", error);
          });
              };
            },
            () => {
              console.error("授权失败！");
            }
          );
} else {
  console.error("浏览器不支持 getUserMedia");
}