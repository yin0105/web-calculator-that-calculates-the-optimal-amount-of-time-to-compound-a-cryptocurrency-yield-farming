from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django import template
from os.path import join, dirname
from dotenv import load_dotenv
import os

cur_path = dirname(__file__)
env_path = cur_path[:cur_path.rfind("\\")] 
dotenv_path = join(env_path, '.env')
load_dotenv(dotenv_path)
print("### " + dotenv_path + " ##")

context = {}

context['TOKEN_APR_MIN'] = float(os.environ.get('TOKEN_APR_MIN'))
context['TOKEN_APR_MAX'] = float(os.environ.get('TOKEN_APR_MAX'))
context['GAS_FEE_MIN'] = float(os.environ.get('GAS_FEE_MIN'))
context['GAS_FEE_MAX'] = float(os.environ.get('GAS_FEE_MAX'))
context['TIME_HORIZON_DAYS_MIN'] = int(os.environ.get('TIME_HORIZON_DAYS_MIN'))
context['TIME_HORIZON_DAYS_MAX'] = int(os.environ.get('TIME_HORIZON_DAYS_MAX'))
context['TOKEN_START_COUNT_MIN'] = float(os.environ.get('TOKEN_START_COUNT_MIN'))
context['TOKEN_START_COUNT_MAX'] = float(os.environ.get('TOKEN_START_COUNT_MAX'))
context['TOKEN_START_PRICE_MIN'] = float(os.environ.get('TOKEN_START_PRICE_MIN'))
context['TOKEN_START_PRICE_MAX'] = float(os.environ.get('TOKEN_START_PRICE_MAX'))
context['TOKEN_END_PRICE_MIN'] = float(os.environ.get('TOKEN_END_PRICE_MIN'))
context['TOKEN_END_PRICE_MAX'] = float(os.environ.get('TOKEN_END_PRICE_MAX'))


def index(request):
    global dotenv_path
    print(dotenv_path)
    
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))
