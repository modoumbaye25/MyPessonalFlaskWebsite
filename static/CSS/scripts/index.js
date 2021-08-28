// document.querySelector("#bank-btn").addEventListener("click", function() {
//     if (document.querySelector(".bank-desc").style.display === "none"){
//         document.querySelector(".bank-desc").style.display = "block";
//         document.querySelector("#bank-btn").textContent = "Hide Description";
//     } else {
//         document.querySelector(".bank-desc").style.display = "none";
//         document.querySelector("#bank-btn").textContent = "Show Description";
//     }
// });

$("#aws-btn").on("click", function() {
    $(".aws-desc").toggle();
    $(this).text(function(i, text){
          return text === "Show Description" ? "Hide Description" : "Show Description";
      })
})

$("#bank-btn").on("click", function() {
    $(".bank-desc").toggle();
    $(this).text(function(i, text){
          return text === "Show Description" ? "Hide Description" : "Show Description";
      })
})

$("#more-summary-btn").on("click", function() {
    $(".more-summary").toggle();
    $(this).text(function(i, text){
          return text === "... see more" ? "see less" : "... see more";
      })
})


