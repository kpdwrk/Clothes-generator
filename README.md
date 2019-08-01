
# Генератор эскизов одежды
### Задача:  
У дизайнеров закончились идеи по конструированию новых изделий одежды. Разработать скрипт для генерации одежды из случайных элементов.  
### Решение:  
#### Подготовка к работе  
Дизайнер подготавливает изображения .png с прозрачным фоном, одинаковой высотой и шириной.
В папке img_input создаёт подпапки-категории, например: рукава, застежки, воротники и т.д.
Далее наполняет эти папки изображениями.           
                                           
  **Пример:  структуры подпапок папки img_imput**
  
 | 0-background | 1-pocket | 2-collar | 3-sleeves | 4-torso | 5-clasp |
 | ------------ | -------- | -------- | --------- | ------- | ------- |
 | 0.png        | 11.png   | 21.png   | 31.png    | 41.png  | 51.png  |
 | ...          | 12.png   | 22.png   | 32.png    | 42.png  | 52.png  | 
 | ...          | 13.png   | 23.png   | 33.png    | 43.png  | 53.png  |
 | ...          | ...      | ...      | ...       | ...     | ...     |
#### Алгоритм работы скрипта
Скрипт считывает массив подпапок-категорий из папки img_input.  
Далее из каждой подпапки берет одно случайное изображение.
Оторбранные изображения складываются послойно в единое изображение. 
Например: туловище + карман + воротник + рукава + торс + застежка (0.png + 12.png + 23.png + 31.png + 43.png + 51.png ).  
На выходе мы получаем сгенерированное изображение в папке "img_output".  

## Параметры запуска скрипта:

-c --count 5 (количество случайных изображений которое будет сгенерировано)  
-i --input img_imput (папка содержащая подпапки с изображениями .png)  
-o --output img_imput (папка в которую сохранятся сгенерированные изображения)  

![enter image description here](img_output/2019-07-31%2016:19:53.616279/0.png)



