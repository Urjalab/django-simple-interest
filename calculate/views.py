from django.shortcuts import render

def convert_to_int(value):

    integer_value = int(value)
    return integer_value

def index(request):

    context = {}
    if request.method == 'POST':

        user_data = request.POST

        principal = convert_to_int(user_data['principal'])
        time = convert_to_int(user_data['time'])
        rate = convert_to_int(user_data['rate'])

        simple_interest = principal * time * rate / 100

        context = {
            'principal' : principal,
            'time' : time,
            'rate' : rate,
            'answer' : simple_interest,
        }
        

    return render(
        request,
        'calculate/index.html',
        context
    )
