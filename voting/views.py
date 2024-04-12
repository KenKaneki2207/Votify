from django.shortcuts import render, redirect
from django.http import HttpResponse
from voting.models import vote, Election
from votingUser.models import Candidate

active_elections = Election.objects.filter(is_over=False)
candidates_lists = []
for election in active_elections:
    candidates = Candidate.objects.filter(Election=election)
    candidates_lists.append({'election': election, 'candidates': candidates})

# Create your views here.
def voting(request):
    active_elections = Election.objects.filter(is_over=False)
    candidates_lists = []
    for election in active_elections:
        candidates = Candidate.objects.filter(Election=election)
        candidates_lists.append({'election': election, 'candidates': candidates})
    return render(request,'voting.html',{'candidates_lists':candidates_lists})

def result(request):
    result = Candidate.objects.filter(Election__is_over=False)
    print(result)
    return render(request, 'result.html', {'result':result})

def home(request):
    return render(request, 'home.html')

def send_vote(request, candidate_name):
    # candidates = Candidate.objects.all()
    voter = request.user.id
    candidate_name = candidate_name
    print(type(vote.objects.filter(voter = voter).exists()))
    if vote.objects.filter(voter = voter).exists() == True:
        message = 'You can Vote only once' 
        return render(request, 'voting.html',{'message':message, 'candidates_lists':candidates_lists})
    else:
        print(candidate_election, '*******************************')
        candidate_election = Election.objects.get(id = candidate_election)
        
        new_vote = vote.objects.create(voter=voter, candidate=candidate_name, election=candidate_election)
        new_vote.save()
        print('******************Successfully added********')  
        add_votes = Candidate.objects.get(name=candidate_name)
        add_votes.votes += 1
        add_votes.save()
        print('****************Successfully incremented votes***************')
        return redirect('result')
    
