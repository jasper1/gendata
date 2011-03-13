from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
import types

class json:
    
    def __init__(self, function):
        self._f = function
    
    def __call__(self, *args):
        
        response_dict = self._f(*args)
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
     

class template:
    
    def __init__(self, template_name):
        self._t = template_name
        
    def __call__(self, function):
        self._f =  function
        
        def wrap (*args, **kwargs):
                        
            request = args[0]
            response = self._f(*args, **kwargs)
            
            if type(response) == types.DictType:
                return render_to_response(self._t,
                                          response,
                                          context_instance=RequestContext(request))
            else:
                return response
            
        return wrap