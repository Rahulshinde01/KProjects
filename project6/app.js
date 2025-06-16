const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello from my-web-app V2!');
});

app.listen(port, () => {
  console.log(`Web application listening at http://localhost:${port}`);
}); 