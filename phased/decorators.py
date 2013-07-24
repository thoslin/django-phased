from phased.utils import second_pass_render


def two_phased(view_func):
    def wrapper(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        if hasattr(response, 'render') and callable(response.render):
            response = response.render()
        response.content = second_pass_render(request, response.content)
        response['Content-Length'] = str(len(response.content))
        return response
    return wrapper