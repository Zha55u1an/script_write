import psutil
import csv
import os
import time

# Функция для получения использования ЦП и памяти
def get_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    return cpu_percent, memory_percent

# Функция для записи данных в файл CSV
def write_to_csv(cpu_percent, memory_percent):
    file_path = os.path.join(os.path.dirname(__file__), 'system_monitoring.csv')
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), cpu_percent, memory_percent])

# Основная функция
def main():
    print("Monitoring system resources... Press Ctrl+C to stop.")
    try:
        while True:
            cpu_percent, memory_percent = get_usage()
            write_to_csv(cpu_percent, memory_percent)
            time.sleep(60)  # Записывать данные каждые 60 секунд
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    main()
