from flask import Flask, render_template_string, jsonify, send_from_directory
import subprocess
import os
import threading

app = Flask(__name__)

# Đường dẫn tới các file ứng dụng
CAESAR_APP = r"c:\Users\ntrkh\Desktop\bmtt\bmtt-nc-hutech-2280601572\lab-03\caesar_cipher.py"
PLAYFAIR_APP = r"c:\Users\ntrkh\Desktop\bmtt\bmtt-nc-hutech-2280601572\lab-03\playfair_cipher.py"
RSA_APP = r"c:\Users\ntrkh\Desktop\bmtt\bmtt-nc-hutech-2280601572\lab-03\rsa_cipher.py"
RAILFENCE_APP = r"c:\Users\ntrkh\Desktop\bmtt\bmtt-nc-hutech-2280601572\lab-03\railfence_cipher.py"
VIGENERE_APP = r"c:\Users\ntrkh\Desktop\bmtt\bmtt-nc-hutech-2280601572\lab-03\vigenere_cipher.py"

@app.route('/tinhiuhutech.img')
def serve_image():
    """Serve the tinhiuhutech.img file"""
    image_path = r"c:\Users\ntrkh\Desktop\bmtt\bmtt-nc-hutech-2280601572\lab-02\ex02\templates\test"
    return send_from_directory(image_path, 'tinhiuhutech.img')

def run_app(app_path):
    """Chạy ứng dụng PyQt5 trong thread riêng"""
    try:
        subprocess.Popen(['python', app_path])
        return True
    except Exception as e:
        print(f"Error running app: {e}")
        return False

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Thực hành An toàn thông tin nâng cao</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    <style>
        .cipher-link {
            font-size: 18px;
            text-decoration: none;
            color: #007bff;
            padding: 10px 15px;
            border-radius: 5px;
            transition: all 0.3s ease;
            display: inline-block;
            margin: 5px 0;
        }
        
        .cipher-link:hover {
            background-color: #f8f9fa;
            text-decoration: none;
            color: #0056b3;
        }
        
        .status {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            display: none;
        }

        .status.success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }

        .status.error {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        
        li {
            margin: 15px 0;
        }    </style>
</head>
<body>
    <div class="container">
        <img src="https://file1.hutech.edu.vn/file/editor/homepage/stories/hinh34/logo%20CMYK-01.png" alt="hutech" style="display: block; margin-left: auto; margin-right: auto; width: 30%;"/>
        <img src="tinhiuhutech.img" alt="tinh iu hutech" style="display: block; margin-left: auto; margin-right: auto; width: 20%; margin-top: 10px;"/>
        <h4 style="font-weight: bold; text-align: center;">BÀI THỰC HÀNH BẢO MẬT THÔNG TIN NÂNG CAO - Nguyễn Trọng Khôi-2280601572</h4>
        
        <ul style="margin-top: 30px;">
            <li><a href="#" class="cipher-link" onclick="launchApp('caesar')">Caesar Cipher</a></li>
            <li><a href="#" class="cipher-link" onclick="launchApp('playfair')">Playfair Cipher</a></li>
            <li><a href="#" class="cipher-link" onclick="launchApp('railfence')">Railfence Cipher</a></li>
            <li><a href="#" class="cipher-link" onclick="launchApp('vigenere')">Vigenere Cipher</a></li>
            <li><a href="#" class="cipher-link" onclick="launchApp('rsa')">RSA Cipher</a></li>
        </ul>
        
        <div id="status" class="status"></div>
    </div>
    
    <script>
        async function launchApp(appType) {
            const statusDiv = document.getElementById('status');
            statusDiv.style.display = 'block';
            statusDiv.className = 'status';
            statusDiv.textContent = 'Đang khởi chạy ứng dụng...';
            
            try {
                const response = await fetch(`/launch/${appType}`, {
                    method: 'POST'
                });
                
                const result = await response.json();
                
                if (result.success) {
                    statusDiv.className = 'status success';
                    statusDiv.textContent = `Ứng dụng ${appType.toUpperCase()} đã được khởi chạy thành công!`;
                } else {
                    statusDiv.className = 'status error';
                    statusDiv.textContent = `Lỗi: ${result.message}`;
                }
            } catch (error) {
                statusDiv.className = 'status error';
                statusDiv.textContent = 'Lỗi kết nối đến server!';
            }
            
            // Ẩn thông báo sau 3 giây
            setTimeout(() => {
                statusDiv.style.display = 'none';
            }, 3000);
        }
    </script>
</body>
</html>
    ''')

@app.route('/launch/<app_type>', methods=['POST'])
def launch_app(app_type):
    """API endpoint để chạy ứng dụng"""
    try:
        if app_type == 'caesar':
            success = run_app(CAESAR_APP)
            app_name = "Caesar Cipher"
        elif app_type == 'playfair':
            success = run_app(PLAYFAIR_APP)
            app_name = "Playfair Cipher"
        elif app_type == 'railfence':
            success = run_app(RAILFENCE_APP)
            app_name = "Railfence Cipher"
        elif app_type == 'vigenere':
            success = run_app(VIGENERE_APP)
            app_name = "Vigenere Cipher"
        elif app_type == 'rsa':
            success = run_app(RSA_APP)
            app_name = "RSA Cipher"
        else:
            return jsonify({
                'success': False, 
                'message': 'Loại ứng dụng không hợp lệ'
            })
        
        if success:
            return jsonify({
                'success': True, 
                'message': f'{app_name} đã được khởi chạy thành công'
            })
        else:
            return jsonify({
                'success': False, 
                'message': f'Không thể khởi chạy {app_name}'
            })
            
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': f'Lỗi: {str(e)}'
        })

if __name__ == '__main__':
    print("Server đang chạy tại: http://localhost:5001")
    print("Bấm Ctrl+C để dừng server")
    app.run(debug=True, port=5001)
