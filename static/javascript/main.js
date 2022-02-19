export var speech

//var array = ["loerem ipsum,,,,,,,,, ",'heloo??']

var img_num = 0;
var text_num = 0;

let voices = []; // global array of available voices

window.onload= () => {
    speech = new SpeechSynthesisUtterance();
    voices = window.speechSynthesis.getVoices();
    speech.voice = voices[0];
    let voiceSelect = document.querySelector("#voices");
    let x = 0;
    voices.forEach((voice, i) => {
      if (voice.name.includes("English")) {
      voiceSelect.options[x] = new Option(voice.name, i);
      x = x+1;
      }
    });
};

document.querySelector("#rate").addEventListener("input", () => {
 const rate = document.querySelector("#rate").value;

  speech.rate = rate;
  document.querySelector("#rate-label").innerHTML = rate;
});

document.querySelector("#pitch").addEventListener("input", () => {
  // Get pitch Value from the input
  const pitch = document.querySelector("#pitch").value;

  // Set pitch property of the SpeechSynthesisUtterance instance
  speech.pitch = pitch;

  // Update the pitch label
  document.querySelector("#pitch-label").innerHTML = pitch;
});

document.querySelector("#start").addEventListener("click", () => {
  speech.voice = voices[document.querySelector("#voices").value];
  speech.text = document.querySelector("#text p").textContent;
  window.speechSynthesis.speak(speech);
});

document.querySelector("#pause").addEventListener("click", () => {
  window.speechSynthesis.pause();
});

document.querySelector("#resume").addEventListener("click", () => {
  window.speechSynthesis.resume();
});

document.querySelector("#cancel").addEventListener("click", () => {
  window.speechSynthesis.cancel();
});

//collapse open
var pdf_collapse = document.querySelector("#pdf_collapse_icon p");
pdf_collapse.addEventListener("click", () => {
  var elem = document.getElementsByClassName("collapsible_pdf_section")[0];
  elem.classList.toggle("collapse");
});

var videos_collapse = document.querySelector("#videos_collapse_icon p");
videos_collapse.addEventListener("click", () => {
  var elem = document.getElementsByClassName("collapsible_videos_section")[0];
  elem.classList.toggle("collapse");
});

//text in area
document.querySelector("#text p").innerHTML = array[0];
document.getElementById("text_sync_left").addEventListener("click", () =>{
  text_sync(-1);
});

document.getElementById("text_sync_right").addEventListener("click", () =>{
  text_sync(1);
});

function text_sync(num){
  text_num = text_num + num;
  document.querySelector("#text p").innerHTML = array[text_num];
}

// slide and text controls
var left = document.getElementsByClassName('arrow-left')[0];
var right = document.getElementsByClassName('arrow-right')[0];

export function next(){
  window.speechSynthesis.cancel();
  img_num = img_num + 1;
  text_num = text_num + 1;
  document.querySelector("#text p").innerHTML = array[text_num];
  document.querySelector("#slides img").src = img_src+img_num+".png";
};
export function prev(){
  window.speechSynthesis.cancel();
  img_num = img_num - 1;
  text_num = text_num - 1;
  document.querySelector("#text p").innerHTML = array[text_num];
  document.querySelector("#slides img").src = img_src+img_num+".png";
};

left.addEventListener("click", () =>{
  prev();
  });

right.addEventListener("click", () =>{
 next();
});


// Modal
var modal = document.getElementById("myModal");
var modalImg = document.getElementsByClassName("modal-content")[0];
document.querySelector("#slides img").onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
}

var span = document.getElementsByClassName("close")[0];



span.onclick = function() { 
  modal.style.display = "none";
}
