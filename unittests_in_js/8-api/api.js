const express = require("express");
const app = express();

// Define a GET route
app.get("/", (req, res) => {
  res.send("Welcome to the payment system");
});

// Start the server
app.listen(7865, () => {
  console.log("API available on localhost port 7865");
});
