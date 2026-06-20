🧠 Why This Is Important

In an Event Bus:
Producer
   ↓
 Event
   ↓
Consumer

In Publish-Subscribe:
Producer
    ↓
 Topic
  ↙  ↓  ↘
Email SMS Analytics

Multiple consumers can receive the same event independently.

Used By
Apache Kafka
Redis Pub/Sub
RabbitMQ
Google Pub/Sub
AWS SNS

🛠 Tech Stack
Python
Flask
Dictionary
Threading

📂 Project Structure
publish-subscribe-service/
│
├── app.py
└── README.md
