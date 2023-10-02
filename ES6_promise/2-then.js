/* eslint disable */

export default function handleResponseFromAPI(promise) {
    promise
        .then((response) => {
            console.log("Got a response from the API");
            return { status: 200, body: 'Success' };
        })
        .catch(() => {
            console.log("Got a response from the API");
            return new Error();
        })
}