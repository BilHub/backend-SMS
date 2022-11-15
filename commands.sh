# rm -rf *.sqlite3
# source ./venvSchool/bin/activate
# rm -rf */migrations/00*.py
python manage.py makemigrations
python manage.py migrate
# python manage.py loaddata userType.json
# python manage.py loaddata wilaya.json
# python manage.py loaddata communes.json
# python manage.py loaddata school.json
# python manage.py loaddata userGroup.json
#python manage.py loaddata users.json
#python manage.py loaddata cycle.json
# python manage.py loaddata level.json
# python manage.py loaddata modules.json
#python manage.py loaddata classrooms.json
python manage.py runserver
