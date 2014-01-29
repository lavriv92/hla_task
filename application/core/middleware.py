from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class LoginMiddleware(object):
    """
    if user not logined redirect on account login
    """
    
    def process_request(self, request):
        """
        Page request settings.
        """
        url = reverse('account:login')
        if (not request.user.is_authenticated() and
            request.get_full_path() != url):
                return HttpResponseRedirect(reverse('account:login'))
        return None

