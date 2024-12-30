from django.shortcuts import render
import subprocess
import os

def home(request):
    return render(request, 'app/index.html')  # Render the same template for simplicity

def streamlit_app(request):
    script_path = os.path.join(os.path.dirname(__file__), '../scripts/ai_chat_st_app.py')
    script_path = os.path.join(os.path.dirname(__file__), '../scripts/main_app.py')
    script_path = os.path.join(os.path.dirname(__file__), '../scripts/pricing_func.py')
    script_path = os.path.join(os.path.dirname(__file__), '../scripts/ai_chat_analyst_script.py')
    subprocess.Popen(['streamlit', 'run', script_path])
    return render(request, 'app/index.html')