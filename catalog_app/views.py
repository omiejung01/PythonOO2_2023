from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {
        'vaar1': 'This is to handle inpput',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

"""
def back_login(request):
    user = request.GET.get('user')
    passwd = request.GET.get('passwd')

    result1 = [{ 'result': 'Success' }]
    result2 = [{ 'result': 'Failure' }]

    if (user == 'abcd') and (passwd == '1234'):
        qs_json = json.dumps(result1[0])
    else:
        qs_json = json.dumps(result2[0])

    return HttpResponse(qs_json, content_type='application/json')

"""