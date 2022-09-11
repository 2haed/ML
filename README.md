##### Вступительный экзамен ML/DL Осень



## 6 задание
### Задание по программированию
Напишите утилиту, которая на основе заданных текстов генерирует новые. 
Решать можно любым способом. Единственное ограничение ﻿﻿––﻿﻿ можно использовать только библиотеки, встроенные в стандартный Python, и библиотеки, указанные ниже. 

В зависимости от выбранного решения, задача засчитывается как вступительное на Machine Learning (ML) или Deep Learning (DL) программу. Для поступления на DL, нужно решить задачу с использованием методов машинного обучения (линейные модели, случайные леса, нейронные сети). Для поступления на ML достаточно решить задачу с использованием n-gram модели или любым другим способом. 

Возможные (но не обязательные) варианты решения предложены ниже. 



#### N-граммная модель (достаточно для поступления на ML)
В этом методе можно использовать библиотеку numpy.



Предлагается следующий простой и эффективный метод: [n-граммная языковая модель.]()




Будем называть префиксом несколько подряд идущих слов. По большому тексту для каждого префикса выбранного размера (например, 1 или 2 слова) составляется список слов, которые могут идти после него. В ML это называется обучением. Хранить эту информацию можно в виде словаря: 
```
(предыдущее слово префикса 1, ..., предыдущее слово префикса N) : 
[(следующее слово, вероятность), (другое следующее слово, вероятность), ...] 
```
Например для префикса (“мама”, “мыла”) вероятное следующее слово будет “раму”.



При самой генерации следует выбрать начальные слова предложения. Все следующие слова последовательно случайно выбираются из списка слов, идущих после префикса. Выбор из этого словаря можно делать через `np.random.choice`. В ML это называется сэмплированием.



##### Генерация с использованием классического ML (Достаточно для поступления на DL)

В этом подходе предлагается заменить или дополнить n-граммную модель методами машинного обучения. Например, можно сгенерировать n-граммной моделью несколько вариантов следующего слова и выбрать лучший с использованием дополнительной модели. Для этого можно извлечь дополнительные признаки слов: позицию в предложении, длину слова, тип окончания. Для вычисления признаков разрешается использовать внешние word2vec модели и part-of-speech (POS) тэггеры. Реализации ML моделей можно заимствовать из Sklearn (линейные модели, nearest neighbors) и XGBoost. Примеры POS и Word2vec можно заимствовать из репозитория pyfillet.



##### Генерация с использованием нейронных сетей (Достаточно для поступления на DL)
Можно генерировать текст с помощью нейронных сетей. Для этого разрешается использовать внешние word2vec модели и part-of-speech (POS) тэггеры, библиотеки PyTorch и TensorFlow. Дополнительные обертки вокруг стандартных PyTorch/TensorFlow использовать нельзя. Поддерживайте компактный размер моделей, чтобы их можно было обучать без использования GPU (за час или меньше). Примеры POS и Word2vec можно заимствовать из репозитория pyfillet.



### Интерфейс ##
Основной код должен быть разбит на две части: обучение и генерация.



**Обучение:**

- Считать входные данные из файлов.
- Очистить тексты: выкидывать неалфавитные символы, приводить к lowercase.
- Разбить тексты на слова (в ML это называется токенизацией).
- Сохранить модель в каком-нибудь формате, который позволяет восстановить её в утилите генерации.


Параметры `train.py`:

- `--input-dir` ﻿﻿-−﻿﻿ путь к директории, в которой лежит коллекция документов. Если данный аргумент не задан, считать, что тексты вводятся из stdin.
- `--model` ﻿﻿-−﻿﻿ путь к файлу, в который сохраняется модель.


**Генерация:**

- Загрузить модель.
- Инициализировать её каким-нибудь сидом.
- Сгенерировать последовательность нужной длины.
- Вывести её на экран.


Параметры `generate.py`:

- `--model` ﻿﻿-−﻿﻿ путь к файлу, из которого загружается модель.
- `--prefix` ﻿﻿-−﻿﻿ необязательный аргумент. Начало предложения (одно или несколько слов). Если не указано, выбираем начальное слово случайно из всех слов.
- `--length` ﻿﻿-−﻿﻿ длина генерируемой последовательности.


**Детали реализации**:

- Удобно реализовать консольный интерфейс через `argparse`.
- Для работы с текстами может пригодиться библиотека регулярных выражений `re`.
- Соблюдайте, пожалуйста, pep8. Пишите хороший код. Следуй те принципам ООП. Оберните модель в класс, у которого будет методы `fit` и `generate` .
- Для сохранения модели удобно использовать `pickle` или `dill` .
- Создайте только `train.py`, `generate.py`, папку `data` и, возможно, обученную модель, как `model.pkl`.
- Обучать модель можно на чем угодно: от «Войны и мира» и «Гарри Поттера» до текстов ATL и Pyrokinesis.
- Можно разрабатывать и тестировать алгоритм на малом корпусе текстов. Финальный алгоритм желательно обучить на большом корпусе для лучшего качества и большего разнообразия сгенерированных текстов.
- Нельзя использовать внешние библиотеки. Пользуйтесь тем, что есть по умолчанию в Python, и тем, что указано в секциях выше.


Создайте репозиторий на github, залейте туда код и вставьте ссылку в ответ на задачу. Пожалуйста, проверьте, что ваш репозиторий публичный. 



Задание большое и творческое. Нам интересно оценить ваши знания питона и общее умение программировать. Не дописали до конца — не страшно, отправляйте, что есть. 