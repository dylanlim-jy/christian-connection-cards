import os
import json
import random
import functools
from collections import Counter
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
    image_list = ['1.svg', '2.svg', '3.svg', '4.svg', '5.svg', '6.svg', '7.svg']
    random_image = random.choice(image_list)

    # Define max range for questions
    with open(QUESTIONS_PATH, 'r') as json_file:
        questions = json.load(json_file)
    max_card_range_number = max_cards(questions) - (max_cards(questions) % 3)

    context = {
        'random_image': random_image,
        'max_cards': max_card_range_number,
        'default_cards': max_card_range_number // 2,
    }

    return render(request, 'cards/index.html', context)


def play(request):
    # Define max range for questions
    with open(QUESTIONS_PATH, 'r') as json_file:
        questions = json.load(json_file)
    max_card_range_number = max_cards(questions)
    num_cards = request.session.get('num_cards', str(max_card_range_number // 2))
    filtered_questions = generate_questions(questions, int(num_cards))
    
    context = {
        'num_cards': functools.reduce(lambda a, b: a if a > b['index'] else b['index'], filtered_questions, 0),
        'serialised_questions': json.dumps(filtered_questions),
    }

    return render(request, 'cards/play.html', context)

def how_to_play(request):
    return render(request, 'cards/how_to_play.html', {})

def about(request):
    return render(request, 'cards/about.html', {})

def suggest(request):
    return render(request, 'cards/suggest.html', {})

def question_bank(request):
    with open(QUESTIONS_PATH, 'r') as json_file:
        questions = json.load(json_file)
    context = {
        'questions': questions,
    }
    return render(request, 'cards/question_bank.html', context)


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

def max_cards(questions):
    stage_occurrences = [question['stage'] for question in questions]
    stage_counter = Counter(stage_occurrences)
    max_cards = min(stage_counter.values())
    return max_cards