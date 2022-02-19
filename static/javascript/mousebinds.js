import {speech, next,prev} from "./main.js";

var synth = window.speechSynthesis;

Mousetrap.bind('right', () =>  next());
Mousetrap.bind('left', () => prev());
Mousetrap.bind('space', () => {
    if(synth.paused){
        synth.resume();
        console.log("resume");
    }
    else{
        synth.pause();
        console.log("paused");
    }
});
Mousetrap.bind('enter', () => {
    if(synth.paused){
        synth.cancel();
        console.log("paused cancelling");
    }
    else if (synth.speaking) {
        synth.cancel();  
        console.log("cancelled");
    } 
    else{
        speech.text = document.querySelector("#text p").textContent;
        window.speechSynthesis.speak(speech);
        console.log("start");
    }
});