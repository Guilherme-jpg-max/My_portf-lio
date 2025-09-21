document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll("nav ul li a");

    function setActiveLink() {
        let currentSection = "";

        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            if (rect.top <= 0 && rect.bottom >= 0) {
                currentSection = section.id;
            }
        });

        navLinks.forEach(link => {
            if (link.getAttribute("href").includes(currentSection)) {
                link.classList.add("active");
            } else {
                link.classList.remove("active");
            }
        });
    }

    setActiveLink();

    window.addEventListener("scroll", setActiveLink);

    function toggleMenu() {
        const menu = document.querySelector('nav ul');
        menu.classList.toggle('active');
    }

    const menuHamburguer = document.querySelector('.menu-hamburguer');
    if (menuHamburguer) {
        menuHamburguer.addEventListener('click', toggleMenu);
    }
});
