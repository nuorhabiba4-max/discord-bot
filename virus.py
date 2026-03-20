import webbrowser
import time
import os

html_code = """
<!DOCTYPE html>
<html>
<head>
<title>Prank</title>
<script>
let count = 0;

function loopPopup(){
    if(count < 5){
        alert("⚠ Scanning device... Threat detected!");
        count++;
        setTimeout(loopPopup, 800);
    } else {
        alert("😄 Just kidding! This was a harmless prank.");
    }
}
</script>
</head>

<body onload="loopPopup()" style="background:black;color:white;text-align:center;">
<h1>Security Scan</h1>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/3a/Warning_icon.png" width="150">
<p>Running diagnostics...</p>
</body>
</html>
"""

# Save HTML file
with open("prank.html", "w") as f:
    f.write(html_code)

# Open in browser
webbrowser.open("prank.html")
