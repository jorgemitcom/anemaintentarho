import random
from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from django.forms import formset_factory
from thessia.forms import PalabraForm, PalabraDefForm, Diferencias, Acciones
from thessia.models import Cuento, PruebaUno, PruebaTres
from django.core import serializers


def palabras_aleatorias():
    """
    Metodo que se encarga de retornar una lista con las palabras aleatorias y las letras eliminadas de la palabra
    :return: list
    """
    # Almacenamos en una lista el conjunto de todos nuestros registros
    total = PruebaUno.objects.all()
    data = PruebaUno.objects.filter(pk__in=[1, 2, 3, 4, 5]).values_list('concept', flat=True)

    # Creamos una lista para almacenar los ids de las palabras aleatorias seleccionadas
    id_list = []

    # Almacenamos en una lista 5 registros aleatorios de nuestros conceptos
    total_palabras = random.sample(list(total), k=5)

    # Recorremos la lista con las palabras aleatorias que hemos seleccionado y almacenamos su id en otra lista
    for contador in total_palabras:
        id_list.append(contador.id)

    # Almacenamos en un string cada concepto aleatorio guardado
    palabraUna = str(data[0])
    palabraDos = str(data[1])
    palabraTres = str(data[2])
    palabraCuatro = str(data[3])
    palabraCinco = str(data[4])

    # Almacenamos en una variable de tipo lista cada letra de cada palabra
    uno = list(palabraUna)
    dos = list(palabraDos)
    tres = list(palabraTres)
    cuatro = list(palabraCuatro)
    cinco = list(palabraCinco)

    # Eliminamos ciertas letras de la lista y las almacenamos en otra para poder mostrarla
    for counter in range(2):
        uno.pop(random.randint(0, len(uno) - 1))
        dos.pop(random.randint(0, len(dos) - 1))
        tres.pop(random.randint(0, len(tres) - 1))
        cuatro.pop(random.randint(0, len(cuatro) - 1))
        cinco.pop(random.randint(0, len(cinco) - 1))

    # Almacenamos en una lista las palabras con las letras quitadas
    palabras_finales = [uno, dos, tres, cuatro, cinco]
    palabras_totales = [palabraUna, palabraDos, palabraTres, palabraCuatro, palabraCinco]

    # Retornamos la variable que hemos almacenado en la que se encuentra la lista con las palabras para mostrarlas en
    # el juego y la lista con los ids de cada palabra aleatoria seleccionada
    return palabras_finales, id_list, palabras_totales

def  first_view(request):
    context = {
        'otra_cosa': [1, 2, 3]
    }
    return render(request, 'thessia.html', context)


def  thessia_list_view(request):
    context = {
        'cuentos': Cuento.objects.all().order_by("title")[:4]
    }
    return render(request, 'thessia_list_view.html', context)

def all_thessia_list_view(request):
    context = {
        'cuentos': Cuento.objects.all().order_by("title")
    }
    return render(request, 'all_thessia_list.html', context)

def thessia_detail_view(request, id, *args, **kwargs):
    context = {
        'cuento': Cuento.objects.get(id=id)
    }
    return render(request, 'thessia_detail_view.html', context)

def thessia_interactive_game_view(request):
    context = {
        'palabras': PruebaUno.objects.get(id=1)
    }
    return render(request, 'thessia_interactive_game.html', context)

def thessia_first_test_view(request):

    # Creamos las variables que almacenarán el resultado de unos metodos
    palabras_finales = []
    data = []

    # Almacenamos en una lista el resultado de realizar una consulta que filtar los conceptos con los ids 1,2,3,4,5
    data = PruebaUno.objects.filter(pk__in=[1, 2, 3, 4, 5]).values_list('concept', flat=True)

    # Almacenamos en un objeto de tipo QuerySet el resultado de la consulta que devuelve los primeros 5 registros
    cinco_primeros = PruebaUno.objects.filter(pk__in=[1, 2, 3, 4, 5])

    # Almacenamos en una variable el contenido de cada definición que hemos devuelto en la anterior consulta
    def1 = cinco_primeros[0]
    def2 = cinco_primeros[1]
    def3 = cinco_primeros[2]
    def4 = cinco_primeros[3]
    def5 = cinco_primeros[4]

    # Llamamos al metodo que devuelve 3 listas con objetos distintos en cada uno. Se encarga de eliminar letras aleatorias,
    # devolver los ids de las palabras que se muestran y las palabras completas
    palabras_finales, id_lista, palabras_totales = palabras_aleatorias()

    # Declaramos una variable boolean que se encarga de mostrar un contenido u otra en función del valor que contenga
    mensaje = False

    # Realizamos un contador de visitas del usuario
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Comprobamos si la request está enviando o solicitando datos
    if request.method == 'GET':
        # Almacenamos en un variable de tipo form el formulario con los datos del modelo
        formulary = PalabraForm()

        # En caso de que el contador de visitas llegue a 5, reiniciamos el contador a 0
        if num_visits >= 5:
            request.session['num_visits'] = 0

    # En caso de que estemos enviando datos
    else:
        # Almacenamos en un variable de tipo form el formulario con los datos del modelo
        formulary = PalabraForm(request.POST)

        # Comprobamos si los datos del formulario son válidos
        if formulary.is_valid():
            # Determinamos que la validación es correcta para poder mostrar otro contenido en la página
            mensaje = True

    # Agregamos a la página web los datos que queremos enviar
    context = {
        'form': formulary,
        'palabrasRandom': cinco_primeros,
        'palabras_totales': cinco_primeros,
        'def1': def1,
        'def2': def2,
        'def3': def3,
        'def4': def4,
        'def5': def5,
        'concept1': data[0],
        'concept2': data[1],
        'concept3': data[2],
        'concept4': data[3],
        'concept5': data[4],
        'mensaje': mensaje,
        'uno': palabras_finales[0],
        'dos': palabras_finales[1],
        'tres': palabras_finales[2],
        'cuatro': palabras_finales[3],
        'cinco': palabras_finales[4],
        'num_visits': num_visits
    }

    # Retornamos la request, la página a la que queremos enviarlo y el contexto con todos los datos que queremos enviar
    return render(request, "thessia_first_test.html", context)

def  thessia_second_test_view(request):

    # Declaramos la variable que indica si el usuario ha acertado la prueba
    mensaje = False
    err = ""

    definitions = PruebaUno.objects.filter(pk__in=[4, 6, 7, 8, 10])

    # Comprobamos si la request está enviando o solicitando datos
    if request.method == 'GET':
        # Almacenamos en un variable de tipo form el formulario con los datos del modelo
        formulary = PalabraDefForm

    # En caso de que estemos enviando datos
    else:
        # Almacenamos en un variable de tipo form el formulario con los datos del modelo
        formulary = PalabraDefForm(request.POST)

        # Comprobamos si los datos del formulario son válidos
        if formulary.is_valid():
            # Determinamos que la validación es correcta para poder mostrar otro contenido en la página
            mensaje = True


    context = {
        'cuentos': Cuento.objects.all().order_by("title")[:4],
        'form': formulary,
        'definitions': definitions,
        'mensaje': mensaje
    }
    return render(request, 'thessia_second_test.html', context)

def  thessia_third_test_view(request):
    # Declaramos la variable que indica si el usuario ha acertado la prueba
    mensaje = False
    final = False
    ultimo = PruebaTres.objects.last()
    formulary2 = Acciones

    # Comprobamos si la request está enviando o solicitando datos
    if request.method == 'GET':
        # Almacenamos en un variable de tipo form el formulario con los datos del modelo
        formulary = Diferencias

    # En caso de que estemos enviando datos
    elif 'diferencias' in request.POST:
        # Almacenamos en un variable de tipo form el formulario con los datos del modelo
        formulary = Diferencias(request.POST)

        # Comprobamos si los datos del formulario son válidos
        if formulary.is_valid():

            # Guardamos los datos que ha introducido el usuario en la base de datos una vez validados
            formulary.save()

            # Almacenamos en un objeto de tipo QuerySet el contenido de buscar el último objeto de nuestra base de datos
            ultimo = PruebaTres.objects.last()

            # Determinamos que la validación es correcta para poder mostrar otro contenido en la página
            mensaje = True

    # En caso de que el último formulario haya sido enviado en request, validamos ese formulario concreto
    elif 'acciones' in request.POST:

        # Almacenamos en un variable de tipo form el formulario con los datos del formulario
        formulary2 = Acciones(request.POST)

        # Comprobamos si los datos del formulario son válidos
        if formulary2.is_valid():
            # Determinamos que la validación es correcta para poder mostrar otro contenido en la página
            final = True

    context = {
        'form': formulary,
        'form2': formulary2,
        'mensaje': mensaje,
        'ultimo': ultimo,
        'mensaje_final': final
    }
    return render(request, 'thessia_third_test.html', context)
