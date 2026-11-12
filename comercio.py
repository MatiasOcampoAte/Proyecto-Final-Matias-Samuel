def leerProductos():
    listaProductos = []
    try:
        archivo = open("productos.csv", "r")
        lineas = archivo.readlines()
        archivo.close()
        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            if linea != "":
                partes = linea.split(",")
                if len(partes) >= 4:
                    producto = {
                        "sku": partes[0].strip().upper(),
                        "nombre": partes[1].strip(),
                        "categoria": partes[2].strip().upper(),
                        "precioVenta": int(partes[3].strip())
                    }
                    listaProductos.append(producto)
    except FileNotFoundError:
        raise FileNotFoundError("Error: No se encontró el archivo productos.csv.")
    except ValueError as e:
        raise ValueError(f"Error numérico en productos.csv: {e}")
    except IndexError as e:
        raise IndexError(f"Error de columnas en productos.csv: {e}")
    return listaProductos

def leerLotes():
    listaLotes = []
    try:
        archivo = open("lotes.csv", "r")
        lineas = archivo.readlines()
        archivo.close()
        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            if linea != "":
                partes = linea.split(",")
                if len(partes) >= 5:
                    lote = {
                        "lote": partes[0].strip().upper(),
                        "sku": partes[1].strip().upper(),
                        "vencimiento": partes[2].strip(),
                        "cantidad": int(partes[3].strip()),
                        "costoUnitario": int(partes[4].strip())
                    }
                    listaLotes.append(lote)
    except FileNotFoundError:
        raise FileNotFoundError("Error: No se encontró el archivo lotes.csv.")
    except ValueError as e:
        raise ValueError(f"Error numérico en lotes.csv: {e}")
    except IndexError as e:
        raise IndexError(f"Error de columnas en lotes.csv: {e}")
    return listaLotes

def guardarLotes(listaLotes):
    try:
        archivo = open("lotes.csv", "w")
        archivo.write("lote,sku,vencimiento,cantidad,costo_unitario\n")
        for l in listaLotes:
            linea = f"{l['lote']},{l['sku']},{l['vencimiento']},{l['cantidad']},{l['costoUnitario']}\n"
            archivo.write(linea)
        archivo.close()
        return True
    except FileNotFoundError:
        raise FileNotFoundError("Error: No se encontró el archivo lotes.csv para guardar.")

def leerClientes():
    listaClientes = []
    try:
        archivo = open("clientes.csv", "r")
        lineas = archivo.readlines()
        archivo.close()
        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            if linea != "":
                partes = linea.split(",")
                if len(partes) >= 3:
                    cliente = {
                        "clienteId": partes[0].strip().upper(),
                        "nombre": partes[1].strip(),
                        "tipo": partes[2].strip().upper()
                    }
                    listaClientes.append(cliente)
    except FileNotFoundError:
        raise FileNotFoundError("Error: No se encontró el archivo clientes.csv.")
    except IndexError as e:
        raise IndexError(f"Error de formato en clientes.csv: {e}")
    return listaClientes

def leerVentas():
    listaVentas = []
    try:
        archivo = open("ventas.csv", "r")
        lineas = archivo.readlines()
        archivo.close()
        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            if linea != "":
                partes = linea.split(",")
                if len(partes) >= 9:
                    venta = {
                        "ventaId": partes[0].strip().upper(),
                        "fecha": partes[1].strip(),
                        "clienteId": partes[2].strip().upper(),
                        "subtotal": int(partes[3].strip()),
                        "descuento": int(partes[4].strip()),
                        "iva": int(partes[5].strip()),
                        "envio": int(partes[6].strip()),
                        "total": int(partes[7].strip()),
                        "estado": partes[8].strip().upper()
                    }
                    listaVentas.append(venta)
    except FileNotFoundError:
        raise FileNotFoundError("Error: No se encontró el archivo ventas.csv.")
    except ValueError as e:
        raise ValueError(f"Error al leer números en ventas.csv: {e}")
    except IndexError as e:
        raise IndexError(f"Error de formato en ventas.csv: {e}")
    return listaVentas

def guardarVentas(listaVentas):
    try:
        archivo = open("ventas.csv", "w")
        archivo.write("venta_id,fecha,cliente_id,subtotal,descuento,iva,envio,total,estado\n")
        for v in listaVentas:
            linea = f"{v['ventaId']},{v['fecha']},{v['clienteId']},{v['subtotal']},{v['descuento']},{v['iva']},{v['envio']},{v['total']},{v['estado']}\n"
            archivo.write(linea)
        archivo.close()
        return True
    except FileNotFoundError:
        raise FileNotFoundError("Error: No se encontró el archivo ventas.csv para guardar.")

def leerDetalleVentas():
    listaDetalles = []
    try:
        archivo = open("detalle_ventas.csv", "r")
        lineas = archivo.readlines()
        archivo.close()
        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            if linea != "":
                partes = linea.split(",")
                if len(partes) >= 6:
                    det = {
                        "ventaId": partes[0].strip().upper(),
                        "sku": partes[1].strip().upper(),
                        "lote": partes[2].strip().upper(),
                        "cantidad": int(partes[3].strip()),
                        "precioUnitario": int(partes[4].strip()),
                        "costoUnitario": int(partes[5].strip())
                    }
                    listaDetalles.append(det)
    except FileNotFoundError:
        raise FileNotFoundError("Error: No se encontró el archivo detalle_ventas.csv.")
    except ValueError as e:
        raise ValueError(f"Error numérico en detalle_ventas.csv: {e}")
    except IndexError as e:
        raise IndexError(f"Error de columnas en detalle_ventas.csv: {e}")
    return listaDetalles

def guardarDetalleVentas(listaDetalles):
    try:
        archivo = open("detalle_ventas.csv", "w")
        archivo.write("venta_id,sku,lote,cantidad,precio_unitario,costo_unitario\n")
        for d in listaDetalles:
            linea = f"{d['ventaId']},{d['sku']},{d['lote']},{d['cantidad']},{d['precioUnitario']},{d['costoUnitario']}\n"
            archivo.write(linea)
        archivo.close()
        return True
    except FileNotFoundError:
        raise FileNotFoundError("Error: No se encontró el archivo detalle_ventas.csv para guardar.")

def registrarAnulacion(ventaId, fechaAnulacion, motivo):
    try:
        archivo = open("anulaciones.csv", "a")
        archivo.write(f"{ventaId},{fechaAnulacion},{motivo}\n")
        archivo.close()
        return True
    except FileNotFoundError:
        raise FileNotFoundError("Error: No se encontró el archivo anulaciones.csv.")

def validarFormatoFecha(fechaStr):
    partes = fechaStr.strip().split("-")
    if len(partes) != 3:
        return False
    try:
        anio = int(partes[0])
        mes = int(partes[1])
        dia = int(partes[2])
        if anio < 2000 or anio > 2100:
            return False
        if mes < 1 or mes > 12:
            return False
        if dia < 1 or dia > 31:
            return False
        return True
    except (ValueError, IndexError):
        return False

def buscarProductoPorSku(sku):
    listaProductos = leerProductos()
    for p in listaProductos:
        if p["sku"] == sku.upper():
            return p
    return {}

def buscarClientePorId(clienteId):
    listaClientes = leerClientes()
    for c in listaClientes:
        if c["clienteId"] == clienteId.upper():
            return c
    return {}

def buscarVentaPorId(ventaId):
    listaVentas = leerVentas()
    for v in listaVentas:
        if v["ventaId"] == ventaId.upper():
            return v
    return {}

def obtenerLotesVendiblesPorSku(sku, fechaOperacion):
    listaLotes = leerLotes()
    lotesFiltrados = []
    for l in listaLotes:
        if l["sku"] == sku.upper():
            if l["cantidad"] > 0 and l["vencimiento"] >= fechaOperacion:
                lotesFiltrados.append(l)
    for i in range(len(lotesFiltrados)):
        for j in range(len(lotesFiltrados) - 1):
            cambiar = False
            if lotesFiltrados[j]["vencimiento"] > lotesFiltrados[j + 1]["vencimiento"]:
                cambiar = True
            elif lotesFiltrados[j]["vencimiento"] == lotesFiltrados[j + 1]["vencimiento"]:
                if lotesFiltrados[j]["lote"] > lotesFiltrados[j + 1]["lote"]:
                    cambiar = True
            if cambiar:
                temp = lotesFiltrados[j]
                lotesFiltrados[j] = lotesFiltrados[j + 1]
                lotesFiltrados[j + 1] = temp
    return lotesFiltrados

def obtenerStockVendiblePorSku(sku, fechaOperacion):
    lotesValidos = obtenerLotesVendiblesPorSku(sku, fechaOperacion)
    totalStock = 0
    for l in lotesValidos:
        totalStock += l["cantidad"]
    return totalStock

def calcularAsignacionFefo(sku, cantidadRequerida, fechaOperacion):
    lotesOrdenados = obtenerLotesVendiblesPorSku(sku, fechaOperacion)
    asignaciones = []
    pendiente = cantidadRequerida
    for l in lotesOrdenados:
        if pendiente <= 0:
            break
        disponibleEnLote = l["cantidad"]
        if disponibleEnLote > 0:
            if disponibleEnLote >= pendiente:
                asignaciones.append({
                    "lote": l["lote"],
                    "sku": sku,
                    "cantidad": pendiente,
                    "vencimiento": l["vencimiento"],
                    "costoUnitario": l["costoUnitario"]
                })
                pendiente = 0
            else:
                asignaciones.append({
                    "lote": l["lote"],
                    "sku": sku,
                    "cantidad": disponibleEnLote,
                    "vencimiento": l["vencimiento"],
                    "costoUnitario": l["costoUnitario"]
                })
                pendiente -= disponibleEnLote
    if pendiente > 0:
        return []
    return asignaciones

def generarSiguienteIdVenta():
    listaVentas = leerVentas()
    maximo = 0
    for v in listaVentas:
        idStr = v["ventaId"]
        if idStr.startswith("V"):
            try:
                num = int(idStr[1:])
                if num > maximo:
                    maximo = num
            except (ValueError, IndexError):
                pass
    siguiente = maximo + 1
    textoNum = str(siguiente)
    while len(textoNum) < 4:
        textoNum = "0" + textoNum
    return f"V{textoNum}"

def opcionListarProductosYLotes(fechaOperacion):
    menuOpciones = (
        "\n" + "=" * 65 + "\n"
        f"CATÁLOGO DE PRODUCTOS Y LOTES VÁLIDOS (Fecha de corte: {fechaOperacion})\n"
        + "=" * 65 + "\n"
        "1. Ver catálogo completo y stock vendible\n"
        "2. Filtrar productos por categoría\n"
        "3. Consultar detalle de lotes por SKU (vigentes y vencidos)\n"
        "-----------------------------------------------------------------\n"
    )
    subOpcion = input(menuOpciones + "Seleccione una opción [1-3]: ").strip()
    listaProductos = leerProductos()
    if subOpcion == "1":
        salida = "\n" + "-" * 75 + "\n"
        salida += "{:<8} {:<25} {:<15} {:<12} {:<12}\n".format("SKU", "NOMBRE", "CATEGORÍA", "PRECIO", "STOCK VEND.")
        salida += "-" * 75 + "\n"
        for p in listaProductos:
            stock = obtenerStockVendiblePorSku(p["sku"], fechaOperacion)
            salida += "{:<8} {:<25} {:<15} ${:<11} {:<12}\n".format(p["sku"], p["nombre"], p["categoria"], p["precioVenta"], stock)
        salida += "-" * 75
        return salida
    elif subOpcion == "2":
        categorias = []
        for p in listaProductos:
            if p["categoria"] not in categorias:
                categorias.append(p["categoria"])
        ayudaCat = "Categorías disponibles: [" + ", ".join(categorias) + "]\n"
        categoriaBuscada = input(ayudaCat + "Ingrese la categoría a consultar: ").strip().upper()
        if categoriaBuscada == "":
            raise ValueError("Error: Debe ingresar una categoría para filtrar.")
        salida = f"\nProductos pertenecientes a la categoría '{categoriaBuscada}':\n"
        salida += "-" * 60 + "\n"
        salida += "{:<8} {:<25} {:<12} {:<12}\n".format("SKU", "NOMBRE", "PRECIO", "STOCK VEND.")
        salida += "-" * 60 + "\n"
        encontrados = 0
        for p in listaProductos:
            if p["categoria"] == categoriaBuscada:
                encontrados += 1
                stock = obtenerStockVendiblePorSku(p["sku"], fechaOperacion)
                salida += "{:<8} {:<25} ${:<11} {:<12}\n".format(p["sku"], p["nombre"], p["precioVenta"], stock)
        if encontrados == 0:
            salida += f"No se encontraron productos registrados bajo la categoría '{categoriaBuscada}'.\n"
        salida += "-" * 60
        return salida
    elif subOpcion == "3":
        ayudaSkus = "Productos disponibles en catálogo:\n"
        for p in listaProductos:
            ayudaSkus += f"  [{p['sku']}] {p['nombre']}\n"
        skuBuscado = input(ayudaSkus + "Ingrese el código SKU a consultar: ").strip().upper()
        prod = buscarProductoPorSku(skuBuscado)
        if len(prod) == 0:
            raise ValueError(f"Error: El código SKU '{skuBuscado}' no existe en el catálogo.")
        salida = f"\nDetalle de lotes para {prod['sku']} - {prod['nombre']}:\n"
        salida += "-" * 65 + "\n"
        salida += "{:<8} {:<12} {:<10} {:<12} {:<15}\n".format("LOTE", "VENCIMIENTO", "CANTIDAD", "COSTO UNIT", "ESTADO")
        salida += "-" * 65 + "\n"
        listaLotes = leerLotes()
        hayLotes = False
        for l in listaLotes:
            if l["sku"] == skuBuscado:
                hayLotes = True
                estado = "VENDIBLE"
                if l["vencimiento"] < fechaOperacion:
                    estado = "VENCIDO"
                elif l["cantidad"] == 0:
                    estado = "AGOTADO"
                salida += "{:<8} {:<12} {:<10} ${:<11} {:<15}\n".format(l["lote"], l["vencimiento"], l["cantidad"], l["costoUnitario"], estado)
        if not hayLotes:
            salida += "No se registran lotes en inventario para este producto.\n"
        salida += "-" * 65
        return salida
    else:
        raise ValueError("Opción inválida. Seleccione un número entre 1 y 3.")

def opcionGestionarCarrito(carrito, fechaOperacion):
    mensajeEstado = ""
    while True:
        contenido = "\n" + "=" * 55 + "\n"
        contenido += "GESTIÓN DEL CARRITO DE COMPRA\n"
        contenido += "=" * 55 + "\n"
        if len(carrito) == 0:
            contenido += "El carrito se encuentra actualmente VACÍO.\n"
        else:
            contenido += "Contenido actual del carrito:\n"
            contenido += "{:<8} {:<22} {:<10} {:<10}\n".format("SKU", "NOMBRE", "CANTIDAD", "SUBTOTAL")
            contenido += "-" * 55 + "\n"
            subtotalCarrito = 0
            for skuItem, cantItem in carrito.items():
                pInfo = buscarProductoPorSku(skuItem)
                subProd = cantItem * pInfo["precioVenta"]
                subtotalCarrito += subProd
                contenido += "{:<8} {:<22} {:<10} ${:<10}\n".format(skuItem, pInfo["nombre"][:20], cantItem, subProd)
            contenido += "-" * 55 + "\n"
            contenido += f"Subtotal acumulado: ${subtotalCarrito}\n"
        contenido += "\n1. Agregar producto al carrito\n"
        contenido += "2. Modificar cantidad de un producto\n"
        contenido += "3. Eliminar un producto del carrito\n"
        contenido += "4. Vaciar carrito completo\n"
        contenido += "0. Regresar al menú principal\n"
        if mensajeEstado != "":
            contenido += f"\n>>> NOTIFICACIÓN: {mensajeEstado}\n"
            mensajeEstado = ""
        subOpcion = input(contenido + "\nSeleccione una opción [0-4]: ").strip()
        if subOpcion == "0":
            return "Operación finalizada. Regresando al menú principal."
        elif subOpcion == "1":
            listaProductos = leerProductos()
            prodsTexto = "\nProductos disponibles en catálogo:\n"
            for p in listaProductos:
                stockVend = obtenerStockVendiblePorSku(p["sku"], fechaOperacion)
                prodsTexto += f"  [{p['sku']}] {p['nombre']} | Precio: ${p['precioVenta']} | Stock vendible: {stockVend}\n"
            skuIngresado = input(prodsTexto + "Ingrese el código SKU del producto a agregar: ").strip().upper()
            prod = buscarProductoPorSku(skuIngresado)
            if len(prod) == 0:
                raise ValueError(f"Error: El producto con SKU '{skuIngresado}' no existe.")
            cantStr = input(f"¿Cuántas unidades de [{prod['nombre']}] desea agregar?: ").strip()
            if not cantStr.isdigit() or int(cantStr) <= 0:
                raise ValueError("Error: La cantidad a agregar debe ser un número entero mayor a cero.")
            cantidad = int(cantStr)
            stockTotal = obtenerStockVendiblePorSku(skuIngresado, fechaOperacion)
            cantidadActualEnCarrito = carrito.get(skuIngresado, 0)
            cantidadFutura = cantidadActualEnCarrito + cantidad
            advertencia = ""
            if cantidadFutura > stockTotal:
                advertencia = f" (ADVERTENCIA: Stock insuficiente. Hay {stockTotal} disponibles y solicita {cantidadFutura})"
            carrito[skuIngresado] = cantidadFutura
            mensajeEstado = f"Producto {skuIngresado} registrado en el carrito ({carrito[skuIngresado]} unid. en total){advertencia}."
        elif subOpcion == "2":
            if len(carrito) == 0:
                raise ValueError("Error: El carrito está vacío. No hay productos para modificar.")
            itemsTexto = "Ítems actuales en el carrito:\n"
            for s, c in carrito.items():
                itemsTexto += f"  [{s}] Cantidad actual: {c}\n"
            skuModificar = input(itemsTexto + "Ingrese el SKU a modificar: ").strip().upper()
            if skuModificar not in carrito:
                raise ValueError(f"Error: El producto '{skuModificar}' no se encuentra en el carrito.")
            cantStr = input(f"Ingrese la nueva cantidad para {skuModificar} (0 para eliminar): ").strip()
            if not cantStr.isdigit() or int(cantStr) < 0:
                raise ValueError("Error: La cantidad debe ser un número entero mayor o igual a cero.")
            nuevaCantidad = int(cantStr)
            if nuevaCantidad == 0:
                del carrito[skuModificar]
                mensajeEstado = f"Producto {skuModificar} eliminado del carrito."
            else:
                stockTotal = obtenerStockVendiblePorSku(skuModificar, fechaOperacion)
                advertencia = ""
                if nuevaCantidad > stockTotal:
                    advertencia = f" (ADVERTENCIA: Solo hay {stockTotal} unidades vendibles)"
                carrito[skuModificar] = nuevaCantidad
                mensajeEstado = f"Cantidad de {skuModificar} actualizada a {nuevaCantidad}{advertencia}."
        elif subOpcion == "3":
            if len(carrito) == 0:
                raise ValueError("Error: El carrito está vacío.")
            itemsTexto = "Ítems actuales en el carrito:\n"
            for s, c in carrito.items():
                itemsTexto += f"  [{s}] Cantidad: {c}\n"
            skuEliminar = input(itemsTexto + "Ingrese el SKU a eliminar del carrito: ").strip().upper()
            if skuEliminar in carrito:
                del carrito[skuEliminar]
                mensajeEstado = f"Producto {skuEliminar} retirado exitosamente del carrito."
            else:
                raise ValueError(f"Error: El SKU '{skuEliminar}' no está en el carrito.")
        elif subOpcion == "4":
            carrito.clear()
            mensajeEstado = "El carrito ha sido vaciado por completo."
        else:
            raise ValueError("Opción no válida en la gestión del carrito.")

def opcionSimularTotal(carrito, fechaOperacion):
    if len(carrito) == 0:
        raise ValueError("El carrito de compras está vacío. Agregue productos antes de realizar la simulación.")
    salida = "\n" + "=" * 65 + "\n"
    salida += f"REVISIÓN DE DISPONIBILIDAD Y SIMULACIÓN ECONÓMICA (Fecha: {fechaOperacion})\n"
    salida += "=" * 65 + "\n"
    salida += "\n1. VERIFICACIÓN DE DISPONIBILIDAD Y ASIGNACIÓN FEFO:\n"
    salida += "-" * 65 + "\n"
    todoDisponible = True
    subtotal = 0
    for skuItem, cantidadSolicitada in carrito.items():
        pInfo = buscarProductoPorSku(skuItem)
        stockVendible = obtenerStockVendiblePorSku(skuItem, fechaOperacion)
        subtotal += cantidadSolicitada * pInfo["precioVenta"]
        salida += f"SKU: {skuItem} - {pInfo['nombre']}\n"
        salida += f"  Demanda en carrito: {cantidadSolicitada} unid. | Stock vendible actual: {stockVendible} unid.\n"
        if cantidadSolicitada > stockVendible:
            todoDisponible = False
            salida += "  -> [ESTADO]: INSUFICIENTE. Faltan existencias vendibles para cubrir la orden.\n"
        else:
            asignacion = calcularAsignacionFefo(skuItem, cantidadSolicitada, fechaOperacion)
            salida += "  -> [ESTADO]: DISPONIBLE. Asignación por lotes (FEFO):\n"
            for itemAsig in asignacion:
                salida += f"     * Lote: {itemAsig['lote']} (Vence: {itemAsig['vencimiento']}) -> Despacha: {itemAsig['cantidad']} unid.\n"
    salida += "-" * 65 + "\n"
    if not todoDisponible:
        salida += "ADVERTENCIA: No será posible confirmar la venta hasta corregir las cantidades insuficientes.\n"
    promptCliente = salida + (
        "\n2. SIMULACIÓN DE LIQUIDACIÓN Y TARIFAS:\n"
        "Tipos de cliente:\n"
        "  [1] REGULAR (0% de descuento)\n"
        "  [2] PREMIUM (10% de descuento)\n"
        "Seleccione tipo de cliente a simular [1/2]: "
    )
    tipoClienteSel = input(promptCliente).strip()
    if tipoClienteSel not in ["1", "2"]:
        raise ValueError("Opción de cliente inválida. Debe seleccionar 1 para REGULAR o 2 para PREMIUM.")
    esPremium = (tipoClienteSel == "2")
    descuento = int(subtotal * 0.10) if esPremium else 0
    baseImponible = subtotal - descuento
    iva = int(baseImponible * 0.19)
    envio = 5000 if baseImponible < 100000 else 0
    total = baseImponible + iva + envio
    tipoTexto = "PREMIUM (10%)" if esPremium else "REGULAR (0%)"
    salidaLiquidacion = "\n" + "-" * 45 + "\n"
    salidaLiquidacion += "LIQUIDACIÓN ESTIMADA:\n"
    salidaLiquidacion += f"Subtotal productos:        ${subtotal}\n"
    salidaLiquidacion += f"Descuento ({tipoTexto}):   -${descuento}\n"
    salidaLiquidacion += f"Base imponible:            ${baseImponible}\n"
    salidaLiquidacion += f"IVA (19%):                 ${iva}\n"
    salidaLiquidacion += f"Costo de flete/envío:      ${envio} (gratis para compras >= $100.000)\n"
    salidaLiquidacion += f"TOTAL PROYECTADO:          ${total}\n"
    salidaLiquidacion += "-" * 45
    return salidaLiquidacion

def opcionConfirmarVenta(carrito, fechaOperacion):
    if len(carrito) == 0:
        raise ValueError("El carrito de compras está vacío. Agregue productos antes de confirmar.")
    for skuItem, cantidadSolicitada in carrito.items():
        stockVendible = obtenerStockVendiblePorSku(skuItem, fechaOperacion)
        if cantidadSolicitada > stockVendible:
            raise ValueError(f"Error de atomicidad: Stock insuficiente para '{skuItem}'. Solicitado: {cantidadSolicitada}, disponible: {stockVendible}. No se procesó la venta.")
    listaClientes = leerClientes()
    ayudaClientes = "\nClientes registrados en la base de datos:\n"
    for c in listaClientes:
        ayudaClientes += f"  [{c['clienteId']}] {c['nombre']} - Tipo: {c['tipo']}\n"
    clienteId = input(ayudaClientes + "\nIngrese el ID del cliente (ej. C01, C02): ").strip().upper()
    cliente = buscarClientePorId(clienteId)
    if len(cliente) == 0:
        raise ValueError(f"Error: El cliente '{clienteId}' no existe en el sistema.")
    subtotal = 0
    asignacionesGenerales = []
    for skuItem, cantidadSolicitada in carrito.items():
        pInfo = buscarProductoPorSku(skuItem)
        subtotal += cantidadSolicitada * pInfo["precioVenta"]
        asignacionSku = calcularAsignacionFefo(skuItem, cantidadSolicitada, fechaOperacion)
        for asig in asignacionSku:
            asignacionesGenerales.append({
                "sku": skuItem,
                "nombre": pInfo["nombre"],
                "lote": asig["lote"],
                "cantidad": asig["cantidad"],
                "precioUnitario": pInfo["precioVenta"],
                "costoUnitario": asig["costoUnitario"]
            })
    descuento = int(subtotal * 0.10) if cliente["tipo"] == "PREMIUM" else 0
    baseImponible = subtotal - descuento
    iva = int(baseImponible * 0.19)
    envio = 5000 if baseImponible < 100000 else 0
    total = baseImponible + iva + envio
    resumenConfirmacion = (
        "\n" + "=" * 55 + "\n"
        "RESUMEN PREVIO DE FACTURACIÓN\n"
        + "=" * 55 + "\n"
        f"Cliente: {cliente['nombre']} ({cliente['clienteId']}) | Categoría: {cliente['tipo']}\n"
        f"Fecha de transacción: {fechaOperacion}\n"
        f"Subtotal:       ${subtotal}\n"
        f"Descuento:     -${descuento}\n"
        f"Base Imponible: ${baseImponible}\n"
        f"IVA (19%):      ${iva}\n"
        f"Flete de Envío: ${envio}\n"
        f"TOTAL A PAGAR:  ${total}\n"
        + "-" * 55 + "\n"
        "¿Desea confirmar y asentar la venta? (S/N): "
    )
    confirmacion = input(resumenConfirmacion).strip().lower()
    if confirmacion != "s":
        return "Venta cancelada por el usuario. El carrito y el inventario no sufrieron modificaciones."
    nuevaVentaId = generarSiguienteIdVenta()
    listaLotes = leerLotes()
    for asig in asignacionesGenerales:
        for l in listaLotes:
            if l["lote"] == asig["lote"] and l["sku"] == asig["sku"]:
                l["cantidad"] -= asig["cantidad"]
                break
    guardarLotes(listaLotes)
    nuevaVenta = {
        "ventaId": nuevaVentaId,
        "fecha": fechaOperacion,
        "clienteId": cliente["clienteId"],
        "subtotal": subtotal,
        "descuento": descuento,
        "iva": iva,
        "envio": envio,
        "total": total,
        "estado": "CONFIRMADA"
    }
    listaVentas = leerVentas()
    listaVentas.append(nuevaVenta)
    guardarVentas(listaVentas)
    listaDetalles = leerDetalleVentas()
    for asig in asignacionesGenerales:
        nuevoDetalle = {
            "ventaId": nuevaVentaId,
            "sku": asig["sku"],
            "lote": asig["lote"],
            "cantidad": asig["cantidad"],
            "precioUnitario": asig["precioUnitario"],
            "costoUnitario": asig["costoUnitario"]
        }
        listaDetalles.append(nuevoDetalle)
    guardarDetalleVentas(listaDetalles)
    nombreArchivoFactura = f"factura_{nuevaVentaId}_{fechaOperacion}.txt"
    try:
        archivoFactura = open(nombreArchivoFactura, "w")
        archivoFactura.write("=" * 60 + "\n")
        archivoFactura.write("         COMERCIO ELECTRÓNICO - FACTURA DE VENTA\n")
        archivoFactura.write(f"Factura ID: {nuevaVentaId} | Fecha de emisión: {fechaOperacion}\n")
        archivoFactura.write("=" * 60 + "\n")
        archivoFactura.write(f"CLIENTE: {cliente['nombre']} ({cliente['clienteId']})\n")
        archivoFactura.write(f"TIPO:    {cliente['tipo']}\n")
        archivoFactura.write("-" * 60 + "\n")
        archivoFactura.write("DETALLE DE LOTES ENTREGADOS (CRITERIO FEFO):\n")
        archivoFactura.write("{:<8} {:<20} {:<8} {:<8} {:<10}\n".format("SKU", "PRODUCTO", "LOTE", "CANT", "P.UNIT"))
        archivoFactura.write("-" * 60 + "\n")
        for asig in asignacionesGenerales:
            archivoFactura.write("{:<8} {:<20} {:<8} {:<8} ${:<10}\n".format(asig["sku"], asig["nombre"][:20], asig["lote"], asig["cantidad"], asig["precioUnitario"]))
        archivoFactura.write("-" * 60 + "\n")
        archivoFactura.write(f"Subtotal:       ${subtotal}\n")
        archivoFactura.write(f"Descuento:     -${descuento}\n")
        archivoFactura.write(f"Base Imponible: ${baseImponible}\n")
        archivoFactura.write(f"IVA (19%):      ${iva}\n")
        archivoFactura.write(f"Envío:          ${envio}\n")
        archivoFactura.write(f"GRAN TOTAL:     ${total}\n")
        archivoFactura.write("=" * 60 + "\n")
        archivoFactura.close()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error al escribir archivo de factura '{nombreArchivoFactura}'.")
    carrito.clear()
    salida = (
        "\n" + "*" * 55 + "\n"
        "¡TRANSACCIÓN COMPLETADA Y FACTURA EMITIDA EXITOSAMENTE!\n"
        f"Identificador de Factura: {nuevaVentaId}\n"
        f"Monto total cancelado:    ${total}\n"
        f"Archivo físico generado:  '{nombreArchivoFactura}'\n"
        "El inventario por lotes fue actualizado y el carrito ha sido vaciado.\n"
        + "*" * 55
    )
    return salida

def opcionConsultarOAnularVenta(fechaOperacion):
    listaVentas = leerVentas()
    if len(listaVentas) == 0:
        raise ValueError("No existen ventas registradas en el sistema.")
    ayudaVentas = "\nVentas registradas en el sistema:\n"
    for v in listaVentas:
        ayudaVentas += f"  [{v['ventaId']}] Fecha: {v['fecha']} | Cliente: {v['clienteId']} | Total: ${v['total']} | Estado: {v['estado']}\n"
    ventaIdBuscada = input(ayudaVentas + "\nIngrese el ID de la venta a consultar (ej. V0001): ").strip().upper()
    ventaEncontrada = {}
    for v in listaVentas:
        if v["ventaId"] == ventaIdBuscada:
            ventaEncontrada = v
            break
    if len(ventaEncontrada) == 0:
        raise ValueError(f"Error: La venta '{ventaIdBuscada}' no existe en el registro.")
    infoVenta = "\n" + "=" * 55 + "\n"
    infoVenta += f"DETALLE DE LA VENTA {ventaEncontrada['ventaId']}\n"
    infoVenta += "=" * 55 + "\n"
    infoVenta += f"Fecha:        {ventaEncontrada['fecha']}\n"
    infoVenta += f"Cliente ID:   {ventaEncontrada['clienteId']}\n"
    infoVenta += f"Subtotal:     ${ventaEncontrada['subtotal']}\n"
    infoVenta += f"Descuento:    ${ventaEncontrada['descuento']}\n"
    infoVenta += f"IVA:          ${ventaEncontrada['iva']}\n"
    infoVenta += f"Envío:        ${ventaEncontrada['envio']}\n"
    infoVenta += f"Total:        ${ventaEncontrada['total']}\n"
    infoVenta += f"Estado:       {ventaEncontrada['estado']}\n"
    infoVenta += "\nLotes involucrados en la transacción:\n"
    listaDetalles = leerDetalleVentas()
    detallesVenta = []
    for d in listaDetalles:
        if d["ventaId"] == ventaIdBuscada:
            detallesVenta.append(d)
            pInfo = buscarProductoPorSku(d["sku"])
            nombreP = pInfo["nombre"] if len(pInfo) > 0 else "Desconocido"
            infoVenta += f"  * SKU: {d['sku']} ({nombreP}) | Lote: {d['lote']} | Cantidad: {d['cantidad']} | Precio Unit: ${d['precioUnitario']}\n"
    if ventaEncontrada["estado"] == "ANULADA":
        infoVenta += "\n[AVISO]: Esta venta ya se encuentra ANULADA. No es posible anularla nuevamente."
        return infoVenta
    promptAnular = (
        infoVenta + "\n" + "-" * 55 + "\n"
        "¿Desea ANULAR completamente esta venta y reintegrar el stock a sus lotes?\n"
        "Escriba 'SI' para proceder con la reversión: "
    )
    confirmar = input(promptAnular).strip().upper()
    if confirmar != "SI":
        return "Operación cancelada. La venta se mantiene en estado CONFIRMADA."
    motivo = input("Ingrese el motivo justificado de la anulación: ").strip()
    if motivo == "":
        motivo = "Cancelación solicitada por cliente"
    listaLotes = leerLotes()
    for d in detallesVenta:
        loteRestaurado = False
        for l in listaLotes:
            if l["lote"] == d["lote"] and l["sku"] == d["sku"]:
                l["cantidad"] += d["cantidad"]
                loteRestaurado = True
                break
        if not loteRestaurado:
            nuevoLoteRest = {
                "lote": d["lote"],
                "sku": d["sku"],
                "vencimiento": "2099-12-31",
                "cantidad": d["cantidad"],
                "costoUnitario": d["costoUnitario"]
            }
            listaLotes.append(nuevoLoteRest)
    guardarLotes(listaLotes)
    ventaEncontrada["estado"] = "ANULADA"
    guardarVentas(listaVentas)
    registrarAnulacion(ventaIdBuscada, fechaOperacion, motivo)
    salida = (
        "\n" + "*" * 55 + "\n"
        f"¡VENTA {ventaIdBuscada} ANULADA Y REVERTIDA EXITOSAMENTE!\n"
        "Las unidades han sido reintegradas íntegramente a sus lotes de origen.\n"
        "Registro de auditoría almacenado en anulaciones.csv.\n"
        + "*" * 55
    )
    return salida

def opcionIngresarMercancia(fechaOperacion):
    salidaEncabezado = "\n" + "=" * 55 + "\n"
    salidaEncabezado += "INGRESAR NUEVA MERCANCÍA / AJUSTAR STOCK CON MOTIVO\n"
    salidaEncabezado += "=" * 55 + "\n"
    listaProductos = leerProductos()
    ayudaProds = salidaEncabezado + "Productos registrados en catálogo:\n"
    for p in listaProductos:
        ayudaProds += f"  [{p['sku']}] {p['nombre']} ({p['categoria']})\n"
    skuIngresado = input(ayudaProds + "\nIngrese el código SKU del producto (ej. P01): ").strip().upper()
    prod = buscarProductoPorSku(skuIngresado)
    if len(prod) == 0:
        raise ValueError(f"Error: El SKU '{skuIngresado}' no existe en el catálogo.")
    listaLotes = leerLotes()
    lotesDelSku = []
    for l in listaLotes:
        if l["sku"] == skuIngresado:
            lotesDelSku.append(f"{l['lote']} (Vence: {l['vencimiento']}, Stock: {l['cantidad']})")
    ayudaLotes = f"\nProducto: {prod['nombre']} ({prod['categoria']})\n"
    if len(lotesDelSku) > 0:
        ayudaLotes += "Lotes existentes para este producto: " + ", ".join(lotesDelSku) + "\n"
    loteId = input(ayudaLotes + "Ingrese el identificador del lote (ej. L01 o nuevo como L08): ").strip().upper()
    if loteId == "":
        raise ValueError("Error: El identificador del lote no puede estar vacío.")
    vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ").strip()
    if not validarFormatoFecha(vencimiento):
        raise ValueError("Error: Formato de fecha de vencimiento inválido. Debe cumplir YYYY-MM-DD.")
    cantStr = input("Ingrese la cantidad a ingresar (> 0): ").strip()
    if not cantStr.isdigit() or int(cantStr) <= 0:
        raise ValueError("Error: La cantidad debe ser un número entero estrictamente positivo.")
    cantidad = int(cantStr)
    costoStr = input("Ingrese el costo unitario de adquisición (>= 0): ").strip()
    if not costoStr.isdigit() or int(costoStr) < 0:
        raise ValueError("Error: El costo unitario debe ser un valor entero no negativo.")
    costo = int(costoStr)
    motivo = input("Ingrese el motivo del ingreso o ajuste de inventario: ").strip()
    if motivo == "":
        motivo = "Reposición de inventario"
    loteExistente = {}
    for l in listaLotes:
        if l["lote"] == loteId:
            loteExistente = l
            break
    mensajeLote = ""
    if len(loteExistente) > 0:
        if loteExistente["sku"] != skuIngresado:
            raise ValueError(f"Error de integridad: El lote '{loteId}' ya existe para el producto {loteExistente['sku']}, no para {skuIngresado}.")
        if loteExistente["vencimiento"] != vencimiento:
            raise ValueError(f"Error de integridad: El lote '{loteId}' ya existe con fecha de vencimiento diferente ({loteExistente['vencimiento']}).")
        loteExistente["cantidad"] += cantidad
        loteExistente["costoUnitario"] = costo
        mensajeLote = f"Lote existente '{loteId}' actualizado: nuevo stock {loteExistente['cantidad']} unidades."
    else:
        nuevoLote = {
            "lote": loteId,
            "sku": skuIngresado,
            "vencimiento": vencimiento,
            "cantidad": cantidad,
            "costoUnitario": costo
        }
        listaLotes.append(nuevoLote)
        mensajeLote = f"Nuevo lote '{loteId}' creado con éxito con {cantidad} unidades."
    guardarLotes(listaLotes)
    salida = (
        "\n" + "-" * 55 + "\n"
        "INGRESO DE MERCANCÍA ASENTADO CON ÉXITO\n"
        f"{mensajeLote}\n"
        f"Producto: {prod['nombre']} ({prod['sku']})\n"
        f"Motivo registrado: {motivo}\n"
        + "-" * 55
    )
    return salida

def opcionReportesComerciales(fechaOperacion):
    menuReportes = (
        "\n" + "=" * 60 + "\n"
        "MÓDULO DE REPORTES Y ANÁLISIS COMERCIAL\n"
        + "=" * 60 + "\n"
        "1. Unidades vendidas por categoría y Top 3 SKU (Exporta ventas_por_categoria.csv)\n"
        "2. Top 3 clientes por valor pagado (excluye anulaciones)\n"
        "3. Alertas de stock crítico (< 5) y lotes vencidos\n"
        "4. Generar reporte consolidado completo (Exporta informe_comercial.txt)\n"
        "0. Regresar al menú principal\n"
        "------------------------------------------------------------\n"
    )
    subOpcion = input(menuReportes + "Seleccione un reporte [0-4]: ").strip()
    listaVentas = leerVentas()
    listaDetalles = leerDetalleVentas()
    listaProductos = leerProductos()
    listaLotes = leerLotes()
    if subOpcion == "0":
        return "Regresando al menú principal."
    elif subOpcion == "1":
        ventasActivasIds = []
        for v in listaVentas:
            if v["estado"] == "CONFIRMADA":
                ventasActivasIds.append(v["ventaId"])
        unidadesPorCategoria = {}
        unidadesPorSku = {}
        for d in listaDetalles:
            if d["ventaId"] in ventasActivasIds:
                pInfo = buscarProductoPorSku(d["sku"])
                cat = pInfo["categoria"]
                unidadesPorCategoria[cat] = unidadesPorCategoria.get(cat, 0) + d["cantidad"]
                unidadesPorSku[d["sku"]] = unidadesPorSku.get(d["sku"], 0) + d["cantidad"]
        salida = "\nUNIDADES VENDIDAS NETAS POR CATEGORÍA:\n"
        salida += "{:<18} {:<15}\n".format("CATEGORÍA", "UNIDADES NETAS")
        salida += "-" * 35 + "\n"
        for cat, cUds in unidadesPorCategoria.items():
            salida += "{:<18} {:<15}\n".format(cat, cUds)
        salida += "-" * 35 + "\n"
        listaSkuOrdenada = []
        for skuKey, uds in unidadesPorSku.items():
            listaSkuOrdenada.append({"sku": skuKey, "unidades": uds})
        for i in range(len(listaSkuOrdenada)):
            for j in range(len(listaSkuOrdenada) - 1):
                cambiar = False
                if listaSkuOrdenada[j + 1]["unidades"] > listaSkuOrdenada[j]["unidades"]:
                    cambiar = True
                elif listaSkuOrdenada[j + 1]["unidades"] == listaSkuOrdenada[j]["unidades"]:
                    if listaSkuOrdenada[j + 1]["sku"] < listaSkuOrdenada[j]["sku"]:
                        cambiar = True
                if cambiar:
                    temp = listaSkuOrdenada[j]
                    listaSkuOrdenada[j] = listaSkuOrdenada[j + 1]
                    listaSkuOrdenada[j + 1] = temp
        top3Sku = listaSkuOrdenada[:3]
        salida += "\nTOP 3 PRODUCTOS (SKU) POR UNIDADES VENDIDAS:\n"
        pos = 1
        for item in top3Sku:
            pInfo = buscarProductoPorSku(item["sku"])
            salida += f"{pos}. {item['sku']} - {pInfo['nombre']}: {item['unidades']} unidades\n"
            pos += 1
        try:
            archivoCat = open("ventas_por_categoria.csv", "w")
            archivoCat.write("categoria,unidades_vendidas\n")
            for cat, cUds in unidadesPorCategoria.items():
                archivoCat.write(f"{cat},{cUds}\n")
            archivoCat.close()
            salida += "\nReporte exportado exitosamente a 'ventas_por_categoria.csv'."
        except FileNotFoundError:
            raise FileNotFoundError("Error al exportar 'ventas_por_categoria.csv'.")
        return salida
    elif subOpcion == "2":
        pagosPorCliente = {}
        for v in listaVentas:
            if v["estado"] == "CONFIRMADA":
                cId = v["clienteId"]
                pagosPorCliente[cId] = pagosPorCliente.get(cId, 0) + v["total"]
        listaClientesOrdenada = []
        for cId, monto in pagosPorCliente.items():
            listaClientesOrdenada.append({"clienteId": cId, "total": monto})
        for i in range(len(listaClientesOrdenada)):
            for j in range(len(listaClientesOrdenada) - 1):
                cambiar = False
                if listaClientesOrdenada[j + 1]["total"] > listaClientesOrdenada[j]["total"]:
                    cambiar = True
                elif listaClientesOrdenada[j + 1]["total"] == listaClientesOrdenada[j]["total"]:
                    if listaClientesOrdenada[j + 1]["clienteId"] < listaClientesOrdenada[j]["clienteId"]:
                        cambiar = True
                if cambiar:
                    temp = listaClientesOrdenada[j]
                    listaClientesOrdenada[j] = listaClientesOrdenada[j + 1]
                    listaClientesOrdenada[j + 1] = temp
        top3Clientes = listaClientesOrdenada[:3]
        salida = "\nTOP 3 CLIENTES POR VALOR PAGADO (EXCLUYE ANULACIONES):\n"
        salida += "-" * 55 + "\n"
        pos = 1
        for item in top3Clientes:
            cInfo = buscarClientePorId(item["clienteId"])
            nom = cInfo["nombre"] if len(cInfo) > 0 else "Desconocido"
            salida += f"{pos}. {item['clienteId']} - {nom}: ${item['total']}\n"
            pos += 1
        salida += "-" * 55
        return salida
    elif subOpcion == "3":
        salida = "\nALERTAS DE STOCK CRÍTICO VENDIBLE (< 5 UNIDADES):\n"
        salida += "{:<8} {:<22} {:<15}\n".format("SKU", "NOMBRE", "STOCK VENDIBLE")
        salida += "-" * 45 + "\n"
        algunCritico = False
        for p in listaProductos:
            stockVend = obtenerStockVendiblePorSku(p["sku"], fechaOperacion)
            if stockVend < 5:
                algunCritico = True
                salida += "{:<8} {:<22} {:<15}\n".format(p["sku"], p["nombre"], stockVend)
        if not algunCritico:
            salida += "No hay productos con stock vendible menor a 5 unidades.\n"
        salida += "-" * 45 + "\n"
        salida += "\nLISTADO DE LOTES VENCIDOS A LA FECHA:\n"
        salida += "{:<8} {:<8} {:<12} {:<10}\n".format("LOTE", "SKU", "VENCIMIENTO", "CANTIDAD")
        salida += "-" * 45 + "\n"
        algunVencido = False
        for l in listaLotes:
            if l["vencimiento"] < fechaOperacion and l["cantidad"] > 0:
                algunVencido = True
                salida += "{:<8} {:<8} {:<12} {:<10}\n".format(l["lote"], l["sku"], l["vencimiento"], l["cantidad"])
        if not algunVencido:
            salida += "No hay lotes con fecha vencida y stock remanente.\n"
        salida += "-" * 45
        return salida
    elif subOpcion == "4":
        try:
            archInf = open("informe_comercial.txt", "w")
            archInf.write("=" * 60 + "\n")
            archInf.write("           INFORME COMERCIAL DE OPERACIONES\n")
            archInf.write(f"Fecha de corte: {fechaOperacion}\n")
            archInf.write("=" * 60 + "\n\n")
            ventasActivasIds = []
            totalRecaudadoNeto = 0
            for v in listaVentas:
                if v["estado"] == "CONFIRMADA":
                    ventasActivasIds.append(v["ventaId"])
                    totalRecaudadoNeto += v["total"]
            archInf.write(f"TOTAL RECAUDADO (VENTAS ACTIVAS): ${totalRecaudadoNeto}\n\n")
            unidadesPorCategoria = {}
            for d in listaDetalles:
                if d["ventaId"] in ventasActivasIds:
                    pInfo = buscarProductoPorSku(d["sku"])
                    cat = pInfo["categoria"]
                    unidadesPorCategoria[cat] = unidadesPorCategoria.get(cat, 0) + d["cantidad"]
            archInf.write("VENTAS NETAS POR CATEGORÍA:\n")
            for cat, cant in unidadesPorCategoria.items():
                archInf.write(f"- {cat}: {cant} unidades\n")
            archInf.write("\nALERTAS DE STOCK VENDIBLE (< 5 UNIDADES):\n")
            for p in listaProductos:
                stockVend = obtenerStockVendiblePorSku(p["sku"], fechaOperacion)
                if stockVend < 5:
                    archInf.write(f"- {p['sku']} ({p['nombre']}): {stockVend} unidades\n")
            archInf.write("\nLOTES VENCIDOS:\n")
            for l in listaLotes:
                if l["vencimiento"] < fechaOperacion and l["cantidad"] > 0:
                    archInf.write(f"- Lote {l['lote']} ({l['sku']}): Venció {l['vencimiento']} | Quedan {l['cantidad']}\n")
            archInf.close()
            salida = "\n" + "=" * 55 + "\n"
            salida += "Reporte consolidado exportado exitosamente a 'informe_comercial.txt'.\n"
            salida += f"Total recaudado activo: ${totalRecaudadoNeto}\n"
            salida += "=" * 55
            return salida
        except FileNotFoundError:
            raise FileNotFoundError("Error al exportar 'informe_comercial.txt'.")
    else:
        raise ValueError("Opción inválida en reportes. Seleccione un número entre 0 y 4.")

def menuPrincipal():
    fechaOperacion = "2026-11-10"
    carrito = {}
    while True:
        menuTexto = "\n" + "=" * 65 + "\n"
        menuTexto += "SISTEMA DE GESTIÓN DE COMERCIO ELECTRÓNICO\n"
        menuTexto += f"Fecha activa de operación: {fechaOperacion} | Carrito: {len(carrito)} ítem(s)\n"
        menuTexto += "=" * 65 + "\n"
        menuTexto += "1. Listar catálogo y detalle de lotes\n"
        menuTexto += "2. Gestionar carrito de compras\n"
        menuTexto += "3. Simular disponibilidades y liquidación\n"
        menuTexto += "4. Confirmar venta y emitir factura\n"
        menuTexto += "5. Consultar y/o anular venta\n"
        menuTexto += "6. Registrar entrada de mercancía / ajuste de stock\n"
        menuTexto += "7. Generar análisis y reportes comerciales\n"
        menuTexto += "8. Cambiar fecha de operación del sistema\n"
        menuTexto += "0. Salir\n"
        menuTexto += "=================================================================\n"
        opcion = input(menuTexto + "Seleccione una opción [0-8]: ").strip()
        try:
            if opcion == "1":
                resultado = opcionListarProductosYLotes(fechaOperacion)
                if resultado != "":
                    print(resultado)
            elif opcion == "2":
                resultado = opcionGestionarCarrito(carrito, fechaOperacion)
                if resultado != "":
                    print(resultado)
            elif opcion == "3":
                resultado = opcionSimularTotal(carrito, fechaOperacion)
                if resultado != "":
                    print(resultado)
            elif opcion == "4":
                resultado = opcionConfirmarVenta(carrito, fechaOperacion)
                if resultado != "":
                    print(resultado)
            elif opcion == "5":
                resultado = opcionConsultarOAnularVenta(fechaOperacion)
                if resultado != "":
                    print(resultado)
            elif opcion == "6":
                resultado = opcionIngresarMercancia(fechaOperacion)
                if resultado != "":
                    print(resultado)
            elif opcion == "7":
                resultado = opcionReportesComerciales(fechaOperacion)
                if resultado != "":
                    print(resultado)
            elif opcion == "8":
                nuevaFecha = input(f"Fecha actual del sistema: {fechaOperacion}\nIngrese la nueva fecha de corte (YYYY-MM-DD): ").strip()
                if not validarFormatoFecha(nuevaFecha):
                    raise ValueError("Error: Formato de fecha inválido. Utilice el patrón YYYY-MM-DD.")
                fechaOperacion = nuevaFecha
                print(f"Fecha de operación actualizada exitosamente a: {fechaOperacion}")
            elif opcion == "0":
                print("Sesión finalizada. ¡Gracias por utilizar el sistema de comercio electrónico!")
                break
            else:
                raise ValueError("Opción no válida. Por favor digite un número del 0 al 8.")
        except (ValueError, FileNotFoundError, ZeroDivisionError, IndexError) as err:
            print(f"{err}")

menuPrincipal()
