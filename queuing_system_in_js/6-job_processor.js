import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Function to send notification
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Queue process to listen to new jobs on push_notification_code
queue.process('push_notification_code', (job, done) => {
    // Extract phone number and message from job data
    const { phoneNumber, message } = job.data;

    // Call the sendNotification function with phone number and message
    sendNotification(phoneNumber, message);

    // Call done when job processing is complete
    done();
});