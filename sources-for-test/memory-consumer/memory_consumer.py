import os
import time

def consume_memory_slowly(mb, chunk_mb=10, delay=1):
    """
    Медленно занимает память блоками.
    :param mb: всего мегабайт занять
    :param chunk_mb: сколько мегабайт выделять за раз
    :param delay: пауза между выделениями в секундах
    """
    print(f"Буду занимать {mb} MB памяти по {chunk_mb} MB каждые {delay} секунд...")
    
    chunks = []
    total_allocated = 0
    chunk_size = chunk_mb * 1024 * 1024  # в байты
    target_size = mb * 1024 * 1024

    try:
        while total_allocated < target_size:
            # Выделяем чанк
            chunks.append(bytearray(chunk_size))
            total_allocated += chunk_size
            print(f"Выделено: {total_allocated / (1024*1024):.2f} MB")
            time.sleep(delay)
        
        print("Вся память занята. Работаю... Нажмите Ctrl+C для выхода.")
        # Держим память занятой
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Освобождаю память...")
    except MemoryError:
        print("Не хватило памяти для выделения очередного блока.")

if __name__ == "__main__":
    # Читаем из переменных окружения
    mb_str = os.environ.get("MEMORY_MB", "100")
    delay_str = os.environ.get("DELAY_SEC", "1")
    
    try:
        mb = int(mb_str)
        delay = float(delay_str)
    except ValueError:
        print("Неверные значения MEMORY_MB или DELAY_SEC.")
        exit(1)
    
    consume_memory_slowly(mb, chunk_mb=20, delay=delay)
