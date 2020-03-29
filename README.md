# TPV - ECOMMERCE 
# Version V1.0

DESCRIPCIÓN: Proyecto Terminal punto de venta e ecommerce, es un proyecto con la idea de crear una aplicacion web para la funcionalidad de ventas , compras,
cortes de caja, inventario , cancelaciones , etc , la aplicacion ecommerce con la finalidad de tener calagos en linea de los productos, hacer compras en linea, interactuar 
con el cliente etc . aplicacion movil podran tener un resumen de los diferentes TPV de las diversas sucursales como ventas diarias de x sucursal,
vetas mensuales etc , que solo ciertos usuarios podran ver. 


## Funcionalidades disponibles por versiones.

| Funciones                                     			| v1.0  |
| :---                                         				| :---: |
| Maquetado TPV de backend (Admin)             				| P    	|
| Maquetado TPV del backend (Empleado-caja)         		| P	    |
| Maquetado TPV del backend (Gerente de sucusal)         	| P	    |
| Maquetado y Estructura del Backend            			| D     |
| Conexión a fuentes de datos mediante API-REST 			| D     |





OK: Funcionalidad incorporada.
X : Funcionalidad eliminada.
D : Funcionalidad en desarrollo.
P : Previsto a desarrollar

## Integración Continua.


## Instrucciones para armar el proyecto.

## Servidor Linux/Windows.
Es necesario instalar en la computadora host los paquetes:
1. Docker         [https://www.docker.com/products/docker-desktop]
2. Git            [https://git-scm.com/downloads]

## Instrucciones levantar base de datos localhost

Ejecutar base de datos postgres. Nota: Este paso solo para pruebas en Localhost 

```
cd tpv_backend/dev/

docker-compose -f build.yml up -d postgres
```


## Instrucciones levantar proyecto con DJANGO localhost

Crear el virtualEnv 

```
cd tpv_backend/tpvCommerce/
python -m venv tpvEnv
```

Activamos el virtuaLenv

```
tpvEnv\Scripts\activate
```

intalamos las librerias del archivo requirements.txt
```
pip install -r requirements.txt
```

Inicializar proyecto con Django.  
```
cd tpv_backend/tpvCommerce/

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
