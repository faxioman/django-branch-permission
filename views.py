from django.http import HttpResponse


def hide_site_selection_css(request):
    css = None
    if not request.user.is_superuser:
        css = """
            .field-sites {
                display: none;
            }
        """
    return HttpResponse(css, content_type='text/css')