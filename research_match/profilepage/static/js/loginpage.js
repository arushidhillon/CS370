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

