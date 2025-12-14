import webbrowser
import os

file_path = os.path.abspath("sgu_noel.html")
url = f"file://{file_path}"
webbrowser.open(url)
print(f"Đã mở cây thông tại: {url}")