var axios = require('axios');
var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
	axios.get('http://localhost:8000/database')
		.then(function(response){
			//res.send("Yay");
			res.send(response.data);
			console.log(response.data);
		});
});

module.exports = router;
