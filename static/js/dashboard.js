function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("hidden");
}

function toggleDropdown(event) {
  event.preventDefault();
  const dropdown = event.currentTarget.nextElementSibling;
  dropdown.classList.toggle("hidden");
}

function setActiveNavItem(event) {
  event.preventDefault();
  document.querySelectorAll(".nav-item").forEach((item) => {
    item.classList.remove("active");
  });
  event.currentTarget.classList.add("active");
}

function showSection(sectionId) {
  const sections = document.querySelectorAll(".content-section");
  sections.forEach((section) => {
    section.classList.add("hidden");
  });
  document.getElementById(sectionId).classList.remove("hidden");

  const buttons = document.querySelectorAll(".nav-button");
  buttons.forEach((button) => {
    button.classList.remove("active");
  });
  document.getElementById(`btn-${sectionId}`).classList.add("active");
}
