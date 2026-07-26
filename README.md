# Proyecto-Canchas-
Este proyecto consiste en una API REST modular desarrollada para gestionar canchas deportivas y reservas de turnos.
ARQUITECTURA DEL PROYECTO 



reserva_canchas/
├── app/
│   ├── crud/               
│   │   ├── cancha.py
│   │   └── __init__.py
│   ├── models/            
│   │   ├── cancha.py
│   │   ├── reserva.py
│   │   └── __init__.py
│   ├── routers/            
│   │   ├── cancha.py
│   │   └── __init__.py
│   ├── schemas/            
│   │   ├── cancha.py
│   │   ├── reserva.py
│   │   └── __init__.py
│   ├── config.py           
│   ├── database.py         
│   ├── main.py             
│   └── __init__.py
├── .env                    # Variables de entorno locales
├── Dockerfile              # Instrucciones para la construcción de la imagen de la API
├── docker-compose.yml      # Orquestación de contenedores (API + PostgreSQL)
└── requirements.txt        # Dependencias del proyecto Python

//Mnaual de uso 
Requisistos de instalación 
1-	Docker Desktop (debe estar en ejecución).
2-	 Git (opcional, para clonar el repositorio).
3-	 Visual Studio Code (o tu editor de código preferido)
Configuracion e instalación paso a paso 
1-	Clonar o descargar el proyecto
Ubicarse en la carpeta raíz del proyecto (reserva_canchas).
2-	Verificar las variables de Entorno 
3-Ejecucion en Docker 
Para desplegar y levantar todo el ecosistema (Servidor web FastAPI + Base de datos PostgreSQL), ejecuta el siguiente comando en la terminal desde la raíz del proyecto:
Docker compose up –build
