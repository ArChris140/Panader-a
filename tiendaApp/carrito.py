class Carrito:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        
        carrito = self.session.get('carrito')  # Usamos get para evitar KeyError
        if carrito is None or not isinstance(carrito, dict):  # Verificamos si 'carrito' no existe o no es un diccionario
            self.session['carrito'] = {}  # Creamos una entrada con un diccionario vacío
            carrito = self.session['carrito']  # Obtenemos la referencia al diccionario vacío
        
        self.carrito = carrito  # Asignamos la referencia al carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.Nombre,
                "precio": producto.Precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]['cantidad'] +=1
            self.carrito[id]['precio'] += producto.Precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]['cantidad'] -= 1
            self.carrito[id]['precio'] -= producto.Precio
            if self.carrito[id]['cantidad'] <=0:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session['carrito'] = {}
        self.session.modified = True
