document.addEventListener("DOMContentLoaded", function () {
  console.log("🚀 Page Loaded!");

  const form = document.querySelector("form");
  const usernameField = document.getElementById("username");
  const passwordField = document.getElementById("password");

  if (!form) {
      console.error("❌ Form not found!");
      return;
  }

  if (!usernameField || !passwordField) {
      console.error("❌ Username or Password field not found!");
      return;
  }

  form.addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent default form submission for debugging

      console.log("📩 Form Submitted!");
      console.log("Username:", usernameField.value);
      console.log("Password:", passwordField.value);

      this.submit(); // Manually submit the form
  });
});

