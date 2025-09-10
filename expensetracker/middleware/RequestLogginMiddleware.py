from typing import Any
from tracker.models import RequestLogs

class RequestMiddleware:
    
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        request_info=(request)
        
        
        RequestLogs.objects.create(
            request_info=vars(request_info),
            request_type=request_info.path,
            request_method=request_info.method,
        )

        return self.get_response(request)
        
        
        