
document.querySelectorAll(".question-box").forEach(box =>{
    box.addEventListener("click" , ()=>{
        let p = box.querySelector("p");
        if(p.style.height === "0px" || p.style.height === ""){
            p.style.height = p.scrollHeight + "px";
        } else {
            p.style.height = "0px"
        }
    });
});