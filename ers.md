# Introducción.

El presente documento detalla los requisitos para el desarrollo de un módulo para el
control de activos fijos sobre la plataforma Cacao Accounting. Cacao Accounting presenta
la base para el control de las operaciones financieras de una entidad, consta de los módulos
necesarios para el control de Compras, Ventas, Almacenes y Contabilidad General.

Muchas entidades pequeñas no requieren de un control estricto sobre sus Activos Fijos ya
que no cuentan con mucho mobiliario o equipo que controlar, sin embargo, para una entidad mediana
la cantidad de bienes con que cuentan requiere un control especifico
de sus activos fijos ya estos equipos representan en conjunto con sus recursos humanos
la base para que la entidad opere.

## Proposito.

Un módulo de Activo Fijo debe proporcionar información clara, precisa y confiable sobre:

1. Los bienes, maquinarias y demás recursos productivos con que cuenta la entidad.
2. El valor de los Activos Fijos de la entidad considerando:
   1. Su costo de adquisición.
   2. La vida útil estimada del activo fijo.
   3. La depreciación acumulada de los activos fijos.
   4. El valor contable de los activos fijos de la entidad.
        1. Se entiende como valor contable para fines de este documento el valor de adquisición
        del activo menos la depreciación en línea recta del bien según la vida útil estimada.
3. Para fines de presentación complementaria muchas entidades pueden requerir la presentación de
   información adicional en una moneda secundaria a la moneda funcional con que opera la entidad,
   para tal efecto el módulo de activo deber ser capaz de llevar los control de valor contable
   en la moneda funcional de la empresa y una moneda secundaria tomando como base la tasa de
   cambio entre ambas monedas a la fecha de adquisición del activo fijo.
4. Para fines de presentación de información financiera muchas entidades podrán optar por revaluar
   sus activos fijos, para tal efecto el módulo de Activo Fijo debe ser capaz de controlar el valor
   de los revaluos y amortizarlos por el plazo estimado por el perito valuador.
5. La legislación fiscal del país en opera la entidad puede especificar
  normas especiales de valoración de activos fijos y períodos de vida
  útil distintos a los establecidos por la política contable de la entidad
  el módulo deberá ser capaz de llevar control del valor fiscal de los
  activo de la entidad.
    1. Se entiende como valor fiscal el costo de adquisición del bien
       según la legislación fiscal del país es que opera la entidad
       menos la depreciación en línea recta del bien según la vida 
       útil establecida por la legislación fiscal.
6. Como parte de su mantenimiento mucho bienes son sujetos a reparaciones y cambios de fecha que deben
   ser  reconocidos como un aumento del valor del valor de los equipos y una modificación a su vida
   útil la cual debe ser controlada por módulo de activo fijo.
7. Si bien no son bienes tangibles físicamente muchos activos como
   patentes legales, licencias de software, permisos, concesiones,
   plantaciones y similares que deben ser amortizados o agotados en
   períodos mayores a un año pueden controlarse con un módulo de 
   Activo Fijo.

## Ámbito del Sistema.

El módulo de Activo Fijo está pensando para ejecutarse en un entorno
cliente servidor sobre la plataforma de [Cacao Accounting](https://github.com/cacao-accounting/cacao-accounting/) la cual
está desarrollada en [python](https://www.python.org/).

# Descripción General.

Módulo para el control de activos fijos.

## Perspectiva del Producto.

Un módulo que puede incorporarse en una instalación existente de la
plataforma Cacao Accounting incorporándose a nivel de base de datos
y en la interfaz de usuario.

## Funciones del Producto.

Una vez terminado el módulo deberá tener las siguientes funcionalidades.

### Control de Familias de Activo Fijo.

Los Activos Fijos deberán poder agruparse por familias, una familia
de Activo Fijo debe agrupar equipos similares.

La definición de familias de equipos debe poder hacerse en una jerarquía
de árbol (Padres e Hijos) por ejemplo:

```
Mobiliario y Equipo de Oficina
  |- Equipos de Computo
  |  |- Computadoras portátiles y de escritorio 
  |  |- Impresoras
  |  |- Servidores y Equipo de Red
  |- Mobiliario
  |  |- Equipo de Oficina
  |  |- Archivos
Equipo Rodante
  |- Vehículos de Reparto
  |- Vehículos Uso Administrativo
  |- Cargadoras
```

En la jerarquía de familias los niveles que agrupan otras familias no
podrán ser asignadas a un Activo Fijo individual.

La familia de Activo Fijos deberá definir obligatoriamente una cuenta
de balance para el alta de Activos Fijos y una cuenta de depreciación.

Una vez dado de alta un Activo Fijo no podrá cambiarse de familia.

La familia de Activo Fijo debe definir obligatoriamente la vida útil
contable de los activos definidos a esa familia de activos, opcionalmente
podra definir una depreciación fiscal acorde a la legislación local
de la entidad.
 
### Control de Ubicaciones de Activo Fijo.

Similar a las ubicaciones los Activos Fijos podrán ubicarse a una 
aréa física u operativa de la empresa.

```
Administración
  |- Gerencia Financiera
  |  |- Contabilidad
  |  |- Tesoreria
  |- Gerencia Operaciones
  |  |- Almacen 
  |  |- Transporte
Ventas
  |- Sucursal A
  |- Sucursal B
  |- Sucursal C
```

En la jerarquía de ubicaciones los niveles que agrupan otras ubicaciones 
no podrán ser asignadas a un Activo Fijo individual.

La ubicación del Activo Fijo deberá definir obligatoriamente una cuenta de Resultado (Gastos) para cargar la cuota de depreciación correspondiente.

Una vez dado de alta un Activo Fijo podrá cambiarse de ubicación.

### Activo Fijo Agrupador.

En algunos casos un activo fijo puede estar formado por varias partes
identificables y a los que se puede establecer un valor determinado y pueden controlarse por separado, incluso tener un período de vida útil distinto, por ejemplo

```
GRUA VERTICAL HASTA 300 TM
 |- Motor
 |- Contrapeso
 |- Equipo de Control
```

Al momento de crear un Activo Fijo deberá poder especificarse si:

1. Es un Activo Fijo Individual.
2. Es un Activo Fijo Agrupador.
3. Es un componente de un Activo Fijo agrupador.

Todos los componentes de un Activo Fijo Agrupador deben heredar la
misma ubicación, pero podrán pertenecer a distintas familias de Activo
Fijo.

### Alta de Activo Fijo.

El sistema deberá permitir la creación de nuevos registros de Activo Fijo es los que se podrá especificar.

1. Fecha del Alta.
1. Código Definido por el Usuario opcional.
1. Si es un Activo Fijo físico o un registro amortizable.
1. Solo en caso que sea un Activo Fijo físico especificar si es:
    1. Es un Activo Fijo Individual.
    2. Es un Activo Fijo Agrupador.
    3. Es un componente de un Activo Fijo agrupador.
1. Marca
1. Modelo
1. Descripción
1. Número de Serie
1. En caso que sea un automotor:
    1. Código de Motor.
    1. Código de Chasis.
    1. Placa
    1. Número de Registro.
1. Ubicación.
1. Familia
1. Valor del Activo Fijo según la moneda predeterminada de la entidad.
1. Opcionalmente una moneda secundaria para control.
1. Tasa de Cambio a utilizar entre la moneda principal y moneda secundaria.

Al momento de definir el alta de un nuevo Activo Fijo el módulo deberá
establecer un código único para el registro.

### Baja de Activo Fijo.

Según el código único del Activo Fijo se podrá dar de baja un registro
de Activo Fijo detallando:

1. Fecha de la Baja.
1. Razón de la Baja.
1. En caso que el activo aún no esté totalmente depreciado el usuario
deberá especificar una cuenta contable para cargar el saldo pendiente
de depreciar.

### Traslado de Activo Fijo.

Según el código único del se podrá cambiar de una ubicación a otra.

### Listado de Activo Fijo.

Un reporte tipo lista paginada que liste todos los registros de activo
fijo de una entidad y permita aplicar filtros.

### Revaluaciones de Activo Fijo.

Según el código de un Activo Fijo poder establecer el valor de avaluo
practicado por un perito.

El usuario deberá establecer:

1. Una cuenta acreedora y una cuenta deudora para el registro.
2. La vida útil estimada por el perito valuador.
3. Una cuenta para el registro de la amortización del avaluó.
4. Tasa de Cambio de la fecha de alta del avaluó.


En el caso de Activos Fijos agrupadores el avaluó deberá aplicarse
a cada uno de sus componentes.

Las revaluaciones deberán darse de baja junto con el Activo Fijo al
que están relacionadas.

### Capitalización de Mejoras.

Cuando se haya una reparación mayor a un Activo Fijo que prolongue
su vida útil se deberá registrar el valor de la mejora y la nueva vida
útil para depreciación y la tasa de cambio de la fecha de la capitalización.

Las capitalizaciones deberán darse de baja junto con el Activo Fijo al
que están relacionadas.

### Cálculo de la depreciación.

El módulo deberá hacer los cálculos de:

1. Depreciación Contable.
   1. Valor Adquisición / Vida Útil Contable Expresada en Meses.
   1. (Valor Adquisición / TC Fecha Adquisición) / Vida Útil Contable Expresada en Meses.
2. Amortización Revaluós.
   1. Monto Revaluación / Vida Útil Amortización Expresada en Meses.
   1. (Monto Revaluación / TC Fecha Avaluó) / Vida Útil Amortización Expresada en Meses.
3. Amortización Mejoras Capitalizables.
   1. Mejoras Capitalizadas / Plazo Nueva Útil
   1. (Mejoras Capitalizadas / TC Fecha Alta) / Plazo Nueva Útil

### Registros Contables.

El sistema deberá realizar registros contables de:

1. Alta Activo Fijo.
2. Alta Avaluó.
3. Baja Activo Fijo
4. Depreciación y Amortización.

### Reporte de Activo Fijo.

El módulo deberá presentar un reporte resumido de los Activo Fijos de
la entidad para un período determinado.

## Características de los Usuarios.

Los usuarios de la aplicación son personal administrativo de la 
entidad que:

1. Los usuarios deben poder operar en una estación de trabajo.
2. Los usuarios deben poder acceder a un navegador Web.
3. Los usuarios deben poder acceder a la URL de la plataforma e 
   iniciar sesión con su usuario y contraseña.
4. Los usuarios deben tener nociones de contabilidad financiera.

Para poder operar el módulo de Activo Fijo adecuadamente la entidad
deberá contar con una Política de Activo Fijo.

## Suposiciones y Tendencias.

La entidad implementando el módulo de Activo Fijo cuenta con una instancia
de Cacao Accounting configurada para el control de sus operaciones.

No se esperan cambios bruscos en las normas contables aplicables al
control de activo fijo.

La entidad debe ser capaz de implementar los módulos base de Cacao Accounting
y en cualquier momento implementar control adiciones de activo fijo.

## Requisitos Futuros.

El módulo de Activo Fijo deberá seguir el desarrollo de la plataforma Cacao Accounting
y mantenerse compatible con lanzamientos futuros.

Una funcionalidad futura del módulo de Ativo Fijo debe ser poder integrar el acta de un
nuevo Activo Fijo con una salida de inventario, es decir debe ser posible crear un nuevo
Activo Fijo y dar de baja al Artículo del almacen, esto es útil para Activos como computadoras,
motores, herramientas, incluso vehiculos si la entidad por manejar la adquisión de vehiculos 
mediante el flujo:

```
Solicitud de Compra -> Orden de Compra -> Recibo de Bodega -> Salida de Bodega simultanea con Alta de Activo Fijo
```

## Interfaces Externas.

1. Integración con la Plataforma Cacao Accounting.
2. Exportación de Reportes a Excel y PDF.

## Requisitos de Rendimiento.

El módulo de activo fijo debe de poder ejecutarse en el mismo ambiente
en que se puede ejecutar Cacao Accounting, esto incluye:

1. Servicios de Shared Hosting que soporte Python3
2. Servidores físicos con Linux o Windows.
3. Servidores virtuales generalmente con Linux.

Dado que estos ambientes representan un universo bastante heterogéneo
se considera que el mínimo de recursos disponibles en que debe
ejecutarse el módulo de Activo Fijo junto con el stack completo de
Cacao Accounting es una Raspberrypy 3 o un Shared Host estándar.

## Restricciones de Diseño.

El módulo de activo fijo deber diseñado con un interfaz gráfica
utilizando [Patternfly](https://www.patternfly.org/v4/) versión 4
para ser compatible con la interfaz principal de Cacao Accounting.
