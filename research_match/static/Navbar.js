const toggle = document.getElementsByClassName("toggle")[0];
const navbar = document.getElementsByClassName("nav-item");

toggle.addEventListener("click", () => {
  navbar.classList.toggle("active");
});
