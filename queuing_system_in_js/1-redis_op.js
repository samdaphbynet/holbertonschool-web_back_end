
import redis, { createClient } from 'redis';

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

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, value) => {
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