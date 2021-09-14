const express = require("express");
router = express.Router();

sites = require("../controllers/userDetails.controller");

router.get("/codeforces", sites.codeforces);
router.get("/codechef", sites.codechef);

module.exports = router;
