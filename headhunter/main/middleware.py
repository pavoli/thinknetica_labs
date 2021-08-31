from django_user_agents.utils import get_user_agent


class MobileVersionMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        print(exception.__class__.__name__)
        print(exception.message)
        return None

    def process_request(self, request):
        user_agent = get_user_agent(request)

        if user_agent.is_mobile:
            request.urlconf = "main.mobile.urls"
        else:
            print('Desctop.')
