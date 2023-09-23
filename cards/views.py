import os
import json
import random
import functools
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

QUESTIONS_PATH = os.path.join(settings.STATIC_ROOT, 'cards/questions.json')


def index(request):
    if request.method == 'POST':
        request.session['num_cards'] = request.POST['num_cards']
        return HttpResponseRedirect(reverse('cards:play'))
    
    # Randomise hero image selection
    image_list = ['1.svg', '2.svg', '3.svg', '4.svg']
    random_image = random.choice(image_list)
    context = {
        'random_image': random_image,
    }
    return render(request, 'cards/index.html', context)


def play(request):
    num_cards = request.session.get('num_cards', None)
    
    with open(QUESTIONS_PATH, 'r') as json_file:
        questions = json.load(json_file)
    filtered_questions = generate_questions(questions, int(num_cards))
    
    context = {
        'num_cards': functools.reduce(lambda a, b: a if a > b['index'] else b['index'], filtered_questions, 0),
        'serialised_questions': json.dumps(filtered_questions),
    }

    return render(request, 'cards/play.html', context)

def how_to_play(request):
    return render(request, 'cards/how_to_play.html', {})


def generate_questions(questions, n):
    random.shuffle(questions)
    filtered_questions = []
    question_index = 1

    for stage in range(1,4):
        question_list_for_stage = [q['question'] for q in questions if q['stage'] == stage]
        filtered_question_list_for_stage = question_list_for_stage[:n]
        for filtered_question in filtered_question_list_for_stage:
            filtered_questions.append({
                'index': question_index,
                'stage': stage,
                'question': filtered_question,
            })
            question_index+=1
    
    return filtered_questions