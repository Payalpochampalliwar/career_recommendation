document.addEventListener("DOMContentLoaded", function () {
  console.log("Login/Register page loaded");

  document.querySelector("form").addEventListener("submit", function (event) {
      event.preventDefault();
      alert("Form submitted!");
  });
});

