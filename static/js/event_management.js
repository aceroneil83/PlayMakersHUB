function setActiveNavItem(event) {
  event.preventDefault();

  // Remove active class from all nav items
  const navItems = document.querySelectorAll(".nav-item");
  navItems.forEach((item) => item.classList.remove("active"));

  // Hide all content sections
  const contentSections = document.querySelectorAll(".content-section");
  contentSections.forEach((section) => section.classList.add("hidden"));

  // Add active class to clicked nav item
  const target = event.target;
  target.classList.add("active");

  const test = document.querySelectorAll(".nav-li");
  test.forEach((item) => item.classList.add("bg-amber-600"));

  // Show the corresponding content section
  const contentId = target.getAttribute("data-target");
  document.getElementById(contentId).classList.remove("hidden");
}

function toggleDropdown(event) {
  event.preventDefault();
  const dropdownMenu = event.target.closest("button").nextElementSibling;
  dropdownMenu.classList.toggle("hidden");
}

// Close dropdowns if clicked outside
window.onclick = function (event) {
  if (
    !event.target.matches(".dropdown-menu") &&
    !event.target.matches(".dropdown-menu *") &&
    !event.target.matches("button")
  ) {
    const dropdowns = document.querySelectorAll(".dropdown-menu");
    dropdowns.forEach((dropdown) => {
      if (!dropdown.classList.contains("hidden")) {
        dropdown.classList.add("hidden");
      }
    });
  }
};

// Add event listeners to nav items
document.querySelectorAll(".nav-item").forEach((button) => {
  button.addEventListener("click", setActiveNavItem);
});

// Add event listeners to dropdown items
document.querySelectorAll(".dropdown-menu button").forEach((button) => {
  button.addEventListener("click", setActiveNavItem);
});
