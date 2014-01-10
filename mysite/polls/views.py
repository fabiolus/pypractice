# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from django.template import RequestContext, loader

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.core.urlresolvers import reverse

from django.utils import timezone

from polls.models import Poll, Choice

def index(request):
    latest_poll_list = Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    output = ', '.join(p.question for p in latest_poll_list)
    #return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    context = RequestContext(request,{'latest_poll_list': latest_poll_list, })
    return HttpResponse(template.render(context))
    
def detail(request,poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
        
    return render(request,'polls/detail.html',{'poll':poll})
    
    

def results(request,poll_id):
    poll = get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/results.html',{'poll':poll})

def vote(request,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'poll':p, 'error_message':'You have not selected a choice'})
        
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
    