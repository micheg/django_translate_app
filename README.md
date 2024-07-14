# django_translate_app
un clone di google translate in django e dl-translate

# install

ˆˆˆ
python3 -m venv .
. bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
ˆˆˆ

# test

ˆˆˆ
curl -X POST http://localhost:8000/api/translate/      -H "Content-Type: application/json"      -d '{
           "text": "Hello, world!",
           "source_lang": "english",
           "target_lang": "italian"
         }'
ˆˆˆ

# visit

http://127.0.0.1:8000/

