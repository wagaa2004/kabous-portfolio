html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Islam Kabous - إسلام كابوس</title>
<style>
body{margin:0;background:#050a05;color:#0f0;font-family:monospace}
#c{position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;opacity:.12}
.box{max-width:1000px;margin:20px auto;padding:20px;border:1px solid #0f0;background:rgba(0,20,0,.9)}
h1{text-align:center;font-size:55px;text-shadow:0 0 15px #0f0}
h1 span{color:#fff;font-size:32px;display:block}
.card{border:1px dashed #0f0;padding:15px;margin:12px 0}
.badge{border:1px solid #0f0;padding:5px 8px;margin:3px;display:inline-block}
.btn{border:1px solid #0f0;padding:10px 18px;margin:5px;display:inline-block;color:#0f0;text-decoration:none}
</style></head>
<body><canvas id="c"></canvas>
<div class="box">
<h1>Islam Kabous <span>إسلام كابوس</span></h1>
<p style="text-align:center;color:#fff">CYBER SECURITY SPECIALIST • PENETRATION TESTER<br>المنيا - بني مزار - الشيخ فضل | 01101145178</p>
<div class="card"><b>Skills 12:</b><br><br>
<span class="badge">Python 90%</span><span class="badge">Linux/Termux 95%</span><span class="badge">Cyber Security 80%</span><span class="badge">JavaScript 85%</span><span class="badge">HTML/CSS 90%</span><span class="badge">PenTesting 70%</span><span class="badge">Git 85%</span><span class="badge">SQL 75%</span><span class="badge">Crypto 75%</span><span class="badge">Networking 70%</span><span class="badge">Bash 80%</span><span class="badge">API 85%</span>
</div>
<div class="card"><b>Projects 6:</b><br>
1- Kabous Hacker Interface V2<br>
2- BTC Tracker Bot<br>
3- Vuln Scanner<br>
4- Binary Portfolio (هذا الموقع)<br>
5- FB Auto Tools<br>
6- Termux Setup Script
</div>
<div class="card" style="text-align:center">
<a class="btn" href="https://wa.me/201101145178">WhatsApp 01101145178</a>
<a class="btn" href="https://www.facebook.com/share/1EkYRm2Y68/">Facebook</a>
</div>
</div>
<script>
var c=document.getElementById("c"),x=c.getContext("2d");c.width=innerWidth;c.height=innerHeight;
var s="01ISLAMKABOUS",a=c.width/14,b=[];for(var i=0;i<a;i++)b[i]=1;
function d(){x.fillStyle="rgba(5,10,5,.05)";x.fillRect(0,0,c.width,c.height);x.fillStyle="#0f0";x.font="14px monospace";for(var i=0;i<b.length;i++){var t=s[Math.floor(Math.random()*s.length)];x.fillText(t,i*14,b[i]*14);if(b[i]*14>c.height&&Math.random()>.975)b[i]=0;b[i]++}}setInterval(d,35)
</script>
</body></html>
"""
open("index.html","w",encoding="utf-8").write(html)
print("تم بنجاح ✅")
