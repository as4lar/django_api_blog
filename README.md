# Blog API - Django Rest Framework

Este es un proyecto de API para gestionar entradas de blog y comentarios, desarrollado con Django y Django Rest Framework.

## Requisitos

- asgiref==3.8.1
- certifi==2024.8.30
- charset-normalizer==3.3.2
- coreapi==2.3.3
- coreschema==0.0.4
- Django==5.1.1
- djangorestframework==3.15.2
- idna==3.8
- itypes==1.2.0
- Jinja2==3.1.4
- MarkupSafe==2.1.5
- requests==2.32.3
- setuptools==74.1.2
- sqlparse==0.5.1
- tzdata==2024.1
- uritemplate==4.1.1
- urllib3==2.2.2

### En donde encontrar la API

La API esta disponible en http://localhost:8000/

#### Endpoints de la API
La documentación sobre el uso de la API se puede encontrar en http://localhost:8000/
#####POSTS
- Listar todos los posts: GET /api/posts/
- Crear un nuevo post: POST /api/posts/
- Obtener un post por ID: GET /api/posts/{id}/
- Actualizar un post: PUT /api/posts/{id}/
- Eliminar un post: DELETE /api/posts/{id}/

######COMMENTS
- Listar todos los comentarios: GET /api/comments/
- Crear un nuevo comentario: POST /api/comments/
- Obtener un comentario por ID: GET /api/comments/{id}/
- Actualizar un comentario: PUT /api/comments/{id}/
- Eliminar un comentario: DELETE /api/comments/{id}/
- Obtener comentarios de un post específico: GET /api/posts/{post_id}/comments/
