from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import requests
from scripts.financial_scraper import get_historical_stock, get_exchange_rate, get_historical_currency
from scripts.analysis import create_df, get_plots
from .models import Article, Date, Ticker, Currency
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import date, timedelta
from scripts.form import UserInput
from scripts.translate import translate_keywords
import pandas as pd
import numpy as np
import random
import re


def get_date_ints(article_date):
    '''
    Takes a date string and return a datime object with the year,month,day
    '''

    pattern = r'(?<=0)\d|\d{4}|[^/0]\d*'
    date_ints = re.findall(pattern, article_date)
    m,d,y = date_ints
    return date(int(y),int(m),int(d))

def search_news(request):
    '''
    search news form page
    '''

    if request.method == 'POST':
        form = UserInput(request.POST)
        if form.is_valid():
            HttpResponse('Thank you we are processing your request')
    else:
        form = UserInput()
    return render(request,'search.html',{'form': form})

def results_png(dates,scores_text,scores_title,findata):

    df = create_df(dates,scores_text,scores_title,findata)

    get_plots(df)

def results(request):
    '''
    This function will take user data and query our database for the appropriate information
    to create our subplots

    INPUTS:
        form data
    Outputs:
        results page with  get_plots
    '''

    column_names = [
        'Title',
        'Published Date',
        'Title Sentiment Score',
        'Text Sentiment Score',
        'Source',
        'Financial Data']

    context = {}
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = UserInput(request.POST)

        # Check if the form is valid:
        if form.is_valid():

            args = True

            start_date = get_date_ints(form.data['start_date'])
            end_date = get_date_ints(form.data['end_date'])
            

            dobjs =  Date.objects.filter(pk__range=(start_date, end_date))

            articles = []
            findata_real = []

            keyword = form.data['keyword']

            if form.data['spanish_word'] == 'Y':
                keyword = translate_keywords(keyword)

            if keyword == None:
                context['result'] = 'g_fail'
                return render(request,'results.html',context)

            

            for dobj in dobjs:
                article = Article.objects.filter(date = dobj)


                
                if len(keyword.split()) > 1:
                    
                    split_keywords = keyword.split()
                    
                    article = article.filter(title__icontains=split_keywords[0]+" ")
                    
                    for word in split_keywords[1:]:
                        
                        article = article.filter(title__icontains=word)

                        
                else:

                    article = article.filter(title__icontains=keyword+" ")

                if len(article):

                    articles.append(article)

                    if form.data['stock_or_currency'] == 'stocks':
                        stock = Ticker.objects.filter(ticker=form.data['ticker'], date=dobj)
                        findata_real.append(stock[0].close)
                        column_names[-1] = form.data['ticker']
                    else:
                        exchange_rate = Currency.objects.filter(date = dobj)
                        findata_real.append(exchange_rate[0].exchange_rate)


            dates = []
            nltk_scores = []
            nltk_scores_title = []
            articles_print=[]

            for index, article in enumerate(articles):
                for a in article:
                    dates.append(a.date_id)
                    nltk_scores.append(a.nltk_score)
                    nltk_scores_title.append(a.nltk_score_title)
                    articles_print.append([a.title,a.date_id,a.nltk_score,a.nltk_score_title,a.source,findata_real[index]])

            if not len(articles_print):
                context['result'] = None
            else:
                results_png(dates,nltk_scores,nltk_scores_title,findata_real)
                context['result'] = articles_print
                context['num_results'] = len(articles_print)
                context['columns'] = column_names
            context['form']=form
    else:
        form= UserInput()

    return render(request,'results.html',context)
