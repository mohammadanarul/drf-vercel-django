echo 'build start'
python3.9 -m pip install -r requirements.txt
python3.9 manage.py makemigratoins
python3.9 manage.py migrate
echo 'build end'