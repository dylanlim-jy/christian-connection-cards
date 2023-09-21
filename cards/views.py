import os
import json
import random
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

QUESTIONS_PATH = os.path.join(settings.STATIC_ROOT, 'cards/questions.json')


def index(request):
    if request.method == 'POST':
        request.session['num_cards'] = request.POST['num_cards']
        return HttpResponseRedirect(reverse('cards:play'))
    
    return render(request, 'cards/index.html', {})


def play(request):
    num_cards = request.session.get('num_cards', None)
    
    with open(QUESTIONS_PATH, 'r') as json_file:
        questions = json.load(json_file)

    context = {
        'num_cards': num_cards,
        'questions': questions,
        'filtered_questions': generate_questions(questions, int(num_cards)),
    }

    return render(request, 'cards/play.html', context)


def generate_questions(questions, n):
    random.shuffle(questions)
    filtered_questions = {}
    for stage in range(1,4):
        stage_question = [q['question'] for q in questions if q['stage'] == stage]
        filtered_questions['Stage ' + str(stage)] = stage_question[:n]
    return filtered_questions