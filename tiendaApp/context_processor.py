def total_carrito(request):
    total = 0
    if 'carrito' in request.session and request.session['carrito']:
        for key, value in request.session['carrito'].items():
            total += int(value['precio'])
    return {'total_carrito': total}

def identificador(request):
    valor = 1
    if 'carrito' in request.session and request.session['carrito']:
        for key, value in request.session['carrito'].items():
            valor += 1

    valor = 1
    return {'identificador': str(valor)}
