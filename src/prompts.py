from langchain.prompts import PromptTemplate

PROMPT_TEMPLATE = """
Eres el maestro de un juego de roles, un nuevo personaje debe ser agregado, 
utilizando toda tu imaginacion debes crear un nuevo personaje tomando en cuenta algunos de los siguientes detalles, 
se te dara el mundo origen de este personaje, toma en cuenta que cada uno de los mundos de este universo son desconocidos y 
extravagantes por lo que el nombre de cada uno es bastante descriptivo respecto a las caracteristicas del mismo, y la otra informacion 
que tienes es un medidor de sentimientos del personaje que describe su personalidad. Esto quiere decir que para las 
emociones de felicidad, tristeza, sorpresa y enojo se te dara un valor de 1 a 5 con un 1 significando que el personaje no 
muestra muchos rasgos de esa emocion en su personalidad y 5 significa que esa emocion es dominante en la personalidad del 
personaje. A partir de estos datos necesito que generes el origen de personaje, principalmente que me devuelvas una breve 
historia de personaje en cuanto a su pasado, y en base a eso necesito que tambien me devuelvas cuales son los objetivos de este personaje.
El mundo de origen del personaje es {origen}, su nivel de felicidad es {felicidad}, su nivel de tristeza es {tristeza}, 
su nivel de sorpresa es {sorpresa} y finalmente su nivel de enojo es {enojo}.
"""