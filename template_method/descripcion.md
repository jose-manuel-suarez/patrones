## Método plantilla (Template Method)

### Descripción
	Patron de comportamiento
	Este patrón permite definir una secuenciación determinada de pasos en una clase abstracta, y que sean las subclases concretas las que definan cada uno de los pasos concretos de esta secuenciación general de pasos funcionales.

### Funcionalidad

### Propósito
	Proporcionar un método que permita a las diferentes subclases redefinir partes de la lógica general, mediante redefinición de ciertos métodos gancho (hooks).
	Evitar la duplicidad y repetición de código (métodos complejos) en las subclases.

### Estructura
![Patrón Método Plantilla](estructura.drawio.svg)

### Aplicailidad
	> Proporcionar un esqueleto (plantilla) para un método.
	> Centralizar las partes de un método que se definirán en todas las subclases, pero pueden diferir levemente en su implementación.
	> Controlar las operaciones redefinibles por las subclases.
	> Muchos métodos de clases relacionadas, poseen una estructura similar. Pudiendo centralizarse y reutilizarse en la superclase.

### Ventajas
	> Facilita la reutilización del código.
	> Permite diferenciar la secuenciación lógica de pasos, de la implementación concreta.
	> Permite extensibilidad por herencia (de caja blanca), muy utilizada en frameworks.

### Desventajas
	> Puede ser tedioso a la hora de utilizarlo si la clase abstracta contiene muchos métodos abstractos.
	> Se recomienda que sea liviano, es decir, la clase abstracta invoque a pocos métodos abstractos.
	> Otra posibilidad es utilizar métodos por defecto en la clase abstracta, se le denominan ***métodos de anclaje***.

### Aspectos a considerar
	> Considerar qué métodos ameritan ser abstractos o mantener una implementación por defecto en la clase abstracta.