let signup = document.querySelector(".signup");
let student = document.querySelector(".student");
let lab = document.querySelector(".lab");
let slider = document.querySelector(".slider");
let formSection = document.querySelector(".form-section");

signup.addEventListener("click", () => {
  if (lab.hasAttribute("id")) {
    lab.removeAttribute("id");
  }
  if (student.hasAttribute("id")) {
    student.removeAttribute("id");
  }
  signup.setAttribute("id", "selected");
  if (slider.classList.contains("moveslider")) {
    slider.classList.remove("moveslider");
  }
  slider.classList.add("moveslider2");
  formSection.classList.add("form-section-move2");
});

student.addEventListener("click", () => {
  if (lab.hasAttribute("id")) {
    lab.removeAttribute("id");
  }
  if (signup.hasAttribute("id")) {
    signup.removeAttribute("id");
  }
  student.setAttribute("id", "selected");
  slider.classList.remove("moveslider");
  slider.classList.remove("moveslider2");
  formSection.classList.remove("form-section-move");
  formSection.classList.remove("form-section-move2");
});

lab.addEventListener("click", () => {
  if (student.hasAttribute("id")) {
    student.removeAttribute("id");
  }
  if (signup.hasAttribute("id")) {
    signup.removeAttribute("id");
  }
  lab.setAttribute("id", "selected");
  slider.classList.add("moveslider");
  slider.classList.remove("moveslider2");
  formSection.classList.add("form-section-move");
  formSection.classList.remove("form-section-move2");
});
