import { createClient } from 'redis';

// Connect to localhost on port 6379.

const client = createClient();

// console the message when the connection to Redis works correctly
client.on("connect", () => {
    console.log("Redis client connected to the server")
})

// console the message when the connection to Redis does not work
client.on("error", (err) => {
    console.log("Redis client not connected to the server: ", err)
})
