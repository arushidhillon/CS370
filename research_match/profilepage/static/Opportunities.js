const matches = document.getElementById("matches");

// Creates matches on opportunities page
function addMatchElement(imgSrc, header, subtitle, desc) {
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

  // Lab description
  var infoContainer = document.createElement("div");
  infoContainer.classList.add("matchInfo");
  title.appendChild(infoContainer);
  var info = document.createElement("p");
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

  matches.appendChild(matchDiv);
}

// Some examples
// Descriptions generated using ChatGPT
addMatchElement(
  "{% static '/placeholder/lab1.jpg' %}",
  "XYZ Research Lab",
  "XYZresearchlab@emory.edu",
  "Welcome to the exciting world of the XYZ Research Lab, where innovation knows no bounds and curiosity fuels our quest for knowledge! Our cutting-edge lab is currently seeking passionate and driven students to join our dynamic research team. Nestled at the forefront of scientific discovery, our lab is dedicated to pushing the boundaries of human understanding in fields such as biotechnology, artificial intelligence, and environmental science. As a student researcher here, you'll have the opportunity to work alongside world-class scientists, engage in groundbreaking experiments, and contribute to projects that have the potential to change the world. Whether you're a budding biologist, a tech enthusiast, or an environmental advocate, our lab offers a diverse range of opportunities to explore, learn, and grow. Join us on this thrilling journey of exploration, innovation, and discovery, and be part of a team that is shaping the future of science."
);
addMatchElement(
  "{% static '/placeholder/lab2.jpg' %}",
  "Biology Laboratory",
  "biologylaboratory@emory.edu",
  "Welcome to our state-of-the-art Biology Laboratory, a hub of scientific exploration and discovery. Here, we delve deep into the intricate web of life, unraveling its mysteries one experiment at a time. Our lab is a haven for inquisitive minds, whether you are a seasoned researcher or a budding scientist eager to embark on your journey. Equipped with cutting-edge technology and staffed by a team of dedicated experts, our Biology Lab offers a diverse range of research opportunities, from genetic studies and ecological investigations to microbiological explorations. We are committed to fostering innovation, advancing our understanding of the natural world, and contributing to the global body of biological knowledge. Join us in the pursuit of answers, as we uncover the secrets of life itself in our dynamic and collaborative research environment."
);
addMatchElement(
  "{% static '/placeholder/lab3.jpg' %}",
  "Dooley's CS Lab",
  "dooleylab@emory.edu",
  "Welcome to Dooley's CS Lab, where innovation meets computation in the heart of our digital realm. Named after the legendary computer scientist, Dooley's Lab is a sanctuary for the curious minds of the tech world. With a dazzling array of cutting-edge hardware and software, our lab serves as a launchpad for coding enthusiasts, aspiring AI researchers, and cybernetic pioneers alike. Our mission is to push the boundaries of computer science through rigorous experimentation and collaboration. From machine learning and data analytics to cybersecurity and software engineering, our diverse range of projects will challenge and inspire you. Join us in the pursuit of ones and zeros as we explore the infinite possibilities of the digital age within the welcoming confines of Dooley's CS Lab."
);
