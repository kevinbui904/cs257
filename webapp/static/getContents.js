/*getContents.js 
Thien K. M. Bui and Robbie Young 08 November 2021
Updated 15 November 2021


Helper methods to fetch data from our api.py
For use in Carleton CS 251 Fall 2021
*/

const getAPIBaseUrl = () => {
	const baseUrl = `${window.location.protocol}//${window.location.hostname}:${window.location.port}/api`;
	return baseUrl;
};

const getRecommended = () => {
	const genre = document.getElementById("genre-select");
	const genreString = genre.value;
	const url = `${getAPIBaseUrl()}/recommended?genre=${genreString}`;
	// send GET request to specified URL
	fetch(url, { method: "GET" })
		.then((response) => response.json())
		.then((jsonResponse) => {
			let contentHTML = "";
			//internal agreement, API will ONLY ever return 1 object in a list of size 1
			const content = jsonResponse[0];
			contentHTML = `
                <div class="content-container">
                    <div class="content">
                        <div class="content-title">
                            <strong>${content.title}</strong>
							(${content.type})
                        </div>
                        <div class="content-subheading">
                            <strong>Director(s):</strong> ${content.directors}
                        </div>
                        <div class="content-subheading">
                            <strong>Cast(s):</strong> ${content.cast}
                        </div>
						<div class="content-subheading">
							<strong>Genre(s):</strong> ${content.listed_in}
						</div>
                        <div class="content-sypnopsis">
                            <strong>Sypnopsis:</strong>
                            ${content.description}
                        </div>
                    </div>
                </div> 
            `;
			const recommendedContainer = document.getElementById(
				"recommended-container"
			);
			recommendedContainer.innerHTML = contentHTML;
		});
};

//------------------------- by title handler

const getByTitle = (titleString) => {
	const url = getAPIBaseUrl() + `/titles/${titleString}`;
	// send GET request to specified URL
	fetch(url, { method: "GET" })
		.then((response) => response.json())
		.then((jsonContent) => {
			const formattedContents = jsonContent.map((content) => {
				return `
				<div class="content-container">
					<div class="content">
						<div class="content-title">
							<strong>${content.title}</strong>
							(${content.type})
						</div>
						<div class="content-subheading">
							<strong>Director(s):</strong> ${content.directors}
						</div>
						<div class="content-subheading">
							<strong>Cast(s):</strong> ${content.cast}
						</div>
						<div class="content-subheading">
							<strong>Genre(s):</strong> ${content.listed_in}
						</div>
						<div class="content-sypnopsis">
							<strong>Sypnopsis:</strong>
							${content.description}
						</div>
					</div>
				</div> 
			`;
			});
			const contentsContainer = document.getElementById("contents-container");
			contentsContainer.innerHTML = formattedContents;
		});
};

//------------------------- by directors

const getByDirector = (directorString) => {
	const url = getAPIBaseUrl() + `/directors/${directorString}`;
	// send GET request to specified URL
	fetch(url, { method: "GET" })
		.then((response) => response.json())
		.then((jsonContent) => {
			const formattedContents = jsonContent.map((content) => {
				return `
				<div class="content-container">
					<div class="content">
						<div class="content-title">
							<strong>${content.title}</strong>
							(${content.type})
						</div>
						<div class="content-subheading">
							<strong>Director(s):</strong> ${content.directors}
						</div>
						<div class="content-subheading">
							<strong>Cast(s):</strong> ${content.cast}
						</div>
						<div class="content-subheading">
							<strong>Genre(s):</strong> ${content.listed_in}
						</div>
						<div class="content-sypnopsis">
							<strong>Sypnopsis:</strong>
							${content.description}
						</div>
					</div>
				</div> 
			`;
			});
			const contentsContainer = document.getElementById("contents-container");
			contentsContainer.innerHTML = formattedContents;
		});
};

//------------------------ by cast
const getByCast = (castString) => {
	const url = getAPIBaseUrl() + `/cast/${castString}`;
	// send GET request to specified URL
	fetch(url, { method: "GET" })
		.then((response) => response.json())
		.then((jsonContent) => {
			const formattedContents = jsonContent.map((content) => {
				return `
				<div class="content-container">
					<div class="content">
						<div class="content-title">
							<strong>${content.title}</strong>
							(${content.type})
						</div>
						<div class="content-subheading">
							<strong>Director(s):</strong> ${content.directors}
						</div>
						<div class="content-subheading">
							<strong>Cast(s):</strong> ${content.cast}
						</div>
						<div class="content-subheading">
							<strong>Genre(s):</strong> ${content.listed_in}
						</div>
						<div class="content-sypnopsis">
							<strong>Sypnopsis:</strong>
							${content.description}
						</div>
					</div>
				</div> 
			`;
			});
			const contentsContainer = document.getElementById("contents-container");
			contentsContainer.innerHTML = formattedContents;
		});
};

//on window load, recommend a random content
window.onload = getRecommended;
