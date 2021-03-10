import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# add python site packages, you can use virtualenvs also
site.addsitedir("C:/Users/suneel/AppData/Local/Programs/Python/Python39/Lib/site-packages")

# Add the app's directory to the PYTHONPATH 
sys.path.append('C:/Users/suneel/Downloads/project-py') 
sys.path.append('C:/Users/suneel/Downloads/project-py/python_webapp_django')  

os.environ['DJANGO_SETTINGS_MODULE'] = 'python_webapp_django.settings' 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_webapp_django.settings")  
 
application = get_wsgi_application()