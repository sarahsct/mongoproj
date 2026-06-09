const navToggle = document.querySelector("[data-nav-toggle]");
const navMenu = document.querySelector("[data-nav-menu]");
const header = document.querySelector("[data-header]");

if (navToggle && navMenu) {
  navToggle.addEventListener("click", () => {
    const isOpen = navMenu.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });
}

if (header) {
  const syncHeader = () => {
    header.classList.toggle("is-scrolled", window.scrollY > 16);
  };

  syncHeader();
  window.addEventListener("scroll", syncHeader, { passive: true });
}

const revealItems = document.querySelectorAll(".reveal");

if ("IntersectionObserver" in window) {
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.14 }
  );

  revealItems.forEach((item) => revealObserver.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add("is-visible"));
}

const commentForm = document.querySelector("[data-comment-form]");
const commentList = document.querySelector("[data-comment-list]");

if (commentForm && commentList) {
  commentForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(commentForm);
    const name = String(formData.get("name") || "").trim();
    const comment = String(formData.get("comment") || "").trim();

    if (!name || !comment) {
      return;
    }

    const emptyComment = commentList.querySelector(".empty-comment");
    if (emptyComment) {
      emptyComment.remove();
    }

    const card = document.createElement("article");
    card.className = "comment-card";
    card.innerHTML = `
      <div>
        <strong></strong>
        <time>Just now</time>
      </div>
      <p></p>
    `;
    card.querySelector("strong").textContent = name;
    card.querySelector("p").textContent = comment;

    commentList.prepend(card);
    commentForm.reset();
  });
}
