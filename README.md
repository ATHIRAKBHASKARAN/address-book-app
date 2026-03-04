# Address Book APP

## Setup

1. Clone repo
git clone <repo-url>
cd address-book-app

2. Create virtual env
python -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run server
uvicorn app.main:app --reload

5. Open
http://127.0.0.1:8000/docs