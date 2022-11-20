from io import StringIO

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse

from xhtml2pdf import pisa

from .models import Order


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = StringIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Transfer-Encoding'] = 'utf8'
    pisa_status = pisa.pisaDocument(html.encode("UTF-8"),response)

    if not pisa_status.err:
        return result.getvalue()

    return None


@login_required
def admin_order_pdf(request, order_id):
    if request.user.is_superuser:
        order = get_object_or_404(Order, pk=order_id)
        pdf = render_to_pdf('order_pdf.html', {'order': order})

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            content = "attachment; filename=%s.pdf" % order_id
            response['Content-Disposition'] = content

            return response

    return HttpResponse("We can not generate this order reciept")
