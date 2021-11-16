/* sort.js 
 Written by Thien K. M. Bui and Robbie Young 
 Last updated Nov 15 2021 

 Simple sorting from localStorage
*/

const initSortBy = () => {
	const sortBySelect = document.getElementById("sort-by-select");
	sortBySelect.onchange = sort;
};

const sort = () => {
	const sortBySelect = document.getElementById("sort-by-select");
	const sortBy = sortBySelect.value;
	switch (sortBy) {
		case "title":
			if (window.localStorage.getItem("searched-results")) {
				const jsonStorage = JSON.parse(
					window.localStorage.getItem("searched-results")
				);
				const jsonContent = jsonStorage.sort((a, b) => {
					if (a.title < b.title) {
						return -1;
					} else {
						return 1;
					}
				});
				const formattedContents = jsonContent.map((content) => {
					return `
					<div class="content-container">
						<div class="content">
							<div class="content-title">
								<strong>${content.title}</strong>
								(${content.type})
								${content.release_year}
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
			}
			break;
		case "release_year":
			if (window.localStorage.getItem("searched-results")) {
				const jsonStorage = JSON.parse(
					window.localStorage.getItem("searched-results")
				);
				const jsonContent = jsonStorage.sort((a, b) => {
					if (a.release_year > b.release_year) {
						return -1;
					} else {
						return 1;
					}
				});
				const formattedContents = jsonContent.map((content) => {
					return `
                    <div class="content-container">
                        <div class="content">
                            <div class="content-title">
                                <strong>${content.title}</strong>
                                (${content.type})
                                ${content.release_year}
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
			}
			break;
		case "duration":
			if (window.localStorage.getItem("searched-results")) {
				const jsonStorage = JSON.parse(
					window.localStorage.getItem("searched-results")
				);
				const jsonContent = jsonStorage.sort((a, b) => {
					if (a.duration > b.duration) {
						console.log(a.duration, b.duration, "check this");
						return -1;
					} else {
						return 1;
					}
				});
				const formattedContents = jsonContent.map((content) => {
					return `
                    <div class="content-container">
                        <div class="content">
                            <div class="content-title">
                                <strong>${content.title}</strong>
                                (${content.type})
                                ${content.release_year}
                                ${content.duration}
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
			}
			break;
		default:
			window.alert("something went wrong, please refresh the page");
	}
};

window.addEventListener("load", initSortBy, true);
