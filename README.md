<div align="center">
<table>
    <theader>
        <tr>
            <td style="width:25%;"><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>
            <td>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </td>            
        </tr>
    </theader>
    <tbody>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Proyecto web</span>: Desarrollo de una aplicación web para inscripción de laboratorios</td>
        </tr>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Fecha</span>:  2022/08/09</td>
        </tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">PROYECTO WEB</span><br />
</div>


<table>
<theader>
<tr><th>INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td>Programación Web 2</td>
    </tr>
    <tr>
        <td>SEMESTRE:</td><td>III</td>
    </tr>
    <tr>
        <td>FECHA INICIO:</td><td>30-May-2022</td><td>FECHA FIN:</td>
        <td>03-Jun-2022</td><td>DURACIÓN:</td><td>04 horas</td>
    </tr>
        <tr>
        <td colspan="3">Integrantes:
        <ul>
        <li>Vladimir Arturo Sulla Quispe - vsullaq@unsa.edu.pe</li>
        <li>Yozet Cozco Mauri - ycozcom@unsa.edu.pe</li>
        </ul>
        </td>
    </<tr>
    <tr>
        <td colspan="3">DOCENTES:
        <ul>
        <li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
        </ul>
        </td>
    </<tr>
</tdbody>
</table>

#   WebApp con Django
##  Tipo de Sistema
    Se trata de una aplicación web construida con el framework Django 4, que permita la inscripción de los alumnos en los horarios de laboratorios establecidos cada inicio de semestre.

##  Requisitos del sistema
    El sistema debe satisfacer los siguientes requisitos funcionales y no funcionales:
```

    -  RQ 01 registro de usuarios : El sistema debe tener un panel de registro  de usuarios
        - usuarios:
        - Nombres
        - Dni
        - Fecha Nacimiento
        - Membresía(type_1,type_2, …)
        - huella digital
        - foto
.

        - Membresia:
        - Nombre
        - Descripcion
        - precio_mes
        - precio_mes_3
        - precio_mes_6
        - precio_mes_12
    El sistema debe mostrar al registrar un usuario los datos básicos de registro.

    - RQ 02 administracion de usuarios : El sistema debe presentar información completa de los usuarios
        - Información personal del usuario 
        - tabla de deudas relacionadas al usuario
        - información completa de la membresía (expiración)
        - clases 
        - rutinas 

    - RQ 03 Uso de tecnologías : El sistema estará construido usando las tecnologías Django, HTML, CSS, JavaScript, SQL.

    - RQ 03 Panel de vistas para usuarios : Los usuarios podrán visualizar su información, 
Tablas usuarios, membresía, clases, rutinas 
relacionadas con sí mismos, todos estos campos siendo no editables
(posible funcionalidad) contactar con instructores, solicitar clases, rutinas, membresías.

    - RQ 04 Generar reportes : Generar reportes de todos los usuarios activos de acuerdo a petición del cliente.
        - Usuarios, nombre, dni, membresía, fecha_ini,fecha_fin, promo, deudas

    - RQ 05 Punto de venta : La página de venta deberá permitirnos seleccionar la opción de venta ( libre, usuario)
        - tipo de pago ( contado, deuda(usuario),izzipay,yape,plin ) 
        - La deuda sólo podrá buscar y seleccionar usuarios previamente registrados.

    - RQ 06 Registro de inventario tienda : El sistema deberá permitir el registro de nuevos productos de la tienda
        - id
        - código de barras
        - nombre
        - características
        - cantidad
        - precio
    - RQ 07 Control de asistencia de usuarios ( control biométrico) : El sistema nos permitirá llevar el registro de asistencia de los usuarios

    - RQ 08 Asignación de rutinas de instructores a usuarios establecidos (futura funcionalidad) : El sistema permitirá a los administradores/ instructores mandar rutinas a los usuarios directamente.

    - RQ 09 Despliegue de la aplicación y base de datos : Se desplegará inicialmente en la plataforma Heroku usando una base de datos sql

    - RQ 10 Creación de promociones suscripción por semanas o meses : El sistema debe permitir crear promociones con nuevos planes, estos planes se pueden acceder temporalmente

    - RQ 11 Panel administrador filtrado por usuarios con cumpleanos cercanos : El sistema debe tener una página donde se muestre la información de los usuarios próximos a cumplir años, mostrar información: nombre, tipo membresia, fecha_fin, fecha_ini, fecha cumpleanos, deudas.

    - RQ 12 Panel administrador filtrado por usuarios con membresías próximas a vencer : El sistema debe tener una página que muestre una lista filtrada por usuarios con sus membresías próximas a vencer, emitir alertas a los usuarios si es que les falta una semana en sus membresías. 

    - RQ 13 Reportes diarios, semanal, mensual sobre las ventas : El sistema deberá permitir emitir reportes diarios, semanales, mensuales. filtrado por ventas:( usuario, producto,fecha,tipo_pago,precio) emitir totales por ventas_contado,ventas_yape,ventas_deuda,ventas_plin, membresías.

    - RQ 14 Manejo de gastos : El sistema debe permitir el ingreso de gastos (pago  personal, pago servicios, otros)
```

##  Modelo de datos
    El modelo de datos esta conformado por las siguientes entidades.

    -   Curso : En esta entidad se almacena la información de los cursos o asignaturas que se imparten en una Escuela Profesional. Ejemplo: Programación Web 2, III semestre, 02 horas teóricas, 04 horas de laboratorio, etc..
    -   Profesor : En esta entidad se almacena los datos de los profesores que se responsabilizan del avance académico en la enseñanza de los temas planificados en cada curso. Ejemplo: Richart Escobedo, rescobedoq@unsa.edu.pe, Magister, etc.

    ...

##  Diccionario de datos

    En la construcción de software y en el diccionario de datos sobre todo se recomienda y se utilizará el idioma inglés para especificar objetos, atributos, etc.

| Course | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| code  | Numerico| No | Si | Ninguno | Código |
| name  | Cadena| No | No | Ninguno | Nombre |
...

| Teacher | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| code  | Numerico| No | Si | Ninguno | Código |
| name | Cadena| No | No | Ninguno | Nombres |
| email | Cadena| No | No | Ninguno | Correo electrónico |
| gender | Fecha| Si | No | NULL | Fecha de nacimiento |
...

| Clients | | | | | |
| -- | -- | -- | -- | -- | -- |
| Abtributo | Tipo | Nulo | Clave | Predeterminado | Descripcion |
|CliCod	Codigo de clientes	
|CliNom	Cliente nombre	
|CliEma	Cliente email	
|CliPas	cliente contrasena	
|CliNumTel	Cliente numero de telefono	
|CliTipDoc	Cliente tipo de documento	
|CliNumDoc	Cliente numero de documento	
|CliFecCum	Cliente fecha de cumpleanos	
|CliHueDig	Cliente huella digital	
|CliMemCod	Cliente Membresia codigo	
|CliMemIni	Cliente Membresia inicio	
|CliMemFin	Cliente Membresia Fin	
		

##  Diagrama Entidad-Relación
    ...

##  Administración con Django
    Se muestran los pasos realizados para crear el Proyecto, la aplicación, creacion de modelos, migraciones y habilitación del panel de administración en Django.
    ...

##  Plantillas Bootstrap
    Se seleccionó la siguiente plantilla para el usuario final (No administrador).

    Demo online:
    URL: ...

    Se muestran las actividades realizadas para adecuación de plantillas, vistas, formularios en Django.
    ...

##  CRUD - Core Business - Clientes finales
    El núcleo de negocio del sistema de inscripciones tiene valor de aceptación para los cliente finales (alumnos) radica en realizar el proceso de inscripción propiamente, que empieza desde que:
    1. El alumno inicia sesión.
    2. El alumno selecciona el o los cursos donde desea realizar una inscripción.
    3. El alumno selecciona el grupo de laboatorio donde desea incribirse.
    4. El alumno puede tener la posibilidad de anular una incripción por varias razones: cambio de grupo, corregir error, etc.
    5. El alumno puede ver el consolidado de sus inscripciones.
    6. El alumno cierra sesión.

    Todas y cada una de estas pantallas debe funcionar en la plantilla bootstrap.
    A continuación se muestran las actividades realizadas para su construcción:
    ...

##  Servicios mediante una API RESTful
    Se ha creado una aplicación que pondra a disposición cierta información para ser consumida por otros clientes HTTP.
    1. GET : Con el método get se devolverá la lista de cursos, grupos y horarios establecidos para que el alumno sobre todo vea esta información en cualquier otro medio. En formato JSON. 
    2. POST : Con este método se enviara el código del alumno y se devolvera sus inscripciones. En formato JSON.
    
    Ejemplo: Prueba en Página web, aplicación móvil, PDF, etc.
    Se especifican los pasos para crear el servicio RestFul
    ...

##  Operaciones asíncronas AJAX
    Se propone el uso de AJAX para realizar la asignación de carga académica a los docentes que estan registrados. Esta operación la realizará el usuario operador encargado por el DAISI.
    Se muestran los pasos necesarios a realizar.
    ....

##  Investigación: Email, Upload.
    - Email: Se utilizará la funcionalidad del uso de envío de correos electrónicos cuando el proceso de inscripciones culmine y al profesor le llegue la lista de alumnos inscritos en sus grupos a cargo.
    - Upload: Se utilizará esta funcionalidad para subír, archivos CSV para importar y exportar información en el sistema.
    Se muestran los pasos realizados para su funcionamiento correcto.
    ...

Github del proyecto:
```
https://github.com/ycozco/ovacenter_pe.git
```

URL en Heroku:

```

```

URL Playlist YouTube.
Producción de un PlayList en Youtube explicando cada una de los requerimientos.
Video 01 - Sistema - Requisitos.
Video 02 - Modelo de datos - DD - DER.
etc…


## REFERENCIAS
-   

#
