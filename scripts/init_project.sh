python manage.py makemigrations
python manage.py migrate
python manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('admin@example.com', 'arch@SL01');"
python manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_user('sample001@example.com', 'arch@SL01');"
python manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_user('sample002@example.com', 'arch@SL01');"
python manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_user('sample003@example.com', 'arch@SL01');"
python manage.py loaddata shiftapp.initdata.json
python manage.py runserver
