const express = require('express');
const app = express();
const mysql = require('mysql');
const bodyParser = require('body-parser');
const flash = require('connect-flash');
const session = require('express-session');

app.set('view engine', 'ejs');
app.use(flash());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({
    secret: 'my-secret-key',
    resave: false,
    saveUninitialized: true
  }));


const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'Samyuktha@30',
  database: 'ecommerce'
});



app.get('/products/:id', (req, res) => {
  const productId = req.params.id;
  const query = `SELECT * FROM products WHERE product_id = ${productId}`;
  db.query(query, (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error retrieving product from database');
    } else if (result.length === 0) {
      res.status(404).send('Product not found');
    } else {
      res.json(result[0]);
    }
  });
});

app.get('/products', (req, res) => {
  const productId = req.params.id;
  const query = `SELECT * FROM products;`;
  db.query(query, (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error retrieving product from database');
    } else if (result.length === 0) {
      res.status(404).send('Product not found');
    } else {
      res.json(result);
    }
  });
});

app.get('/customers', (req, res) => {
  const productId = req.params.id;
  const query = `SELECT * FROM customers;`;
  db.query(query, (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error retrieving customer from database');
    } else if (result.length === 0) {
      res.status(404).send('customer not found');
    } else {
      res.json(result);
    }
  });
});

app.get('/customers/:id', (req, res) => {
    const customer_id = req.params.id;
    const query = `SELECT * FROM customers WHERE customer_id = ${customer_id}`;
    db.query(query, (err, result) => {
      if (err) {
        console.error(err);
        res.status(500).send('Error retrieving Customer from database');
      } else if (result.length === 0) {
        res.status(404).send('Customer not found');
      } else {
        res.json(result[0]);
      }
    });
  });

app.post('/customers', (req, res) => {
  const firstName = req.body.firstName;
  const lastName = req.body.lastName;
  const email = req.body.email;
  const address = req.body.address;
  const phone = req.body.phone;

 
  const insertQuery = `INSERT INTO customers (first_name, last_name, email, address, phone) VALUES ('${firstName}', '${lastName}', '${email}', '${address}', '${phone}')`;
  db.query(insertQuery, (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error inserting new customer');
    } else {
      res.send(`New customer with ID ${result.insertId} inserted successfully`);
    }
  });
});


app.put('/customers/:id', (req, res) => {
  const customerId = req.params.id;
  const firstName = req.body.firstName;
  const lastName = req.body.lastName;
  const email = req.body.email;
  const address = req.body.address;
  const phone = req.body.phone;
  
  const updateQuery = `UPDATE customers SET first_name = '${firstName}', last_name = '${lastName}', email = '${email}', address = '${address}', phone = '${phone}' WHERE customer_id = ${customerId}`;
  db.query(updateQuery, (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error updating customer information');
    } else if (result.affectedRows === 0) {
      res.status(404).send('Customer not found');
    } else {
      res.send(`Customer with ID ${customerId} updated successfully`);
    }
  });
});


app.delete('/customers/:id', (req, res) => {
  const customerId = req.params.id;


  const deleteQuery = `DELETE FROM customers WHERE customer_id = ${customerId}`;
  db.query(deleteQuery, (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error deleting customer');
    } else if (result.affectedRows === 0) {
      res.status(404).send('Customer not found');
    } else {
      res.send(`Customer with ID ${customerId} deleted successfully`);
    }
  });
});


app.delete('/products/:id', (req, res) => {
  const productId = req.params.id;

 
  const deleteQuery = `DELETE FROM products WHERE product_id = ${productId}`;
  db.query(deleteQuery, (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error deleting product');
    } else if (result.affectedRows === 0) {
      res.status(404).send('Product not found');
    } else {
      res.send(`Product with ID ${productId} deleted successfully`);
    }
  });
});

// POST request to add a product to an order
app.post('/orders/:cart_id/items', (req, res) => {
    const cart_id = req.params.cart_id;
    const productId = req.body.productId;
    const quantity = req.body.quantity;
  
    const stockQuery = `SELECT stock_count FROM products WHERE product_id = ${productId}`;
    db.query(stockQuery, (err, result) => {
      if (err) {
        console.error(err);
        res.status(500).send('Error checking product stock');
      } else if (result.length === 0) {
        res.status(404).send('Product not found');
      } else if (result[0].stock_count < quantity) {
        res.status(400).send('Not enough stock available');
      } else {
    
        const orderItemQuery = `INSERT INTO order_items (cart_id, product_id, quantity) VALUES (${cart_id}, ${productId}, ${quantity})`;
        db.query(orderItemQuery, (err, result) => {
          if (err) {
            console.error(err);
            res.status(500).send('Error adding product to order');
          } else {
            res.send('Product added to order');
          }
        });
      }
    });
  });
  
 
app.get('/cart/order_items', (req, res) => {
    const query = `SELECT c.cart_id,c.total_amount, c.customer_id, oi.order_item_id, oi.product_id, oi.quantity, oi.item_price
                   FROM cart c
                   JOIN order_items oi ON c.cart_id = oi.cart_id`;
    db.query(query, (err, result) => {
      if (err) {
        console.error(err);
        res.status(500).send('Error retrieving cart and order_items data');
      } else {
        res.send(result);
      }
    });
  });
  

  app.get('/cart/order_items/:id', (req, res) => {
    const customer_id = req.params.id;
    const query = `SELECT c.cart_id,c.total_amount, c.customer_id, oi.order_item_id, oi.product_id, oi.quantity, oi.item_price
                   FROM cart c
                   JOIN order_items oi ON c.cart_id = oi.cart_id where c.customer_id = ${customer_id}`;
    db.query(query, (err, result) => {
      if (err) {
        console.error(err);
        res.status(500).send('Error retrieving cart and order_items data');
      } else {
        res.send(result);
      }
    });
  });


app.listen(3000,(req,res)=>{
    console.log("listening of port 3000")
})

