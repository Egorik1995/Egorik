effective-mobile-tests/          # Корневая директория проекта
│
├── pages/                       # Page Object Model (POM)
│   ├── __init__.py              # Инициализация пакета pages
│   ├── base_page.py             # Базовый класс для всех страниц
│   ├── main_page.py             # Класс для главной страницы
│
├── tests/                       # Тесты
│   ├── __init__.py              # Инициализация пакета tests
│   ├── test_main_page.py        # Тесты для главной страницы
│
├── utils/                       # Вспомогательные функции и утилиты
│   ├── __init__.py              # Инициализация пакета utils
│   ├── helpers.py               # Вспомогательные функции
│
├── allure-results/              # Результаты отчетов Allure (автоматически создается)
│
├── .dockerignore                # Игнорируемые файлы для Docker
├── .gitignore                   # Игнорируемые файлы для Git
├── Dockerfile                   # Конфигурация Docker
├── README.md                    # Документация проекта
├── requirements.txt             # Зависимости Python
├── pytest.ini                   # Конфигурация pytest и Allure
└── conftest.py                  # Фикстуры pytest (опционально)