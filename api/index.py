from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>API Server Updated</title>

<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}
body{
    background:#0f172a;
    color:#fff;
    display:flex;
    justify-content:center;
    align-items:center;
    min-height:100vh;
    padding:20px;
}
.card{
    max-width:760px;
    width:100%;
    background:#111827;
    border-radius:20px;
    padding:40px;
    border:1px solid rgba(255,255,255,.08);
    box-shadow:0 20px 50px rgba(0,0,0,.4);
}
h1{font-size:34px;margin-bottom:15px}
.subtitle{color:#cbd5e1;line-height:1.7;margin-bottom:30px}
.section{margin-top:25px}
.section h2{color:#38bdf8;margin-bottom:10px}
.section p{line-height:1.8;color:#e5e7eb}
.btn{
display:block;
margin-top:35px;
text-align:center;
background:#229ED9;
color:#fff;
padding:16px;
text-decoration:none;
border-radius:10px;
font-weight:bold;
}
.btn small{display:block;margin-top:5px}
.footer{
margin-top:25px;
text-align:center;
color:#94a3b8;
font-size:14px;
}
</style>
</head>
<body>

<div class="card">

<h1>🚨 API Server Updated</h1>

<p class="subtitle">
Our API infrastructure has been updated. Please obtain the latest API credentials to continue using our services without interruption.
</p>

<div class="section">
<h2>🇬🇧 English</h2>
<p>
The API server has been changed.<br><br>
Please DM <strong>@RichAllOver</strong> to get the new API credentials.<br><br>
Update your integration as soon as possible to avoid any service interruption.
</p>
</div>

<div class="section">
<h2>🇮🇳 हिंदी</h2>
<p>
API सर्वर बदल दिया गया है।<br><br>
नई API प्राप्त करने के लिए <strong>@RichAllOver</strong> को DM करें।<br><br>
किसी भी सेवा में रुकावट से बचने के लिए कृपया जल्द से जल्द अपनी API अपडेट करें।
</p>
</div>

<a class="btn" href="https://t.me/RichAllOver">
📩 Click Here to Contact Support
<small>नई API प्राप्त करने के लिए इस बटन पर क्लिक करें</small>
</a>

<div class="footer">
© 2026 All Rights Reserved
</div>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/api")
def api():
    return render_template_string(HTML)

# Vercel
app = app
