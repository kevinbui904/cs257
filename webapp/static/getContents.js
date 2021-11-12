/*getContents.js 
Thien K. M. Bui and Robbie Young 08 November 2021
Updated 08 November 2021


Helper methods to fetch data from our api.py
*/

const getAPIBaseUrl = () => {
	const baseUrl = `${window.location.protocol}//${window.location.hostname}:${window.location.port}/api`;

	return baseUrl;
};

// Recommend handler
const initGetRecommended = () => {
	const recommendButton = document.getElementById("recommend-button");
	recommendButton.onclick = onRecommendButtonClicked;
};

const onRecommendButtonClicked = () => {
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
                <div id="content-container">
                    <div class="content">
                        <div id="content-title">
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
const initGetByTitle = () => {
	const titleButton = document.getElementById("by-title-button");
	titleButton.onclick = onTitleButtonClicked;
};

const onTitleButtonClicked = (e) => {
	e.preventDefault();

	const titleInput = document.getElementById("by-title-input");

	const titleString = titleInput.value;
	//making sure that input isn't blank
	if (titleInput && titleString) {
		const url = getAPIBaseUrl() + `/titles/${titleString}`;
		// send GET request to specified URL
		fetch(url, { method: "GET" })
			.then((response) => response.json())
			.then((jsonContent) => {
				const formattedContents = jsonContent.map((content) => {
					return `
					<div id="content-container">
						<div class="content">
							<div id="content-title">
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
	} else {
		window.alert("required field can not be null");
	}
};

//------------------------- by directors handler
const initGetByDirector = () => {
	const directorsButton = document.getElementById("by-director-button");
	directorsButton.onclick = onDirectorButtonClicked;
};

const onDirectorButtonClicked = (e) => {
	e.preventDefault();

	const directorInput = document.getElementById("by-director-input");

	const directorString = directorInput.value;
	//making sure that input isn't blank
	if (directorInput && directorString) {
		const url = getAPIBaseUrl() + `/directors/${directorString}`;
		// send GET request to specified URL
		fetch(url, { method: "GET" })
			.then((response) => response.json())
			.then((jsonContent) => {
				const formattedContents = jsonContent.map((content) => {
					return `
					<div id="content-container">
						<div class="content">
							<div id="content-title">
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
	} else {
		window.alert("required field can not be null");
	}
};

//------------------------ by cast handler
const initGetByCast = () => {
	const titleButton = document.getElementById("by-cast-button");
	titleButton.onclick = onCastButtonClicked;
};

const onCastButtonClicked = (e) => {
	e.preventDefault();

	const castInput = document.getElementById("by-cast-input");

	const castString = castInput.value;
	//making sure that input isn't blank
	if (castInput && castString) {
		const url = getAPIBaseUrl() + `/cast/${castString}`;
		// send GET request to specified URL
		fetch(url, { method: "GET" })
			.then((response) => response.json())
			.then((jsonContent) => {
				const formattedContents = jsonContent.map((content) => {
					return `
					<div id="content-container">
						<div class="content">
							<div id="content-title">
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
	} else {
		window.alert("required field can not be null");
	}
};
window.addEventListener("load", initGetRecommended, true);
window.addEventListener("load", initGetByTitle, true);
window.addEventListener("load", initGetByDirector, true);
window.addEventListener("load", initGetByCast, true);
