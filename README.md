# Proyecto Final de Santiago Navalon y Rodrigo Gimenez
## Resumen: El sistema cuenta con un modulo para crear objetos, crear usuarios y postear en un blog independiete.
- 
- El modulo "Maestro":
    +Funcionalidad de Crear "Productos"
    +Funcionaldiad de Buscar "Productos"
    +Funcionalidad de Editar "Productos"
    +Funcionalidad de Eliminar "Productos"
    
    - En dicho modulo se utilizan vistas y clases basadas en vistas.

- El modulo "Distribucion":
    +Funcionalidad de Crear "Transportes"
    +Funcionaldiad de Buscar "Transportes"
    +Funcionalidad de Editar "Transportes"
    +Funcionalidad de Eliminar "Transportes"
    
    - En dicho modulo se utilizan vistas y clases basadas en vistas.

- El modulo "Accounts" posee la funcionalidad de:
    +Funcionalidad de Crear usuario
        *Ingresando valor en Usuario
        *Ingresando valores en Contraseña
    +Funcionalidad de Editar informacion del usuario antes creado y logeado:
        *Ingresando Nombre
        *Ingresando Apellido
        *Ingresando Mail
        *Ingresando Password
        *Ingresando Descripcion
        *Ingresando Avatar

    +Utilizando decoradores:
        +Tiene el usuario acceso a los modulos "Maestro" y "Distribucion" para la de creacion, edicion y eliminacion de elementos. 
        +Acceder al modulo de creacion de "Posteo"
        +Posee la funcionalidad de Editar el Password
    +Los usuarios poseen la posibilidad de obtener los datos de los elementos creados en la base.

    -En dicho modulo se utilizan decoradores, vistas y clases basadas en vistas.

- El modulo "Blog":
    +Funcionalidad de Crear "Blog"
        *Los blogs poseen las siguientes caracteristicas:
            **Los posteos existentes estan ordenados de los mas recientes a los mas antiguos
            **Estan paginados de a 3
            **Poseen vinculos que te lleva a visualizar mayor informacion del autor del posteo.
            **Al momento de la creacion del posteo se incluye la funcionalidad de ingreso de imagen
            **Cada uno de los posteos se identifican por autor

    - En dicho modulo se utilizan decoradores, vistas y clases basadas en vistas

-Las bases creadas a traves de los modelos para que la funcionalidad del proyecto sea optima son:
    +Usuario {auth_user}
    +Distribucion {distribucio_transporte}
    +Autor del Posteo {muro_posteo}
    +Posteor {muro_posteousuarios}
    +Productos {vistas_producto}

-Se crean los siguiente templates para la adecuada visualizacion:

    +About:
        *sobre_rodri.html
        *sobre_santi.html

    +Accounts:
        *cambiar_password.html
        *editar_perfil.html
        *login.html

    +Distribucion:
        *busqueda_transporte.html
        *crear_transporte.html
        *distribucion.html
        *editar_transporte.html
        *edite_transporte.html
        *eliminar_transporte.html
        *elimine_transporte.html

    +Maestros:
        *busqueda_propucto.html
        *crear_stock.html
        *editar_producto.html
        *edite_producto.html
        *eliminar_producto.html
        *maestro.html

    +Muro:
        *autor.html
        *base.html
        *crear_post.html

Template Index --> index.html

-Se utilizaron statics para una mejor visualizacion de los templates.