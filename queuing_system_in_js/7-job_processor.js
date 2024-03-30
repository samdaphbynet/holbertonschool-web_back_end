import kue from 'kue';

const blackList = ["4153518780", "4153518781"]

// Create a queue with Kue
const queue = kue.createQueue();

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);

    if (blackList.includes(phoneNumber)) {
        const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
        return done(error);
    }

    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    done();
}

// Queue process to listen to new jobs on push_notification_code
queue.process('push_notification_code_2', 2, (job, done) => {
    // Extract phone number and message from job data
    const { phoneNumber, message } = job.data;

    // Call the sendNotification function with phone number and message
    sendNotification(phoneNumber, message, job, done);

    // Call done when job processing is complete
});