# Trashcity

Trashcity es un programa de simulación de recolección de basura en una ciudad. Permite realizar turnos de recolección con camiones y empleados, y registrar el tiempo y los empleados involucrados en cada turno. También hay un centro de acopio donde se reciclan los diferentes tipos de materiales recolectados.

## Funcionamiento

El programa comienza preguntando si se desea iniciar el día. Si la respuesta es "si", se procede a crear una instancia de la clase `turno` para determinar la cantidad de camiones y empleados disponibles. A continuación, se genera una ubicación geográfica aleatoria utilizando la clase `puntogeografico` y se inicia un turno de recolección utilizando la clase `Trashcity`. Si hay suficientes camiones y empleados, se registra la ubicación y se muestra un mensaje de inicio de turno.

Luego, se registra el tiempo que duró el turno utilizando la clase `tiempo` y se muestran los empleados a cargo. Después de eso, se eliminan los empleados que participaron en el turno de la lista de empleados disponibles para el resto del día.

A continuación, se crea una instancia de la clase `CentroAcopio` para simular el reciclaje de los materiales recolectados. Se generan cantidades aleatorias de vidrio, papel, plástico, metal y materiales orgánicos, y se muestra la cantidad reciclada de vidrio hasta el momento.

Después de reciclar, se pregunta si se desea hacer otro turno. Si la respuesta es "si", se repite el proceso de generar una ubicación aleatoria, iniciar un turno, registrar el tiempo y los empleados, y reciclar los materiales recolectados.

Si en algún momento no hay suficientes camiones o empleados para hacer otro turno, se muestra un mensaje indicando que no se pueden realizar más turnos. Si se decide no hacer otro turno desde el principio, se muestra un mensaje indicando que no se recogió basura ese día.

## Modificaciones

Puedes realizar varias modificaciones en el programa para adaptarlo a tus necesidades. Algunas sugerencias son:

- Cambiar los límites aleatorios para generar ubicaciones geográficas en la clase `puntogeografico`. Por ejemplo, puedes utilizar coordenadas que representen una ciudad específica.
- Modificar los límites aleatorios para generar tiempos en la clase `tiempo`. Puedes ajustarlos para que los turnos tengan una duración más realista.
- Cambiar los identificadores de empleados en la lista `idempleados` de la clase `Trashcity`. Puedes agregar o quitar identificadores según sea necesario.
- Modificar las cantidades aleatorias de materiales reciclados en la clase `CentroAcopio`. Puedes ajustar los límites para que reflejen mejor la cantidad de materiales recolectados en cada turno.
- Agregar métodos o atributos adicionales a las clases existentes, o crear nuevas clases, según tus necesidades. Por ejemplo, podrías añadir una clase `Camion` con atributos y métodos específicos de los camiones de recolección.

