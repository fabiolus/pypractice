from django.http import HttpResponse, Http404

from django.shortcuts import render, get_object_or_404, get_list_or_404

from mypolls.models import Poll, Choice

def index(request):
    poll_list = get_list_or_404(Poll)
    return render(request,'mypolls/index.html',{'poll_list':poll_list})
    
def detail(request,poll_id):
    poll = get_object_or_404(Poll,pk=poll_id)
    return render(request,'mypolls/detail.html',{'poll':poll})
    
    
def results(request,poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request,'mypolls/results.html',{'poll':poll})
    
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return HttpResponse('Vote Page')