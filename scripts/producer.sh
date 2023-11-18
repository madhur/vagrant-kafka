#!/bin/bash

if [ $# -gt 0 ]; then
    $KAFKA_HOME/bin/kafka-console-producer.sh --topic "$1" --broker-list vkc-zk1:9092,vkc-zk2:9092,vkc-zk3:9092
else
    echo "Usage: "$(basename $0)" <topic_name>"
fi
