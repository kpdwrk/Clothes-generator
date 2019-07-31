
# Генератор одежды из случайных элементов
Задача:  
    У дизайнеров одежды закончились идеи по конструированию новых изделий.  
Решение:  
    Дизайнер подготавливает изображения .png с прозрачным фоном, одинаковой высотой и шириной.
    В папке "img_input" создаёт подпапки-категории, например: рукава, замки, воротники и т.д.,
    далее наполняет эти папки изображениями.           
                                           
  **Пример:  структура подпапок папки img_imput**
  
 | 0-background | 1-pocket | 2-collar | 3-sleeves | 4-torso | 5-clasp |
 | ------------ | -------- | -------- | --------- | ------- | ------- |
 | 0.png        | 11.png   | 21.png   | 31.png    | 41.png  | 51.png  |
 | ...          | 12.png   | 22.png   | 32.png    | 42.png  | 52.png  | 
 | ...          | 13.png   | 23.png   | 33.png    | 43.png  | 53.png  |
 | ...          | ...      | ...      | ...       | ...     | ...     |

Скрипт считывает массив подпапок-категорий из "img_input".  
Далее из каждой подпапки берет одно случайное изображение и накладывает послойно одно изображение на другое.  
Например туловище + карман + воротник + рукава + торс + замок (0.png + 12.png + 23.png + 31.png + 43.png + 51.png ).  
На выходе мы получаем изображение в папке "img_output".  

## Параметры запуска скрипта:

-c --count 5 (количество случайных изображений которое будет сгенерировано)  
-i --input img_imput (папка содержащая подпапки с изображениями .png)  
-o --output img_imput (папка в которую сохранятся сгенерированные изображения)  

![enter image description here](img_output/2019-07-31%2016:19:53.616279/0.png)



