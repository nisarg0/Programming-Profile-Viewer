const express = require("express");
router = express.Router();

sites = require("../controllers/codeforces.controller");

router.get("/", sites.codeforces);

module.exports = router;
