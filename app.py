from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ดีกันนะ</title>

<style>
body{
    font-family: Arial, sans-serif;
    text-align: center;
    padding: 30px;
    background: linear-gradient(180deg, #fff0f5, #ffffff);
    overflow-x: hidden;
}
h1, h2{
    color: #e75480;
}
button{
    font-size: 18px;
    padding: 12px 28px;
    margin: 10px;
    border: none;
    border-radius: 30px;
    background-color: #ff8fab;
    color: white;
    cursor: pointer;
}
button:hover{
    background-color: #ff5d8f;
}

/* หัวใจลอย */
.heart{
    position: fixed;
    bottom: 0;
    font-size: 24px;
    animation: floatUp 3s ease-in forwards;
    pointer-events: none;
}
@keyframes floatUp{
    0%{ transform: translateY(0) scale(1); opacity: 1; }
    100%{ transform: translateY(-600px) scale(1.8); opacity: 0; }
}

#musicPage{ display:none; }
iframe{
    width: 100%;
    max-width: 560px;
    height: 315px;
    border-radius: 20px;
}
</style>

<script>
let noCount = 0;

function createHeart(){
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "💖";
    heart.style.left = Math.random() * window.innerWidth + "px";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 3000);
}

function hideAll(){
    ["scene1","scene2","scene3","musicPage"].forEach(id=>{
        document.getElementById(id).style.display="none";
    });
}

function goToMusic(){
    hideAll();
    document.getElementById("musicPage").style.display="block";
}

function backFromMusic(){
    hideAll();
    document.getElementById("scene1").style.display="block";
}

function agree(){
    for(let i=0;i<8;i++){
        setTimeout(createHeart,i*150);
    }
    hideAll();
    document.getElementById("scene3").style.display="block";
}

function disagree(){
    noCount++;
    if(noCount === 1){
        hideAll();
        document.getElementById("scene2").style.display="block";
    }
}

function moveButton(btn){
    btn.style.position="absolute";
    btn.style.left=Math.random()*(window.innerWidth-120)+"px";
    btn.style.top=Math.random()*(window.innerHeight-120)+"px";
}

function finish(){
    for(let i=0;i<12;i++){
        setTimeout(createHeart,i*120);
    }
    alert("เค้าสัญญาว่าจะดูแลหัวใจพี่ให้ดีที่สุดนะ 💞");
}
</script>
</head>

<body>

<!-- หน้าแรก -->
<div id="scene1">
    <h1>ดีกันนะคนดี 🤍</h1>
    <p>
        ถ้าวันไหนเค้าทำให้พี่เหนื่อย<br>
        เค้าขอโทษจากใจจริง
    </p>
    <button onclick="goToMusic()">🎵 เค้าอยากให้พี่ได้ฟังนะ</button><br>
    <button onclick="agree()">ตกลง</button>
    <button onclick="disagree()">ไม่ตกลง</button>
</div>

<!-- ขออีกรอบ -->
<div id="scene2" style="display:none;">
    <h2>ขอโอกาสเค้าอีกครั้งได้ไหม 🥺</h2>
    <p>เค้าไม่อยากเสียพี่ไปจริง ๆ</p>
    <button onclick="agree()">ตกลง</button>
    <button onmouseover="moveButton(this)" ontouchstart="moveButton(this)">
        ไม่ตกลง
    </button>
</div>

<!-- สำเร็จ -->
<div id="scene3" style="display:none;">
    <h2>ขอบคุณที่เลือกเค้า 💖</h2>
    <p>
        ต่อจากนี้เค้าจะฟังพี่มากขึ้น<br>
        และรักพี่ให้ดีที่สุด 💗
    </p>
    <button onclick="goToMusic()">🎵 ฟังเพลงนี้นะ</button><br><br>
    <button onclick="finish()">ตกลง</button>
    <button onclick="finish()">ตกลง</button>
</div>

<!-- หน้าเพลง -->
<div id="musicPage">
    <h2>เพลงนี้จากใจเค้า 🎶</h2>
    <iframe
        src="https://www.youtube.com/embed/eoG6vj-DyS4"
        allowfullscreen>
    </iframe><br><br>
    <button onclick="backFromMusic()">⬅ กลับไปอ่านข้อความ</button>
</div>

</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

