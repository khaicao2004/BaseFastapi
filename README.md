# Fastapi 

## Tạo venv
    python3 -m venv venv ( cài đặt môi trường ảo )
	MacOS: source venv/bin/activate
	pip install <tên_gói> cài đặt các gói phụ thuộc ví dụ ( fastapi )
	pip install -r requirements.txt ( cài nhiều gói cùng 1 lúc, các gói sẽ được viết trong requirements.txt )
	python script.py ( chạy 1 script trong môi trường ảo )
	deactivate ( thoát môi trường ảo )
	uvicorn app.main:app --host 0.0.0.0 --port 8000 ( chạy app )