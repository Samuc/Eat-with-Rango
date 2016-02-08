# Descripción - Eat with Rango

La idea se centra en una aplicación web que contiene información acerca de bares que visitar, la localización de éstos, las tapas que hay disponibles.

En cada bar mostrará las visitas que ha generado, cada vez que se visite la sección de ese bar en la aplicación, subirán sus visitas.

Cada bar, tendrá su lista de tapas, a las que se podrá votar (con un like), para ver cuáles gusta más a los usuarios.

La aplicación contiene un formulario de Login y de Registro.

El registro de usuarios permite añadir una imagen de avatar para el perfil del usuario.

Los usuarios logeados, podrán hacer "logout", añadir Bares, y añadir tapas a esos bares.

Cada bar, se podrá crear añadiendo su nombre y una dirección.
Gracias a ésta dirección, si está bien escrita, una vez se visualice el bar y la lista de tapas, debajo mostrará un mapa (con easy_maps) localizando el bar en su dirección correcta.

Al añadir tapa, se insertará el nombre de la tapa y el bar al que pertenece.

Una vez insertada, a ésta tapa podremos darle a "like" y su contador irá subiendo al refrescar la página. Igual que las visitas de cada bar.

Toda ésta información se guardará permanentemente en la base de datos.

Contiene diferentes botones botones para cambiar el tamaño de la letra.

También, contiene una sección Hightchart, donde se monitoriza las visitas de los bares, mostrando una gráfica con relación nombre del bar y número de visitas.
