const express = require("express");
const bodyParser = require("body-parser");
require("dotenv").config();
// const cors = require("cors");
// const helmet = require("helmet");
// const morgan = require("morgan");
port = process.env.PORT;

app = express();

// adding Helmet to enhance your API's security
// app.use(helmet());
// using bodyParser to parse JSON bodies into JS objects
app.use(bodyParser.json());
// enabling CORS for all requests
// app.use(cors());
// adding morgan to log HTTP requests
// app.use(morgan("combined"));

app.use("/codeforces", require("./routes/site.route"));

app.listen(port, () => {
	console.log(`Listening at port ${port}`);
});
