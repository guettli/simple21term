from simple21.models import GlobalConfig


class SetAnonymousUserMiddleware:
    """
    Avoid fancy if/else dancing in the code. The user in request.user is always a real row in the
    users table.

    Related: https://github.com/guettli/programming-guidelines/blob/master/README.md#avoid-nullable-foreign-keys
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            request.user = GlobalConfig.get().anonymous_user
        return self.get_response(request)
