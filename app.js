const express = require('express');
const { Pool } = require('pg');

const app = express();
const PORT = 3000;

const pool = new Pool({
  user: 'postgres',
  host: '127.0.0.1',
  database: 'joy_of_painting',
  password: '2016',
  port: '5432',
});

app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next();
});

app.get('/', (req, res) => {
    res.send('Welcome to Joy of Painting!');
});

app.get('/episodes', async (req, res) => {
  try {
    const queryResult = await pool.query('SELECT * FROM episodes');
    res.json(queryResult.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

app.get('/colors', async (req, res) => {
  try {
    const queryResult = await pool.query('SELECT * FROM colors');
    res.json(queryResult.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

app.get('/subjects', async (req, res) => {
  try {
    const queryResult = await pool.query('SELECT * FROM subjects');
    res.json(queryResult.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

app.get('/color_id/:color_id', async (req, res) => {
  const color_id = req.params.color_id;
  try {
    const query = {
      text: `SELECT * FROM episodes WHERE ',' || colors || ',' LIKE $1`,
      values: [`%,${color_id},%`],
    };
    const result = await pool.query(query);
    res.json(result.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

app.get('/color_name/:color_name', async (req, res) => {
  const color_name = req.params.color_name;
  try {
    const query = {
      text: `SELECT * FROM episodes WHERE ',' || colors || ',' LIKE '%,' || (SELECT color_id::varchar FROM colors WHERE color_name = $1) || ',%';`,
      values: [color_name],
    };
    const result = await pool.query(query);
    res.json(result.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

app.get('/subject_id/:subject_id', async (req, res) => {
  const subject_id = req.params.subject_id;
  try {
    const query = {
      text: `SELECT * FROM episodes WHERE ',' || subjects || ',' LIKE $1`,
      values: [`%,${subject_id},%`],
    };
    const result = await pool.query(query);
    res.json(result.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

app.get('/subject_name/:subject_name', async (req, res) => {
  const subject_name = req.params.subject_name;
  try {
    const query = {
      text: `SELECT * FROM episodes WHERE ',' || subjects || ',' LIKE '%,' || (SELECT subject_id::varchar FROM subjects WHERE subject_name = $1) || ',%';`,
      values: [subject_name],
    };
    const result = await pool.query(query);
    res.json(result.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

app.get('/month/:month_name', async (req, res) => {
  const month_name = req.params.month_name;
  try {
    const query = {
      text: `SELECT * FROM episodes WHERE month = $1;`,
      values: [month_name],
    };
    const result = await pool.query(query);
    res.json(result.rows);
  } catch (error) {
    console.error('Error executing query', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});


app.listen(PORT, () => {
  console.log(`Server is running and listening on port ${PORT}`);
});
