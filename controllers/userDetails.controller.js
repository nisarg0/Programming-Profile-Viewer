const axios = require("axios");
const { spawn } = require("child_process");

exports.codeforces = async (request, response) => {
	const id = request.query.id;
	console.log(id);

	var result = await axios.get(
		`https://codeforces.com/api/user.info?handles=${id}`
	);
	// var contest_details = await axios.get(
	// 	`https://codeforces.com/api/user.rating?handle=${id}`
	// );
	result = result.data;
	// console.log(user_details.data);

	https: response.send(result);
};

exports.codechef = async (request, response) => {
	// GRPC Trial
	// https://gonzalo123.com/2021/09/13/playing-with-grpc-and-python/

	// const id = request.query.id;
	// console.log(id);
	// var largeDataSet = [];
	// // spawn new child process to call the python script
	// const python = spawn("python", ["/Scraper/codechef.py"]);

	// // collect data from script
	// python.stdout.on("data", async function (data) {
	// 	console.log("Pipe data from python script ...");
	// 	console.log(data);
	// 	largeDataSet.push(data);
	// });
	// // in close event we are sure that stream is from child process is closed
	// python.on("close", (code) => {
	// 	console.log(`child process close all stdio with code ${code}`);
	// 	// send data to browser
	// 	response.send(largeDataSet.join(""));
	// });
	response.send("Succes_codechef");
};
