const kue = require("kue");

const queue = kue.createQueue();

const jobDate = {
    phoneNumber: 1234567890,
    message: "Hello, world"
}

const job = queue.create("push_notification_code", jobDate)
    .save((error) => {
        if (error) {
            console.log("Notification job failed", error)
        } else {
            console.log("Notification job created", job.id)
        }
    })

    job.on("complete", () => {
        console.log("Notification job completed")
    })
    
    job.on("failed", (error) => {
        console.log("Notification job failed", error)
    })
    
