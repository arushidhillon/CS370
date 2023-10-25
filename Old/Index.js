let signup = document.querySelector(".signup");
let student = document.querySelector(".student");
let lab = document.querySelector(".lab");
let slider = document.querySelector(".slider");
let formSection = document.querySelector(".form-section");
 
signup.addEventListener("click", () => {
    slider.classList.add("moveslider2");
    formSection.classList.add("form-section-move2");
});
 
student.addEventListener("click", () => {
    slider.classList.remove("moveslider");
    slider.classList.remove("moveslider2");
    formSection.classList.remove("form-section-move");
    formSection.classList.remove("form-section-move2");
});

lab.addEventListener("click", () => {
    slider.classList.add("moveslider");
    slider.classList.remove("moveslider2");
    formSection.classList.add("form-section-move");
    formSection.classList.remove("form-section-move2");

});

/*get login and password and authenticate it*/

/*get new signup password and username, add to database (make php file?) Add password requirements (ex. must be 8 characters long)*/
var email = document.getElementById("email");

function validateEmail(email) {
    const regex = /^[^\s@]+@emory.edu$/;
}
