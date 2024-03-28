import redis, {createClient} from'redis';

const client = createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server")
})

client.on("error", (err) => {
    if (err) {
        console.error(err)
        return
    }
    console.log("Redis client not connected to the server: ", err)
})

// Create hash

client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Get hash

client.hgetall("HolbertonSchools", (err, res) => {
    if (err) {
        console.error(err)
        return
    }
    console.log(res)
})
