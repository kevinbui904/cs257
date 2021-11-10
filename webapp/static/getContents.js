/*getContents.js 
Thien K. M. Bui and Robbie Young 08 November 2021
Updated 08 November 2021


Helper methods to fetch data from our api.py
*/

//------------REMOVE BEFORE SUBMISSION -----

const recommendedContent = {
	type: "Movie",
	title: "A Spark Story",
	directors: "Jason Sterman, Leanne Dare",
	casts: "Apthon Corbin, Louis Gonzales",
	date_added: "September 24, 2021",
	release_year: "2021",
	rating: "TV-PG",
	duration: "88 min",
	listed_in: "Documentary",
	description:
		"Two Pixar filmmakers strive to bring their uniquely personal SparkShorts visions to the screen.",
};

const contents = [
	{
		type: "Movie",
		title: "A Spark Story",
		directors: "Jason Sterman, Leanne Dare",
		casts: "Apthon Corbin, Louis Gonzales",
		date_added: "September 24, 2021",
		release_year: "2021",
		rating: "TV-PG",
		duration: "88 min",
		listed_in: "Documentary",
		description:
			"Two Pixar filmmakers strive to bring their uniquely personal SparkShorts visions to the screen.",
	},
	{
		type: "Movie",
		title: "A Spark Story",
		directors: "Jason Sterman, Leanne Dare",
		casts: "Apthon Corbin, Louis Gonzales",
		date_added: "September 24, 2021",
		release_year: "2021",
		rating: "TV-PG",
		duration: "88 min",
		listed_in: "Documentary",
		description:
			"Two Pixar filmmakers strive to bring their uniquely personal SparkShorts visions to the screen.",
	},
	{
		type: "Movie",
		title: "A Spark Story",
		directors: "Jason Sterman, Leanne Dare",
		casts: "Apthon Corbin, Louis Gonzales",
		date_added: "September 24, 2021",
		release_year: "2021",
		rating: "TV-PG",
		duration: "88 min",
		listed_in: "Documentary",
		description:
			"Two Pixar filmmakers strive to bring their uniquely personal SparkShorts visions to the screen.",
	},
	{
		type: "Movie",
		title: "A Spark Story",
		directors: "Jason Sterman, Leanne Dare",
		casts: "Apthon Corbin, Louis Gonzales",
		date_added: "September 24, 2021",
		release_year: "2021",
		rating: "TV-PG",
		duration: "88 min",
		listed_in: "Documentary",
		description:
			"Two Pixar filmmakers strive to bring their uniquely personal SparkShorts visions to the screen.",
	},
	{
		type: "Movie",
		title: "A Spark Story",
		directors: "Jason Sterman, Leanne Dare",
		casts: "Apthon Corbin, Louis Gonzales",
		date_added: "September 24, 2021",
		release_year: "2021",
		rating: "TV-PG",
		duration: "88 min",
		listed_in: "Documentary",
		description:
			"Two Pixar filmmakers strive to bring their uniquely personal SparkShorts visions to the screen.",
	},
];
//-----------------------------------------------

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
	const url = getAPIBaseUrl() + "/recommend";
	//send GET request to specified URL
	// fetch(url , {method: 'GET'})
	//     .then(response => response.json())
	//     .then(recommendedContent => {
	let newContent = `
                <div id="contents-container">
                    <div class="content">
                        <div id="content-title">
                            ${recommendedContent.title}
                        </div>
                        <div class="content-subheading">
                            <strong>Director(s):</strong> ${recommendedContent.directors}
                        </div>
                        <div class="content-subheading">
                            <strong>Cast(s):</strong> ${recommendedContent.casts}
                        </div>
                        <div class="content-sypnopsis">
                            <strong>Sypnopsis:</strong>
                            ${recommendedContent.description}
                        </div>
                    </div>
                </div> 
            `;
	// })
	const recommendedContainer = document.getElementById("recommended-container");

	if (recommendedContainer && recommendedContainer.children.length === 0) {
		recommendedContainer.innerHTML = newContent;
	} else if (
		recommendedContainer &&
		recommendedContainer.children.length !== 0
	) {
		console.log(recommendedContainer.childNodes, "check this");
		recommendedContainer.innerHTML = "";
	}
};

//------------------------- by title handler
const initGetByTitle = () => {
	const titleButton = document.getElementById("by-title-button");
	titleButton.onclick = onTitleButtonClicked;
};

const onTitleButtonClicked = (e) => {
	e.preventDefault();

	const titleInput = document.getElementById("by-title-input");

	//making sure that input isn't blank
	if (titleInput && titleInput.value) {
		const url = getAPIBaseUrl() + "/recommend";
		//send GET request to specified URL
		// fetch(url , {method: 'GET'})
		//     .then(response => response.json())
		//     .then(recommendedContent => {
		const formattedContents = contents.map((content) => {
			return `
			<div id="contents-container">
				<div class="content">
					<div id="content-title">
						${content.title}
					</div>
					<div class="content-subheading">
						<strong>Director(s):</strong> ${content.directors}
					</div>
					<div class="content-subheading">
						<strong>Cast(s):</strong> ${content.casts}
					</div>
					<div class="content-sypnopsis">
						<strong>Sypnopsis:</strong>
						${content.description}
					</div>
				</div>
			</div> 
		`;
		});
		// })
		const contentsContainer = document.getElementById("contents-container");
		//------------------REMOVE BEFORE SUBMISSION---------------
		if (contentsContainer && contentsContainer.children.length !== 0) {
			contentsContainer.innerHTML = "";
		} else if (contentsContainer && contentsContainer.children.length === 0) {
			contentsContainer.innerHTML = formattedContents;
		}
		//----------------------------------------------------------------------
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

	//making sure that input isn't blank
	if (directorInput && directorInput.value) {
		const url = getAPIBaseUrl() + "/recommend";
		//send GET request to specified URL
		// fetch(url , {method: 'GET'})
		//     .then(response => response.json())
		//     .then(recommendedContent => {
		const formattedContents = contents.map((content) => {
			return `
			<div id="contents-container">
				<div class="content">
					<div id="content-title">
						${content.title}
					</div>
					<div class="content-subheading">
						<strong>Director(s):</strong> ${content.directors}
					</div>
					<div class="content-subheading">
						<strong>Cast(s):</strong> ${content.casts}
					</div>
					<div class="content-sypnopsis">
						<strong>Sypnopsis:</strong>
						${content.description}
					</div>
				</div>
			</div> 
		`;
		});
		// })
		const contentsContainer = document.getElementById("contents-container");
		//------------------REMOVE BEFORE SUBMISSION---------------
		if (contentsContainer && contentsContainer.children.length !== 0) {
			contentsContainer.innerHTML = "";
		} else if (contentsContainer && contentsContainer.children.length === 0) {
			contentsContainer.innerHTML = formattedContents;
		}
		//----------------------------------------------------------------------
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
	const url = getAPIBaseUrl() + "/recommend";

	const castInput = document.getElementById("by-cast-input");

	//making sure that input isn't blank
	if (castInput && castInput.value) {
		const url = getAPIBaseUrl() + "/recommend";
		//send GET request to specified URL
		// fetch(url , {method: 'GET'})
		//     .then(response => response.json())
		//     .then(recommendedContent => {
		const formattedContents = contents.map((content) => {
			return `
			<div id="contents-container">
				<div class="content">
					<div id="content-title">
						${content.title}
					</div>
					<div class="content-subheading">
						<strong>Director(s):</strong> ${content.directors}
					</div>
					<div class="content-subheading">
						<strong>Cast(s):</strong> ${content.casts}
					</div>
					<div class="content-sypnopsis">
						<strong>Sypnopsis:</strong>
						${content.description}
					</div>
				</div>
			</div> 
		`;
		});
		// })
		const contentsContainer = document.getElementById("contents-container");
		//------------------REMOVE BEFORE SUBMISSION---------------
		if (contentsContainer && contentsContainer.children.length !== 0) {
			contentsContainer.innerHTML = "";
		} else if (contentsContainer && contentsContainer.children.length === 0) {
			contentsContainer.innerHTML = formattedContents;
		}
		//----------------------------------------------------------------------
	} else {
		window.alert("required field can not be null");
	}
};
window.addEventListener("load", initGetRecommended, true);
window.addEventListener("load", initGetByTitle, true);
window.addEventListener("load", initGetByDirector, true);
window.addEventListener("load", initGetByCast, true);
