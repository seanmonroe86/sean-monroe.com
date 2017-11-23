var express = require('express');
var router = express.Router();

/* GET login. */
router.get('/', get_login);

/* POST login. */
router.post('/', send_login);

module.exports = router;
