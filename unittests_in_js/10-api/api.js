const express = require("express");
const app = express();

// Define a GET route
app.get("/", (req, res) => {
  res.send("Welcome to the payment system");
});

// Define a GET route
app.get("/cart/:id(\\d+)", (req, res) => {
  res.send("Payment methods for cart " + req.params.id);
});

// Define a GET route
app.get("/available_payments", (req, res) => {
  res.send({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

// To parse the body of the request
app.use(express.json());
// Define a POST route
app.post("/login", (req, res) => {
  res.send("Welcome " + req.body.userName);
});

// Start the server
app.listen(7865, () => {
  console.log("API available on localhost port 7865");
});
