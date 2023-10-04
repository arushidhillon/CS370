const currentLabs = document.getElementById("currentLabs");
const pastLabs = document.getElementById("pastLabs");

// adds current labs
function addLab(current, imgSrc, labName, desc, tags) {
  // Container
  var div = document.createElement("div");
  div.classList.add("ProfileBox");

  if (current) {
    currentLabs.appendChild(div);
  } else {
    pastLabs.appendChild(div);
  }

  // container with title and image
  var leftDiv = document.createElement("div");
  leftDiv.classList.add("Labinfo");
  leftDiv.style = "cursor: pointer;";
  leftDiv.onclick = clickLab;
  div.appendChild(leftDiv);
  // Lab Name
  var title = document.createElement("h2");
  title.textContent = labName;
  title.classList.add("LabMemberName");
  leftDiv.appendChild(title);
  // Lab Image
  var img = document.createElement("img");
  img.classList.add("LabPicture");
  img.src = imgSrc;
  img.alt = labName;
  leftDiv.appendChild(img);

  // container with description, email, tags
  var rightDiv = document.createElement("div");
  rightDiv.classList.add("Labinfo");
  rightDiv.style =
    "display: flex;flex-direction: column;justify-content: space-between;width: 100%;margin-left: 2rem;";
  div.appendChild(rightDiv);

  // Info div
  var infoDiv = document.createElement("div");
  infoDiv.classList.add("Info");
  rightDiv.appendChild(infoDiv);

  // info inside infoDiv
  let i = 0;
  while (i < desc.length) {
    var info = document.createElement("span");
    info.classList.add("LabMemberInfo");
    info.textContent = desc[i];
    infoDiv.appendChild(info);
    i++;
  }

  // tagDiv
  var tagDiv = document.createElement("div");
  tagDiv.classList.add("tags");
  rightDiv.appendChild(tagDiv);

  // tags inside tagsDiv
  i = 0;
  while (i < tags.length) {
    var tag = document.createElement("span");
    tag.classList.add("tag");
    tag.textContent = tags[i];
    tagDiv.appendChild(tag);
    i++;
  }
}

function clickLab() {
  console.log("test");
}

var exampleLabDesc = [
  "Position: Student Leader",
  "Email: smith.samantha@emory.edu",
  "Description: Smith Lab focuses on Biochemistry, Biosynthesis, and Microbiology.",
];
var exampleLabTags = ["Biochemistry", "Biosynthesis", "Microbiology"];

addLab(
  true,
  "LaboratoryProfileImage.jpeg",
  "Smith Lab",
  exampleLabDesc,
  exampleLabTags
);

var exampleLabDesc2 = [
  "Position: Student Dooley",
  "Email: dooleylab@emory.edu",
  "Description: Dooley's Lab serves as a launchpad for coding enthusiasts, aspiring AI researchers, and cybernetic pioneers alike. ",
];
var exampleLabTags2 = [
  "Computer Science",
  "Artificial Intelligence",
  "Machine Learning",
];

addLab(
  false,
  "assets/placeholderimages/lab3.jpg",
  "Dooley's CS Lab",
  exampleLabDesc2,
  exampleLabTags2
);
