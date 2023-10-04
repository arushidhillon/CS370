
document.querySelector("form.Biographyform").addEventListener("submit", function(event) {
    event.preventDefault();
    document.getElementById("target").innerText = document.getElementById("bio").value;
});

document.querySelector("form.Courseform").addEventListener("submit", function(event) {
    event.preventDefault();
 document.getElementById("target2").innerText = document.getElementById("course").value;

});
  
function SavePhoto(e) 
{
    let user = { name:'john', age:34 };
    let xhr = new XMLHttpRequest();
    let formData = new FormData();
    let photo = e.files[0];      
    
    formData.append("user", JSON.stringify(user));   
    formData.append("photo", photo);
    
    xhr.onreadystatechange = state => { console.log(xhr.status); } // err handling
    xhr.timeout = 5000;
    xhr.open("POST", '/upload/image'); 
    xhr.send(formData);
}

document.getElementById("addSkill").onclick  = function() {

    var node = document.createElement("Li");
    var text = document.getElementById("Skill_input").value; 
    var textnode=document.createTextNode(text);
    node.appendChild(textnode);
    document.getElementById("Skill_item").appendChild(node);
}

document.getElementById("addCourse").onclick  = function() {

    var node = document.createElement("Li");
    var text = document.getElementById("Course_input").value; 
    var textnode=document.createTextNode(text);
    node.appendChild(textnode);
    document.getElementById("Course_item").appendChild(node);
}