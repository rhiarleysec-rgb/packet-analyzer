def save_log(log):
    with open("report.html", "w") as f:
        f.write("<html><body style='background:#111;color:#0f0;font-family:monospace'>")
        f.write("<h2>Packet Analyzer Report</h2><ul>")
        for line in log:
            color = "red" if "PORT SCAN" in line else "lime"
            f.write(f"<li style='color:{color}'>{line}</li>")
        f.write("</ul></body></html>")