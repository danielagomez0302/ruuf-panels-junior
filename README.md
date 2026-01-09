# Tarea Dev Junior - Ruuf

## 🛠️ Problema

El problema consiste en calcular la máxima cantidad de paneles solares de dimensiones "a" y "b" que pueden instalarse dentro de un techo de dimensiones "x" e "y".

Los paneles pueden rotarse, por lo que se deben considerar ambas orientaciones.

---

## 📝 Solución

La solución evalúa las dos posibles orientaciones de paneles dentro del techo. Para cada orientación se calcula cuántos paneles caben utilizando división entera.
Para que finalmente se retorne el mayor valor entre ambas configuraciones.

Sin embargo, mencionar que aún con los calculos de manera logica matematica resta un espacio de 1x3 donde sigue entrando un panel solar más, pero esto no se calcula con este tipo de codigo, sino con un algoritmo packing 2D.

---

## 🤔 Supuestos y Decisiones

- Los paneles no pueden superponerse.
- Se permite rotar los paneles.
- No existen configuraciones adicionales que permitan instalar más paneles que las evaluadas.

---

## 🎥 Video explicativo

[PEGAR AQUÍ EL LINK DEL VIDEO]
