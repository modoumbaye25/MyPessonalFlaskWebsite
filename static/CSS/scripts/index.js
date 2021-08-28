document.querySelector("#bank-btn").addEventListener("click", function() {
    if (document.querySelector(".description").style.display === "none"){
        document.querySelector(".description").style.display = "block";
        document.querySelector("#bank-btn").textContent = "Hide Description";
    } else {
        document.querySelector(".description").style.display = "none";
        document.querySelector("#bank-btn").textContent = "Show Description";
    }
    // document.querySelector(".description").style.color = "red"
});

$("#aws-btn").on("click", function() {
    $(".aws-desc").toggle();
    if ($(this).text = "Show Description") {
        $(this).text("Hide Description")
    }
    else {
        $(this).text("Show Description")
    }
})
