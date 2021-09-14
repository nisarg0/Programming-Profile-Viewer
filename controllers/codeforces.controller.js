const axios = require("axios");

exports.codeforces = async (request, response) => {
	const id = request.query.id;
	console.log(id);

	var user_details = await axios.get(
		`https://codeforces.com/api/user.info?handles=${id}`
	);
	var contest_details = await axios.get(
		`https://codeforces.com/api/user.rating?handle=${id}`
	);
	console.log(contest_details.data);

	https: response.send("Success");
};
