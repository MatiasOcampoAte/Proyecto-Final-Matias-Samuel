# Sistema de Gestión de Comercio Electrónico

## 1. Descripción del proyecto

Este proyecto implementa un sistema de gestión de comercio electrónico
desarrollado en Python. Permite consultar el catálogo de productos y sus
lotes, administrar un carrito de compras, simular el valor de una
compra, confirmar ventas, emitir facturas, consultar o anular ventas,
registrar entradas de mercancía y generar reportes comerciales.

La información se almacena en archivos CSV locales, por lo que no es
necesario configurar una base de datos externa.

## 2. Requisitos

Antes de ejecutar el proyecto, asegúrese de tener:

-   Python 3 instalado.
-   Los archivos del proyecto descargados en una misma carpeta.
-   Una terminal o consola para ejecutar el programa.

El programa utiliza funcionalidades de la biblioteca estándar de Python.
**No requiere instalar paquetes externos ni ejecutar comandos
`pip install`.**

Para comprobar que Python está instalado, abra una terminal y ejecute:

``` bash
python --version
```

En algunos equipos puede ser necesario utilizar:

``` bash
py --version
```

## 3. Estructura de archivos

Todos los archivos CSV que utiliza el programa deben estar en la misma
carpeta que `comercio.py`. La estructura recomendada es:

``` text
comercio-electronico/
│
├── comercio.py
├── productos.csv
├── lotes.csv
├── clientes.csv
├── ventas.csv
├── detalle_ventas.csv
├── anulaciones.csv
└── ventas_por_categoria.csv
```

> **Importante:** los archivos adjuntos o descargados pueden tener un
> sufijo como `(1)` en el nombre. Antes de ejecutar el programa,
> renómbrelos exactamente como aparecen en la estructura anterior. Por
> ejemplo, `productos(1).csv` debe llamarse `productos.csv`. También
> debe renombrar `comercio(2).py` como `comercio.py`.

### Archivos CSV utilizados

  ----------------------------------------------------------------------------
  Archivo                      Función                 Columnas
  ---------------------------- ----------------------- -----------------------
  `productos.csv`              Catálogo de productos,  `sku`, `nombre`,
                               categorías y precios de `categoria`,
                               venta.                  `precio_venta`

  `lotes.csv`                  Inventario por lotes,   `lote`, `sku`,
                               fechas de vencimiento,  `vencimiento`,
                               cantidades y costos.    `cantidad`,
                                                       `costo_unitario`

  `clientes.csv`               Clientes registrados y  `cliente_id`, `nombre`,
                               su tipo (REGULAR o      `tipo`
                               PREMIUM).               

  `ventas.csv`                 Registro general de las `venta_id`, `fecha`,
                               ventas y sus valores.   `cliente_id`,
                                                       `subtotal`,
                                                       `descuento`, `iva`,
                                                       `envio`, `total`,
                                                       `estado`

  `detalle_ventas.csv`         Productos y lotes       `venta_id`, `sku`,
                               asociados a cada venta. `lote`, `cantidad`,
                                                       `precio_unitario`,
                                                       `costo_unitario`

  `anulaciones.csv`            Registro de auditoría   `venta_id`,
                               de las ventas anuladas. `fecha_anulacion`,
                                                       `motivo`

  `ventas_por_categoria.csv`   Archivo de salida del   `categoria`,
                               reporte de unidades     `unidades_vendidas`
                               vendidas por categoría. 
  ----------------------------------------------------------------------------

Los archivos CSV deben conservar sus encabezados y el orden de las
columnas. Los campos numéricos deben contener valores enteros. Evite
incluir comas dentro de los datos de texto, porque el programa separa
las columnas utilizando ese carácter.

`ventas_por_categoria.csv` es generado o sobrescrito por la opción
correspondiente del módulo de reportes. Puede conservarse en la carpeta
para tener disponible el resultado de la última generación.

## 4. Instalación y ejecución

Siga estos pasos para ejecutar el proyecto desde cero:

1.  Descargue o clone el repositorio de GitHub en su computador.

2.  Descomprima el proyecto, si lo descargó como archivo ZIP.

3.  Verifique que `comercio.py` y todos los archivos CSV estén dentro de
    la misma carpeta.

4.  Compruebe que los nombres de los archivos coincidan exactamente con
    los indicados en la sección anterior.

5.  Abra una terminal en la carpeta del proyecto.

6.  Ejecute el programa con:

    ``` bash
    python comercio.py
    ```

    Si utiliza Windows y el comando anterior no funciona, pruebe:

    ``` bash
    py comercio.py
    ```

7.  El menú principal aparecerá en la terminal. Seleccione la opción
    deseada e ingrese los datos que solicite el sistema.

No es necesario crear un entorno virtual ni instalar dependencias
adicionales para ejecutar la versión actual del proyecto.

## 5. Funcionalidades del sistema

El menú principal ofrece las siguientes opciones:

  -----------------------------------------------------------------------
  Opción                              Funcionalidad
  ----------------------------------- -----------------------------------
  1                                   Consultar el catálogo completo y el
                                      stock vendible, filtrar productos
                                      por categoría y consultar los lotes
                                      de un SKU.

  2                                   Gestionar el carrito: agregar
                                      productos, modificar cantidades,
                                      eliminar productos o vaciar el
                                      carrito.

  3                                   Simular la disponibilidad de los
                                      productos y calcular subtotal,
                                      descuento, IVA, envío y total
                                      estimado.

  4                                   Confirmar una venta, actualizar el
                                      inventario, guardar el registro de
                                      venta y generar una factura en
                                      formato TXT.

  5                                   Consultar una venta o anularla,
                                      reintegrando las unidades a los
                                      lotes correspondientes y
                                      registrando el motivo de la
                                      anulación.

  6                                   Registrar entradas de mercancía o
                                      ajustar el stock de un lote
                                      existente.

  7                                   Generar reportes comerciales y
                                      consultar alertas de inventario.

  8                                   Cambiar la fecha de operación
                                      utilizada para evaluar vencimientos
                                      y disponibilidad.

  0                                   Finalizar la ejecución del
                                      programa.
  -----------------------------------------------------------------------

### Reglas principales de operación

-   **Asignación FEFO:** al despachar productos, el sistema prioriza los
    lotes cuya fecha de vencimiento es más próxima.
-   **Stock vendible:** solo se consideran lotes con cantidad mayor que
    cero y fecha de vencimiento igual o posterior a la fecha de
    operación.
-   **Clientes PREMIUM:** reciben un descuento del 10 %. Los clientes
    REGULAR no reciben descuento.
-   **IVA:** se calcula con una tarifa del 19 % sobre la base imponible.
-   **Envío:** se cobran \$5.000 cuando la base imponible es inferior a
    \$100.000. Para compras iguales o superiores a ese valor, el envío
    es gratuito.
-   **Anulaciones:** una venta anulada cambia su estado a `ANULADA` y
    las unidades se reintegran al inventario de sus lotes de origen.

## 6. Archivos generados durante la ejecución

Además de consultar y actualizar los CSV existentes, el programa puede
crear los siguientes archivos en la carpeta desde la que se ejecuta:

-   `factura_VXXXX_YYYY-MM-DD.txt`: factura de cada venta confirmada. El
    identificador y la fecha varían según la operación.
-   `ventas_por_categoria.csv`: reporte de unidades vendidas netas por
    categoría, generado desde la opción 7.1.
-   `informe_comercial.txt`: reporte consolidado, generado desde la
    opción 7.4.

El sistema también actualiza `lotes.csv`, `ventas.csv` y
`detalle_ventas.csv` cuando se confirma una venta o se modifica el
inventario. Las anulaciones se agregan a `anulaciones.csv`.

**Recomendación:** realice una copia de seguridad de los archivos CSV
antes de probar operaciones que confirmen ventas, anulen ventas o
modifiquen el inventario, ya que estas acciones escriben cambios en los
archivos.

## 7. Solución de problemas

-   **No se encuentra un archivo CSV:** compruebe que todos los archivos
    estén en la misma carpeta que `comercio.py` y que sus nombres no
    conserven sufijos como `(1)`.
-   **Error al convertir un número:** revise que las columnas de
    cantidades, precios, costos, descuentos e impuestos contengan
    números enteros válidos.
-   **No aparece el menú:** confirme que Python esté instalado y que
    esté ejecutando el comando desde la carpeta correcta.
-   **No se genera una factura o reporte:** compruebe que la carpeta
    tenga permisos de escritura y que el programa no esté siendo
    ejecutado desde una ubicación protegida.

## 8. Tecnologías utilizadas

-   **Python 3:** lenguaje de programación utilizado para implementar la
    lógica del sistema.
-   **Archivos CSV:** almacenamiento local de productos, lotes,
    clientes, ventas y detalles.
-   **Biblioteca estándar de Python:** lectura y escritura de archivos,
    validaciones, estructuras de datos y operaciones del sistema.

## 9. Autor

Proyecto académico de gestión de comercio electrónico:
 Samuel lopez 
 Matias Ocampo

------------------------------------------------------------------------

Para utilizar el sistema, descargue el repositorio completo y siga las
instrucciones de instalación y ejecución descritas en este documento.
