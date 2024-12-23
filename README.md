# chatGPTmySQL
Uno de los problemas de chatGPT en particular y los LLM en general es que su conocimiento suele estar limitado a los datos de entrenamiento. Si bien es posible agregar datos manualmente en el prompt — opción no escalable y con altos costos de tokens — o por medio de ciertos mecanismos como los vector files — opción con datos estáticos — , conectar chatGPT a una base de datos abre un universo de posibilidades.

Para este ejemplo voy a conectar una base de datos mysql con productos para el cuidado de la piel a chatGPT y así poder interactuar en lenguaje natural.

# Pasos
1. Obtener un API key de openAI
2. Crear un asistente
3. Configurar la definición del function calling
4. Crear la estructura de la base mySQL y cargar registros
5. Editar los settings del script Python

# Function Calling

{
  "name": "get_cream",
  "description": "Get cream description and price from a mysql database",
  "strict": true,
  "parameters": {
    "type": "object",
    "properties": {
      "purpose": {
        "type": "string",
        "description": "The cream purpose. Ex: beauty"
      }
    },
    "additionalProperties": false,
    "required": [
      "purpose"
    ]
  }
}

# Contacto
Por proyectos de IA generativa o Machine Learning
https://www.linkedin.com/in/ronibandini/
https://www.instagram.com/ronibandini/
