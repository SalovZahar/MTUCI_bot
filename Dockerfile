# Используем официальный базовый образ Python
FROM python:3.13-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости и файл requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости (библиотеки Python)
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . .

# Определяем команду для запуска бота при старте контейнера
CMD ["python", "Mtuci_lab_bot.py"]
