const current = document.getElementById("matches-current");
const past = document.getElementById("matches-past");

// Creates matches on opportunities page
function addMatchElement(imgSrc, header, subtitle, tags, desc, section) {
  // Div container
  var matchDiv = document.createElement("div");
  matchDiv.classList.add("match");

  // Image
  var img = document.createElement("img");
  img.classList.add("thumbnail");
  img.src = imgSrc;
  matchDiv.appendChild(img);

  // Title container
  var title = document.createElement("div");
  title.classList.add("matchTitle");
  matchDiv.appendChild(title);
  var titleHeader = document.createElement("h1"); // name of lab
  titleHeader.textContent = header;
  title.appendChild(titleHeader);
  var titleSubheader = document.createElement("h2"); // lab subtitle
  titleSubheader.textContent = subtitle;
  title.appendChild(titleSubheader);

  // Lab info container
  var infoContainer = document.createElement("div");
  infoContainer.classList.add("matchInfo");
  title.appendChild(infoContainer);

  var cluster = document.createElement("div"); // tags
  cluster.classList.add("tagscluster");
  for (let i = 0; i < tags.length; i++) {
    var tag = document.createElement("div");
    tag.classList.add("child");
    tag.textContent = tags[i];
    cluster.appendChild(tag);
  }
  infoContainer.appendChild(cluster);

  var info = document.createElement("p"); // description
  info.classList.add("matchText");
  info.textContent = desc;
  infoContainer.appendChild(info);

  // Buttons container
  var buttons = document.createElement("div");
  buttons.classList.add("matchButtonsDiv");
  matchDiv.appendChild(buttons);
  var messageButton = document.createElement("button"); // message button
  messageButton.classList.add("matchButtons");
  messageButton.textContent = "Message";
  buttons.appendChild(messageButton);
  var matchButton = document.createElement("button"); // match button
  matchButton.classList.add("matchButtons");
  matchButton.textContent = "Match";
  buttons.appendChild(matchButton);
  var viewFullProfileButton = document.createElement("button"); // view full profile button
  viewFullProfileButton.classList.add("matchButtons");
  viewFullProfileButton.textContent = "View Full Profile";
  buttons.appendChild(viewFullProfileButton);

  section.appendChild(matchDiv);
}

// var test = "{% static '/placeholder/lab1.jpeg' %}";
// const tags1 = ["Biotechnology", "Biology", "Environmental Science"];
// const tags2 = [
//   "Computer Science",
//   "Artificial Intelligence",
//   "Machine Learning",
// ];
// // Some examples
// // Descriptions generated using ChatGPT
// addMatchElement(
//   test,
//   "Name",
//   "Student@emory.edu",
//   tags1,
//   "Student Bio.",
//   current
// );
// addMatchElement(
//   "{% static '/placeholder/lab2.jpeg' %}",
//   "Name",
//   "Name@emory.edu",
//   tags1,
//   "I am a biology student who likes to eat cheese!.",
//   past
// );
// // addMatchElement(
// //   "{% static '/placeholder/lab3.jpg' %}",
// //   "Dooley's CS Lab",
// //   "dooleylab@emory.edu",
// //   tags2,
// //   "Welcome to Dooley's CS Lab, where innovation meets computation in the heart of our digital realm. Named after the legendary computer scientist, Dooley's Lab is a sanctuary for the curious minds of the tech world. With a dazzling array of cutting-edge hardware and software, our lab serves as a launchpad for coding enthusiasts, aspiring AI researchers, and cybernetic pioneers alike. Our mission is to push the boundaries of computer science through rigorous experimentation and collaboration. From machine learning and data analytics to cybersecurity and software engineering, our diverse range of projects will challenge and inspire you. Join us in the pursuit of ones and zeros as we explore the infinite possibilities of the digital age within the welcoming confines of Dooley's CS Lab.",
// //   past
// // );
