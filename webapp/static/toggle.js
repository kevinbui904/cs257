/* toggle.js 
Thien K. M. Bui, Robbie Young, 11 Nov 2021

Toggle element script
For use in Carleton CS 251 Fall 2021
*/

const show = (element) => {
	element.style.display = "flex";
};

const hide = (element) => {
	element.style.display = "none";
};

const toggle = (element) => {
	if (window.getComputedStyle(element).display === "flex") {
		hide(element);
		return;
	} else {
		show(element);
	}
};

//Event listener
const initializeToggle = () => {
	const togglable = document.getElementById("togglable");
	const elementToToggle = document.getElementById("advanced-container");

	togglable.addEventListener(
		"click",
		() => {
			toggle(elementToToggle);
		},
		false
	);
};

window.addEventListener("load", initializeToggle, true);
