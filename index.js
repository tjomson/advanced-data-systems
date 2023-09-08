const duckdb = require("duckdb");

const db = new duckdb.Connection();

const conn = db.connect();

db.all("select * from weather", (err, res) => {
  if (err) throw err;
  console.log(res);
});
