import redis, { createClient } from 'redis';

const client = createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server")
});

client.on("error", (err) => {
    if (err) {
        console.error(err)
        return
    }
    console.log("Redis client not connected to the server: ", err)
})

const CHANNEL = "holberton school channel";

client.subscribe(CHANNEL);

client.on('message', (channel, message) => {
    if (channel === CHANNEL) {
        console.log(message);
    }

    if (message === "KILL_SERVER") {
        client.unsubscribe(CHANNEL);
        client.quit();
    }
})