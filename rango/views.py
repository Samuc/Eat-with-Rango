from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Bar, Tapa, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.forms import UserForm, UserProfileForm


def index(request):
    context = RequestContext(request)
    bar_list = Bar.objects.order_by('-visitas')
    context_dict = { 'bars': bar_list}
    if request.user.is_authenticated():
        user = UserProfile.objects.get(user=request.user)
        context_dict['user_login'] = user


    for bar in bar_list:
        bar.url = bar.nombre.replace(' ', '_')

    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    bar_list = Bar.objects.order_by('-visitas')
    context_dict = { 'bars': bar_list}

    for bar in bar_list:
        bar.url = bar.nombre.replace(' ', '_')
    return render_to_response('rango/about.html', context_dict, context)

def highchart(request):
    context = RequestContext(request)
    bar_list = Bar.objects.order_by('-visitas')

    visits_list = { 'Bar_inicial': 0}

    for bar in bar_list:
        visits_list[bar.nombre]  = (bar.visitas)

    visits_list.pop('Bar_inicial')

    context_dict = { 'bars': bar_list}
    context_dict['visits']=visits_list

    for bar in bar_list:
        bar.url = bar.nombre.replace(' ', '_')
    return render_to_response('rango/highchart.html', context_dict, context)


def base(request):
    return render(request, 'rango/base.html')

def bar(request, bar_name_url):
    context = RequestContext(request)
    bar_nombre = bar_name_url.replace('_', ' ')
    context_dict = {'bar_nombre': bar_nombre}

    try:
        bar = Bar.objects.get(nombre=bar_nombre)
        bar.visitas = bar.visitas + 1
        bar.save()
        tapas = Tapa.objects.filter(bar=bar)
        context_dict['tapas'] = tapas
        context_dict['bar'] = bar
        context_dict['direccion'] =  bar.direccion
        context_dict['bar_name_url'] = bar_name_url
    except Bar.DoesNotExist:
        pass

    return render_to_response('rango/bar.html', context_dict, context)



def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the usernombre and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        print username
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the usernombre/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the hometapa.
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied - Please Go back.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'rango/login.html', {})



    from rango.forms import UserForm, UserProfileForm






def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'rango/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )



from django.contrib.auth import logout

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the hometapa.
    return HttpResponseRedirect('/rango/')



from rango.forms import BarForm

def add_bar(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = BarForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new bar to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the hometapa.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = BarForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_bar.html', {'form': form})



from rango.forms import TapaForm

def add_tapa(request, bar_name_url):
    context = RequestContext(request)
    try:
        bar  = Bar.objects.get(slug=bar_name_url)
    except Bar.DoesNotExist:
                bar = None

    if request.method == 'POST':
        form = TapaForm(request.POST)
        if form.is_valid():
            if bar:
                tapa = form.save(commit=False)
                tapa.bar = bar
                tapa.votos = 0
                tapa.save()
                # probably better to use a redirect here.
                return bar(request, bar_name_url)
        else:
            print form.errors
    else:
        form = TapaForm()

    context_dict = {'form':form, 'bar': bar}
    context_dict['bar_name_url'] = bar_name_url

    return render(request, 'rango/add_tapa.html', context_dict)


def add_tapa_save(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = TapaForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new bar to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the hometapa.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = TapaForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_tapa.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def voto_tapa(request):
    tapa_nombre = None
    if request.method == 'GET':
        tapa_nombre = request.GET['tapa_id']
        bar_slug = request.GET['bar_slug']
    votos = 0
    if tapa_nombre:
        print bar_slug
        tapa = Tapa.objects.get(bar__nombre__startswith=bar_slug, nombre=tapa_nombre)

        if tapa:
            votos = tapa.votos + 1
            tapa.votos =  votos
            tapa.save()


    return HttpResponse(votos)


from django.http import JsonResponse
def reclama_bares (request):
    bar_list = Bar.objects.order_by('-visitas')

    visitas = []
    bares = []


    for bar in bar_list:
        bares.append(bar.nombre)
        visitas.append(bar.visitas)


    return JsonResponse(bares, safe=False)

def reclama_visitas (request):
    bar_list = Bar.objects.order_by('-visitas')

    visitas = []
    bares = []


    for bar in bar_list:
        bares.append(bar.nombre)
        visitas.append(bar.visitas)


    return JsonResponse(visitas, safe=False)
