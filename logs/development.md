# CIC — Development Log

## Estado actual

**Proyecto:** Centro de Inteligencia Comercial (CIC)  
**Versión:** 2.0 en desarrollo  
**Fecha de actualización:** 2026-08-31

## Objetivo

Construir una API REST con Django REST Framework como evolución del proyecto existente de análisis de ventas y movilidad de vendedores.

La API se conectará a la base de datos SQL Server existente **ForceSyncDB_Worker**. En la primera etapa no se modificará la información de las tablas de Force Manager; la API comenzará como una API de consulta.

### Tablas iniciales

- `Accounts`
- `Activities`
- `Calendars`
- `dev_Detalle_Corregida`
- `Opportunities`
- `Users`

### Tablas para etapas posteriores

- `MovilidadRegistro`
- `NotificacionesVendedores`
- `PresupuestoSegmentos`
- `ResumenMovilidad`
- `StrikesVendedores`
- `UsuariosCIC`

## Arquitectura inicial

```text
ForceSyncDB_Worker (SQL Server)
        |
        | Django ORM
        v
Django + Django REST Framework
        |
        | JWT + permisos
        v
Flutter / cliente consumidor
```

La aplicación `forcesync` se encargará inicialmente de los modelos que representan los datos existentes provenientes de Force Manager.

## Estructura inicial

```text
cic_api/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── forcesync/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
└── logs/
    ├── dev_log.csv
    ├── development.md
    └── roadmap.md
```

## Trabajo realizado

### 1. Creación del proyecto

Se creó un proyecto Django nuevo para CIC y una aplicación llamada `forcesync`.

### 2. Dependencias

Se definieron las dependencias necesarias para trabajar con:

- Django
- Django REST Framework
- Simple JWT
- python-dotenv
- mssql-django
- pyodbc

### 3. Conexión a SQL Server

Se configuró Django para utilizar la base existente:

```text
ForceSyncDB_Worker
```

La configuración utiliza variables de entorno para evitar almacenar credenciales directamente en el código.

El driver ODBC disponible y seleccionado es:

```text
ODBC Driver 17 for SQL Server
```

### 4. Prueba de conexión

Se ejecutó:

```powershell
python manage.py dbshell
```

La conexión fue exitosa.

Se verificó:

```sql
SELECT DB_NAME() AS BaseDeDatos;
GO
```

Resultado:

```text
ForceSyncDB_Worker
```

### 5. Prueba de datos

Se consultó la tabla `Users`:

```sql
SELECT TOP 5
    Id,
    Name,
    LastName,
    Email,
    IsActive
FROM Users;
GO
```

Se obtuvieron registros reales, confirmando que Django puede consultar la base existente.

### 6. Inspección de modelos

Se utilizó:

```powershell
python manage.py inspectdb Users Accounts Activities Calendars Opportunities > models_generados.py
```

Esto permitió generar una primera representación Django de las tablas existentes.

`dev_Detalle_Corregida` quedó fuera de esta primera inspección porque en el esquema compartido no se identificó una clave primaria declarada.

### 7. Revisión de `Users`

El modelo generado para `Users` contiene:

```python
id = models.IntegerField(db_column='Id', primary_key=True)
```

y:

```python
class Meta:
    managed = False
    db_table = 'Users'
```

Se determinó que `managed = False` es apropiado porque las tablas pertenecen a una base existente que es alimentada por otros procesos.

También se decidió mantener inicialmente el modelo completo y controlar los campos expuestos por la API mediante serializers.

## Relaciones identificadas

```text
Calendars.SalesRepId_Id
        -> Users.Id

Opportunities.SalesRepId_Id
        -> Users.Id

Activities.SalesRepId_Id
        -> Users.Id

Accounts.SalesRepId1_Id
        -> Users.Id

Accounts.SalesRepId2_Id
        -> Users.Id

Accounts.SalesRepId3_Id
        -> Users.Id

Accounts.SalesRepId4_Id
        -> Users.Id

Accounts.SalesRepId5_Id
        -> Users.Id

dev_Detalle_Corregida.Id_Vendedor_FM
        -> Users.Id
```

Estas relaciones serán revisadas antes de convertir los campos enteros generados por `inspectdb` en `ForeignKey`.

## Decisiones técnicas actuales

1. Las tablas existentes de ForceSyncDB_Worker no serán creadas ni administradas por Django.
2. Se utilizará `managed = False` para estos modelos.
3. La primera versión de los endpoints será únicamente de lectura.
4. Se utilizarán `ReadOnlyModelViewSet` y Routers para los endpoints iniciales.
5. Se utilizarán serializers para controlar qué campos se exponen.
6. Las relaciones con `Users` se modelarán con `ForeignKey` cuando se hayan verificado.
7. JWT y permisos se incorporarán después de tener funcionando la API de lectura.
8. No se debe inventar una primary key para `dev_Detalle_Corregida`; primero se debe determinar cómo identificar un registro de forma segura.

## Pendiente inmediato

Revisar los modelos generados de:

- `Activities`
- `Calendars`
- `Opportunities`
- `Accounts`

y convertir las relaciones confirmadas con `Users` en relaciones ORM apropiadas.

Después:

```text
Models
  ↓
Serializers
  ↓
ReadOnlyModelViewSet
  ↓
Routers
  ↓
GET
  ↓
Postman
```
