
import redis, { createClient } from 'redis';
import { promisify } from "util";

// Connect to localhost on port 6379.

const client = createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// console the message when the connection to Redis works correctly
client.on("connect", () => {
    console.log("Redis client connected to the server")
})

// console the message when the connection to Redis does not work
client.on("error", (err) => {
    console.log("Redis client not connected to the server: ", err)
})

async function setNewSchool(schoolName, value) {
    await client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    await client.get(schoolName, (err, value) => {
        if (err) {
            console.error("Error", err);
            return
        }
        console.log(`${value}`)
    })
}

// Call the functions to test them out
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');