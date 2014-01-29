from django.http import HttpResponseRedirect


class LoginMiddleware(object):
    """
    if user not logined redirect on account login
    """
    
    def process_request(self, request):
        """
        page request settings
        """
        if not request.user.is_authenticated():
            pass
            #return HttpResponseRedirect('/account/login')
        return None
    
