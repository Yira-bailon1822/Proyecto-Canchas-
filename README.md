# Proyecto-Canchas-
Este proyecto consiste en una API REST modular desarrollada para gestionar canchas deportivas y reservas de turnos.
ARQUITECTURA DEL PROYECTO 



sistema_reservas/
├── app/
│   ├── models/          # Modelos de base de datos (SQLAlchemy)
│   ├── schemas/         # Esquemas de entrada/salida (Pydantic)
│   ├── crud/            # Lógica de acceso a datos y reglas de negocio
│   ├── routers/         # Controladores de endpoints
│   ├── config.py        # Configuración de variables de entorno
│   ├── database.py      # Conexión y sesión de Base de Datos
│   ├── exceptions.py    # Manejo centralizado de excepciones
│   └── main.py          # Punto de entrada de FastAPI
├── Dockerfile           # Configuración del contenedor de la API
├── docker-compose.yml   # Orquestación de servicios (API + PostgreSQL)
├── requirements.txt     # Dependencias del proyecto
└── .env                 # Variables de entorno

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
