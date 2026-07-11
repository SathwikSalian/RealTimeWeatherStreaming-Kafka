<!-- # Weather Kafka Project

## Prerequisites

- Java JDK
- Python 3.x
- Apache Kafka 3.7.2
- Internet connection
- OpenWeatherMap API Key

---

## 1. Install Required Python Packages

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install kafka-python requests
```

---

## 2. Navigate to Kafka Folder

```bash
cd D:\kafka_2.12-3.7.2\kafka_2.12-3.7.2
```

---

## 3. Start ZooKeeper

Open a Command Prompt:

```bash
D:\kafka_2.12-3.7.2\bin\windows>zookeeper-server-start.bat ..\..\config\zookeeper.properties
```

---

## 4. Start Kafka Broker

Open another Command Prompt:

```bash
D:\kafka_2.12-3.7.2\bin\windows>kafka-server-start.bat ..\..\config\server.properties
```

---

## 5. Create Kafka Topic

Open another Command Prompt:

```bash
bin\windows\kafka-topics.bat --create --topic weather-data --bootstrap-server localhost:9092
```

Expected Output:

```
Created topic weather-data.
```

---

## 6. Verify Topic Creation

```bash
bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
```

Expected Output:

```
weather-data
```

---

## 7. Go to Project Folder

Open a new Command Prompt:

```bash
cd path\to\WeatherKafkaProject
```

Example:

```bash
cd D:\Projects\WeatherKafkaProject
```

---

## 8. Run the Consumer

```bash
python consumer.py
```

Expected Output:

```
Waiting for messages...
```

---

## 9. Run the Producer

Open another Command Prompt:

```bash
python producer.py
```

Expected Output:

```
Producer Started...

Sent :
{
   "city":"Bangalore",
   "temperature":29.6,
   "time":"2026-07-08 20:30:12"
}
```

---

## 10. Consumer Output

```
Waiting for messages...

----------------------------
City        : Bangalore
Temperature : 29.6 °C
Time        : 2026-07-08 20:30:12
----------------------------
```

---

## 11. Stop Kafka Services

Press:

```
Ctrl + C
```

in the following terminals:

- Producer
- Consumer
- Kafka Broker
- ZooKeeper

---

## Kafka Topic Commands

### List Topics

```bash
bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
```

### Describe Topic

```bash
bin\windows\kafka-topics.bat --describe --topic weather-data --bootstrap-server localhost:9092
```

### Delete Topic

```bash
bin\windows\kafka-topics.bat --delete --topic weather-data --bootstrap-server localhost:9092
```

---

## Project Structure

```
WeatherKafkaProject
│
├── producer.py
├── consumer.py
├── weather_api.py
├── config.py
├── requirements.txt
└── README.md
``` -->