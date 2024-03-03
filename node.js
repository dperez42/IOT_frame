// npm install pg
// https://tembo.io/docs/postgres_guides/connecting-to-postgres-with-nodejs

const { Client } = require('pg');

const client = new Client({
    user: 'user',
    password: 'password',
    host: 'localhost',
    port: '5432',
    database: 'db',
  });

client.connect()
  .then(() => {
    console.log('Connected to PostgreSQL database');
  })
  .catch((err) => {
    console.error('Error connecting to PostgreSQL database', err);
  });

client.query('SELECT * FROM test', (err, result) => {
    if (err) {
      console.error('Error executing query', err);
    } else {
      console.log('Query result:', result.rows);
    }
  });
/*
client.end()
  .then(() => {
    console.log('Connection to PostgreSQL closed');
  })
  .catch((err) => {
    console.error('Error closing connection', err);
  });
  */